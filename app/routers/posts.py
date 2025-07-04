from fastapi import Depends,HTTPException,status,APIRouter
from app import database,models,schemas,oauth2
from app.database import get_db
from sqlalchemy.orm import Session,joinedload

router = APIRouter(tags=['posts'])

#GET POSTS

@router.get("/posts", response_model=list[schemas.PostOut])
def get_posts(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    posts = (
        db.query(models.Posts)
        .options(joinedload(models.Posts.owner))
        .filter(models.Posts.owner_id == current_user.id)  # Optional filter
        .all()
    )
    return posts

#CREATE POST
@router.post("/create-post")
def create_post(post : schemas.PostCreate, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Convert Pydantic model to SQLAlchemy model
    db_post = models.Posts(owner_id = current_user.id,**post.dict())
    print(current_user)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return post



#get post by id
@router.get("/posts/{id}",response_model=schemas.PostOut)
def get_post(id: int,db : Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post :
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post



# update post
@router.put("/posts/{id}")
def update_post(id: int,post : schemas.PostUpdate,db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    db_posts = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not db_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found") 
    if db_posts.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")
    post_data = post.model_dump(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_posts, key, value)
    db.commit() 
    db.refresh(db_posts)
    return db_posts


# delete post
@router.delete("/delete-posts/{id}")
def delete_post(id : int, db: Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}
