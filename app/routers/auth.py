from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Body, Optional,Depends, List
from ..database import get_db
from .. import schemas,models,utils


router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    ##verify user email
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Invalid credentials")
    

    ##verify user password
    if not utils.verify(user_credentials.password, user.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Invalid credentials")