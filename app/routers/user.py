from .. import models, schemas, utils
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Body, Optional,Depends, List
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/users",
    tags = ['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.UserOut)
def create_user(user: schemas.CreateUser,
                 db: Session =  Depends(get_db)):
    
    #hash pwd
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    user_query = models.User(**user.dict())

    db.add(user_query)
    db.commit()
    db.refresh(user_query)
    

    # return {"status" : "User created"}
    return user_query

@router.get("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model = schemas.UserOut)
def get_user_id(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} not found")

    return user
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()



    return users