from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from db import cursor, conn


app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None



@app.get('/posts')
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {'message': posts}


@app.get('/posts/{id}')
def get_post(id):
    cursor.execute("""SELECT * FROM posts WHERE id=%s""", (id))
    post = cursor.fetchone()
    return {'post': post}


@app.post('/posts')
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING *""", (post.title, post.content))
    post = cursor.fetchone()
    conn.commit()
    return {'message': post}