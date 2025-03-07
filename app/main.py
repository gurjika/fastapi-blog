from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
# from db import cursor, conn
from . import models
from db import engine, get_db
from sqlalchemy.orm import Session




models.Base.metadata.create_all(bind=engine)
app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None



def validate_post(post):
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')

@app.get('/posts')
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {'message': posts}





# @app.get('/posts')
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return {'message': posts}


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