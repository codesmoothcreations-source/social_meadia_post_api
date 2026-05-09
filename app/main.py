from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
            {
            'id': 1, 
            'title': 'title for post one(1)', 
            'content': 'content for post one(1)'},
            {
            'id': 2,
            'title': 'Favorite food from Ghana',
            'content': 'Bnaku, Fufu, Tz ...'
            }
            ]

def find_post(id):
    try:
        id  = int(id)
    except ValueError:
        return f"Invalid id: {id}"
    for post in my_posts:
        if post["id"] == id:
            return post
        # return f"Id not found {id}"

def find_index(id):
    for i, p in enumerate(my_posts):
        if id == p["id"]:
            return i

# Get url base "root"
@app.get("/")
def root():
    return {"message": "Welcome to my social media app"}

# Get * posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# get create post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

# get post detail
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Post with id: {id} not found")
    return {"data": post}

# get post detail
@app.get("/posts/{id}")
def get_post(id: int, respose: Response):
    post = find_post(id)
    if not post:
        respose.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Post with id: {id} not found"}
    return {"data: post"}

# get post detail
@app.get("/posts/{id}")
def get_post(id):
        data = find_post(id)
        return {"message": data}

# Delet post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # index = None
    # for i, p in enumerate(my_posts):
    #     if p['id'] == id:
    #         index = i

    # if index == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                         detail= f"Post with id: {id} not found")
    # my_posts.pop(index)
    # Working code
    index = find_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"Post with id: {id} not found")
    my_posts.pop(index)

# update a post with the put method
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not found")
    
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data": post_dict}


# Keep off this one too "
# import json
# import os

# # Folder name
# folder_name = "DB"

# # Create folder if it doesn't exist
# os.makedirs(folder_name, exist_ok=True)

# # File path inside DB folder
# file_name = os.path.join(folder_name, "database.json")

# def save_db(register):

#     # Create file if it doesn't exist
#     if not os.path.exists(file_name):
#         with open(file_name, "w", encoding="utf8") as f:
#             json.dump([], f)

#     # Read existing data
#     with open(file_name, "r", encoding="utf8") as f:
#         try:
#             data = json.load(f)
#         except json.JSONDecodeError:
#             data = []

#     # Add new record
#     data.append(register)

#     # Save updated data
#     with open(file_name, "w", encoding="utf8") as f:
#         json.dump(data, f, indent=2)


# # Example
# save_db({
#     "name": "John",
#     "age": 25
# })
# "