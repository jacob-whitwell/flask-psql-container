from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

while (True):
    attempts = 0
    try:
        engine = create_engine (SQLALCHEMY_DATABASE_URL)
        break
    except:
        time.sleep(2)
        attempts += 1
        if attempts >= 5:
            print("Cannot connect to the database!")
            break



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()