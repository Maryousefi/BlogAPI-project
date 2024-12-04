from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, database
from app.auth_utils import get_current_user  

router = APIRouter()

@router.post("/", response_model=schemas.Comment)
def create_comment(
    comment: schemas.CommentCreate,
    blog_post_id: int,
    db: Session = Depends(database.get_db),
    current_user=Depends(get_current_user)  
):
    return crud.create_comment(db, comment, author_id=current_user["id"], blog_post_id=blog_post_id)

@router.get("/{blog_post_id}", response_model=List[schemas.Comment])
def read_comments(blog_post_id: int, db: Session = Depends(database.get_db)):
    return crud.get_comments_by_blog(db, blog_post_id=blog_post_id)
