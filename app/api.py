from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from datetime import datetime
from random import randrange
from typing import Optional
# from local_db import db

app = FastAPI()

class Post(BaseModel):
    id: int = randrange(0, 1000)
    public_id: str = f"pos_{id}"
    title: str
    content: str
    image_url: Optional[str] = f"https://example.com/image{id}.jpeg"
    creatled_at: str = datetime.utcnow().isoformat()
    updated_at: str = None

my_posts = [
    {
        "id": 1, 
        "public_id": "pos_123",
        "title": "First Post", 
        "content": "This is the content of the first post.", 
        "image_url": "https://example.com/image1.jpg", 
        "created_at": "2023-01-01T12:00:00Z", 
        "updated_at": "2023-01-01T12:00:00Z"
    },
    {
        "id": 2, 
        "public_id": "pos_456", 
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "image_url": "https://example.com/image2.jpg",
        "created_at": "2023-01-02T12:00:00Z",
        "updated_at": "2023-01-02T12:00:00Z"
    }
]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post 

def find_index(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to my social media app api!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    my_posts.append(post_dict)
    return {"mes": "Post created", "data": post}

@app.get("/posts/latest")
def latest_post():
    return {"data": my_posts[-1]}

@app.get("/posts/{id}")
def get_post(id: int):
    post_dict = find_post(id)

    if not post_dict:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail= f"post with the id: {id} not found")
    return {"data": post_dict}

@app.put("/posts/{id}")
def update_posts(id: int, post: Post):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Post id: {id} not found")
    post_dict = post.dict()
    post_dict["id"] = id
    post_dict['updated_at'] = datetime.utcnow().isoformat()
    my_posts[index] = post_dict
    return {"msg": "Update succesfully", "data": my_posts[index]}