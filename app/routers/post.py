from .. import models, schemas, utils
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Body, Optional,Depends, List
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/posts",
    tags = ['Posts']
)


#get all the data in the table 
@router.get("/",response_model=List[schemas.Post])
def get_post(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()##fetchess all the data

    return posts


### CREATE posts
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.CreatePost, 
                 db: Session = Depends(get_db)):  
 
    new_post = models.Post(**post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post) ## returning query
    return new_post

####RETRIEVE post by id 
@router.get("/{id}", response_model= schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (id,))
    # post = cursor.fetchall()

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} was not found")
    
    
    return post

###DELETE
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # deleting post
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (id,))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} does not exist")
    
    post_query.delete(synchronize_session = False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

##Update posts with id
@router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def update_post(id: int, post: schemas.Updatepost, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post_update = post_query.first()

    if post_update == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} does not exist")

    post_query.update(post.dict(), synchronize_session = False)
    db.commit()
    return  post_query.first()