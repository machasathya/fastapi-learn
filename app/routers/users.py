
from fastapi import Depends,HTTPException,status,APIRouter
from app import database,models,schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils import hash_password

router = APIRouter(tags=["users"])



#CREATE user
@router.post("/create-user", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    # Check if user already exists (assuming email is unique)
    existing_user = db.query(models.Users).filter(models.Users.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_password = hash_password(user.password)
    db_user = models.Users(**user.dict(exclude={"password"}), password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    user = db.query(models.Users).all()
    return user