from fastapi import Depends,HTTPException,status,APIRouter
from app import database,models,schemas,utils,oauth2
from app.database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


router = APIRouter(tags=["authentication"])


@router.post("/login",response_model=schemas.Token)
def login(cred : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
# def login(cred : schemas.LoginCred, db : Session = Depends(get_db)):

    user = db.query(models.Users).filter(models.Users.email == cred.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = " incorrect username or password")
    
    if not utils.verify_password(cred.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = " incorrect username or password")
    #token generation implementation
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}