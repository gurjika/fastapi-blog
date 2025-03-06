from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from db import cursor


app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None

    

@app.get('/')
async def root():
    cursor.execute('SELECT * FROM posts')
    print(cursor.fetchall())
    return {'message': 'hello world'}


@app.get('/posts')
def get_posts():
    return {'data': 'Post'}


@app.post('/posts')
def create_post(post: Post):
    return {'message': post}