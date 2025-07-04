from fastapi import FastAPI,Depends,HTTPException,status
from app import database,models,schemas
from app.database import SessionLocal, engine,get_db
from sqlalchemy.orm import Session

app = FastAPI()



models.Base.metadata.create_all(bind=database.engine)

# -----------------------In Memory Database-----------------------
# class Item(BaseModel):
#     id: int
#     name: str
#     address: Optional[str] = None




# data = [{ "id": 1, "name": "Item 1","address" : "dowell street"},
#         { "id": 2, "name": "Item 2","address" : "dowell street"},
#         { "id": 3, "name": "Item 3","address" : "dowell street"}    ]
# @app.get("/items")
# def read_root():
#     dataa = [Item(**item) for item in data]
#     return dataa

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     for item in data:
#         if item["id"] == item_id:
#             return Item(**item)
#     return {"error": "Item not found"}

# @app.post("/items/")
# def create_item(item: Item):
#     data.append(item)
#     return item

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     for index, existing_item in enumerate(data):
#         if existing_item["id"] == item_id:
#             data[index] = item.dict()
#             return item
#     return {"error": "Item not found"}  


# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):     
#     for index, item in enumerate(data):
#         if item["id"] == item_id:
#             del data[index]
#             return {"message": "Item deleted successfully"}
#     return {"error": "Item not found"}





@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}   



#GET POSTS
from sqlalchemy.orm import Session

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    post = db.query(models.Posts).all()
    return post


#CREATE POST
@app.post("/create-post")
def create_post(post : schemas.PostCreate, db: Session = Depends(get_db)):
    # Convert Pydantic model to SQLAlchemy model
    db_post = models.Posts(**post.dict())

    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return post



#get post by id
@app.get("/posts/{id}")
def get_post(id: int,db : Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post :
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post



# update post
@app.put("/posts/{id}")
def update_post(id: int,post : schemas.PostUpdate,db : Session = Depends(get_db)):
    db_posts = db.query(models.posts).filter(models.Posts.id == id).first()
    if not db_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found") 
    db_posts.update(post.dict(exclude_unset=True))
    db.commit() 
    db.refresh(db_posts)
    return db_posts


# delete post
@app.delete("/posts/{id}")
def delete_post(id : int, db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}