from sqlalchemy.orm import Session
from app import models, schemas

# CRUD operations for blog posts
def create_blog(db: Session, blog: schemas.BlogPostCreate, author_id: int):
    db_blog = models.BlogPost(**blog.dict(), author_id=author_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blog(db: Session, blog_id: int):
    return db.query(models.BlogPost).filter(models.BlogPost.id == blog_id).first()

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.BlogPost).offset(skip).limit(limit).all()

def delete_blog(db: Session, blog_id: int):
    db_blog = db.query(models.BlogPost).filter(models.BlogPost.id == blog_id).first()
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog

# CRUD operations for comments
def create_comment(db: Session, comment: schemas.CommentCreate, author_id: int, blog_post_id: int):
    db_comment = models.Comment(**comment.dict(), author_id=author_id, blog_post_id=blog_post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_by_blog(db: Session, blog_post_id: int):
    return db.query(models.Comment).filter(models.Comment.blog_post_id == blog_post_id).all()

# CRUD operations for users
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password  # Add hashing here (e.g., bcrypt)
    db_user = models.User(username=user.username, hashed_password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
