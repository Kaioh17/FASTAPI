from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body, Optional,Depends, List
from pydantic import BaseModel

from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas,utils
from .database import engine,get_db
from sqlalchemy.orm import Session
from .routers import post, user

models.Base.metadata.create_all(bind = engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)






    