from fastapi import FastAPI
from app import database,models
from .routers import users,posts,auth
app = FastAPI()


# pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")
models.Base.metadata.create_all(bind=database.engine)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
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


#------------------------Database Connection-----------------------
#GET POSTS


# @app.get("/posts",response_model=list[schemas.PostOut])
# def get_posts(db: Session = Depends(get_db)):
#     post = db.query(models.Posts).all()
#     return post


# #CREATE POST
# @app.post("/create-post")
# def create_post(post : schemas.PostCreate, db: Session = Depends(get_db)):
#     # Convert Pydantic model to SQLAlchemy model
#     db_post = models.Posts(**post.dict())

#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)
#     return post



# #get post by id
# @app.get("/posts/{id}",response_model=schemas.PostOut)
# def get_post(id: int,db : Session = Depends(get_db)):
#     post = db.query(models.Posts).filter(models.Posts.id == id).first()
#     if not post :
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
#     return post



# # update post
# @app.put("/posts/{id}")
# def update_post(id: int,post : schemas.PostUpdate,db : Session = Depends(get_db)):
#     db_posts = db.query(models.Posts).filter(models.Posts.id == id).first()
#     if not db_posts:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found") 
#     post_data = post.model_dump(exclude_unset=True)
#     for key, value in post_data.items():
#         setattr(db_posts, key, value)
#     db.commit() 
#     db.refresh(db_posts)
#     return db_posts


# # delete post
# @app.delete("/posts/{id}")
# def delete_post(id : int, db: Session = Depends(get_db)):
#     post = db.query(models.Posts).filter(models.Posts.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
#     db.delete(post)
#     db.commit()
#     return {"message": "Post deleted successfully"}



# def hash_password(password : str):
#     hashed_password = pwd_context.hash(password)
#     return hashed_password


# #CREATE user
# @app.post("/create-user", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
# def create_user(user: schemas.User, db: Session = Depends(get_db)):
#     # Check if user already exists (assuming email is unique)
#     existing_user = db.query(models.Users).filter(models.Users.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
#     hashed_password = hash_password(user.password)
#     db_user = models.Users(**user.dict(exclude={"password"}), password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @app.get("/users")
# def get_users(db: Session = Depends(get_db)):
#     user = db.query(models.Users).all()
#     return user
 