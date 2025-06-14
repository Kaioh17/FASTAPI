from jose import JWTError, jwt
from datetime import datetime,timedelta
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from. import schemas, database, models
from sqlalchemy.orm import Session
from app.config import Settings

oauth2_scheme =OAuth2PasswordBearer(tokenUrl = 'login')

#SECERET_KEY
#Algorithm
#expiraition time of token

settings = Settings()
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

##verify user token 
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = str(payload.get("user_id"))

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    print(token_data)
    return token_data
def get_current_user(token: str = Depends(oauth2_scheme), db: Session =  Depends(database.get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials", 
                                          headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()
    print(user)
    return user