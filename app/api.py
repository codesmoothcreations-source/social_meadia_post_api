from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from local_db import db

app = FastAPI()

class Post(BaseModel):
    id: int
    public_id: str
    title: str
    content: str
    image_url: str
    creatled_at: str
    updated_at: str


@app.get("/")
def root():
    return {"message": "Welcome to my social media app api!"}