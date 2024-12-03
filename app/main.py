from fastapi import FastAPI
from app.database import Base, engine
from app.routers import blog, comments, users, auth

# Import models to register them with SQLAlchemy Base
from app import models

# Initialize FastAPI app
app = FastAPI()

# Automatically create database tables
Base.metadata.create_all(bind=engine)

# Include routers for modular endpoints
app.include_router(blog.router, prefix="/blogs", tags=["blogs"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
