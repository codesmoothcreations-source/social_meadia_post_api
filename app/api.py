from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from datetime import datetime
# from local_db import db

app = FastAPI()

class Post(BaseModel):
    id: int
    public_id: str = f"pos_{id}"
    title: str
    content: str
    image_url: str = None
    creatled_at: str = datetime.utcnow().isoformat()
    updated_at: str = datetime.utcnow().isoformat()

my_posts = [
    {"id": 1, 
    "public_id": "abc123",
    "title": "First Post", 
    "content": "This is the content of the first post.", 
    "image_url": "https://example.com/image1.jpg", 
    "created_at": "2023-01-01T12:00:00Z", 
    "updated_at": "2023-01-01T12:00:00Z"},
    {"id": 2, 
    "public_id": "def456", 
    "title": "Second Post",
    "content": "This is the content of the second post.",
    "image_url": "https://example.com/image2.jpg",
    "created_at": "2023-01-02T12:00:00Z",
    "updated_at": "2023-01-02T12:00:00Z"}
]

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