from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Body, Optional,Depends, List
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db
from .. import schemas,models,utils,oauth2


router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
##with oauth2passwordrequestform it expects the login request to use form-data content type instead of raw JSON 
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): 

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    ##verify user email
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Invalid credentials")
    

    ##verify user password
    if not utils.verify(user_credentials.password, user.password):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Invalid credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    # creat atoken and return token
    return {"access_token":access_token, "token_type": 'bearer'}