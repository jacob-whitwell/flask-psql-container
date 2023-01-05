from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

# Here we execute our API calls against the PSQL database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {
        "message": "This is the API to create, read, update and delete users from out database. Please see below for the actions. For more information, please visit /docs to view the swagger ui.",
        "get/users/": "Lists all users in the database.",
        "get/user/{id}": "Lists a specific user based on their ID. Must supply {id}.",
        "put/user/{id}": "Updated a specific user. Must supply {id}, {firstname}, {lastname} parameters.",
        "post/create_user/": "Creates a user. Must supply {id}, {firstname}, {lastname} parameters.",
        "delete/user/{id}/": "Deletes a specific user. Must supply {id}."
        

    }

@app.post("post/create_user/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=409, detail="User already exists, pal.")
    return crud.create_user(db=db, user=user)

@app.get("/get/users/")
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/get/user/{id}", response_model=schemas.User)
async def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found, dummy.")
    return db_user

@app.put("/put/user_update/{id}")
async def update_user(id: int, firstname: str, lastname: str, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id=id, firstname=firstname, lastname=lastname)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found, dummy.")
    return {"status": 200}

@app.delete("/delete/user/{id}")
async def delete_user(id: int, db: Session=Depends(get_db)):
    db_user = crud.delete_user(db, user_id=id)
    if db_user is 0:
        raise HTTPException(status_code=404, detail="User isn't found, can't delete!")
    return {"status": 200}