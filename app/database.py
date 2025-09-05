from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from environs import Env


env = Env()
env.read_env()

DATABASE_URL = env('DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
