from fastapi import Depends,HTTPException,status,APIRouter
from app import database,models,schemas,utils
from app.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(tags=["authentication"])


@router.post("/login")
def login(cred : schemas.LoginCred, db : Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == cred.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = " incorrect username or password")
    
    if not utils.verify_password(cred.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = " incorrect username or password")
    #token generation implementation
    return {"token": "new token"}