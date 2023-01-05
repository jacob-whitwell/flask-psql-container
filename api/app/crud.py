from sqlalchemy.orm import Session
from . import models, schemas

# Here is where we set up the CRUD methods for main.py to use.

# Get user by their ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Create a user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(id=user.id, firstname=user.firstname, lastname=user.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Update a users first name, last name
def update_user(db: Session, user_id: int, firstname: str, lastname: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).update({"id": user_id, "firstname": firstname, "lastname": lastname})
    db.commit()
    return db_user

# Delete a user based on ID
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return db_user