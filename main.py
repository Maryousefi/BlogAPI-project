from fastapi import FastAPI
from app.database import Base, engine
from app.routers import blog, comments, users, auth
from app import models

#initializing FastAPI app
app = FastAPI(
    title="Blog Platform API",
    description="A RESTful API for managing blog posts and comments with role-based access.",
    version="1.0.0",
    contact={
        "name": "Maryam Yousefi",
        "email": "maryamyousefi.info@gmail.com",
    },
)

#automatically create database tables
Base.metadata.create_all(bind=engine)

#include routers for modular endpoints
app.include_router(blog.router, prefix="/blogs", tags=["blogs"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["authentication"])

app = FastAPI(
    title="Blog Platform API",
    description="A RESTful API for managing blog posts and comments with role-based access.",
    version="1.0.0",
    contact={
        "name": "Maryam Yousefi",
        "email": "maryamyousefi.info@gmail.com",
    },
)
