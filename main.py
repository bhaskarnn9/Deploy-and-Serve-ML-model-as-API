import uvicorn
from fastapi import FastAPI, Body, Depends
from app.api_model import PostSchema, UserLoginSchema, UserSchema
from app.auth.jwt_handler import signed_jwt
from app.auth.jwt_bearer import jwtBearer

posts = [
    {
        "id": 1,
        "title": "penguins",
        "text": "penguins are a group of aquatic flightless birds"
    },
    {
        "id": 2,
        "title": "tigers",
        "text": "tigers are the largest cat species"
    },
    {
        "id": 3,
        "title": "koalas",
        "text": "koalas are the arboreal herbivorous marsupial native to Australia"
    }
]

users = []

app = FastAPI()


# 1 get - for testing
@app.get("/", tags=["test"])
def greet():
    return {"message": "Hello World"}


# 2 get - posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}


# 3 get - single post by id
@app.get("/posts/{_id}", tags=["posts"])
def get_post(_id: int):
    if _id > len(posts):
        return {"message": "Post nID doesn't exist"}
    for post in posts:
        if post["id"] == _id:
            return {"data": post}


# 4 post - blog post [A handler for creating a post]
@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.model_dump())
    return {"info": "post added successfully"}


# 5 user sign up
@app.post("/user/signup", tags=["users"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signed_jwt(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


@app.post("/user/login", tags=["users"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signed_jwt(user.email)
    else:
        return {"error": "Invalid credentials"}

