from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database

router = APIRouter()

@router.post("/blog/", response_model=schemas.BlogPost)
def create_blog(blog: schemas.BlogPostCreate, db: Session = Depends(database.get_db)):
    db_blog = models.BlogPost(**blog.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog
