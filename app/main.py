from typing import Optional, List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
# from db import cursor, conn
from . import models
from app.db import engine, get_db
from sqlalchemy.orm import Session
from .schemas import PostCreate, PostResponse
 


models.Base.metadata.create_all(bind=engine)
app = FastAPI()






def validate_post(post):
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')



@app.get('/posts', response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@app.post('/posts', response_model=PostResponse)
def create_posts(post: PostCreate, db: Session = Depends(get_db)):
    posts_dict = post.model_dump()
    new_post = models.Post(**posts_dict)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get('/posts/{id}',  response_model=PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    validate_post(post)
    return post


@app.delete('/posts/{id}', response_model=PostResponse)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    validate_post(post.first())
    post.delete()
    db.commit()
    
    return post


@app.put('/posts/{id}', response_model=PostResponse)
def update_post(post: PostCreate, id: int, db: Session = Depends(get_db)):
    update_post_query = db.query(models.Post).filter(models.Post.id == id)
    update_post = update_post_query.first()
    validate_post(update_post)
    
    update_post_query.update(post.model_dump())
    db.commit()
    
    db.refresh(update_post)
    return update_post


# @app.get('/posts')
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#      return {'message': posts}


# @app.get('/posts/{id}')
# def get_post(id: int):
#     cursor.execute("""SELECT * FROM posts WHERE id=%s""", (str(id),))
#     post = cursor.fetchone()
#     validate_post(post)
#     return {'post': post}


# @app.post('/posts')
# def create_post(post: Post):
#     cursor.execute("""INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING *""", (post.title, post.content))
#     post = cursor.fetchone()
#     conn.commit()
#     return {'message': post}



# @app.delete('/posts/{id}')
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id=%s RETURNING *""", (str(id), ))
#     post = cursor.fetchone()
#     validate_post(post)
#     conn.commit()
#     return {'deleted post': post}


# @app.put('/posts/{id}')
# def update_post(post: Post, id: int):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s WHERE id = %s RETURNING *""", (post.title, post.content, id))   
#     post = cursor.fetchone()
#     validate_post(post)
#     conn.commit()
#     return {'updated_post': post}