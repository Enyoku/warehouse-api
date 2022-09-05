import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

SQL_ALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

database = databases.Database(SQL_ALCHEMY_DATABASE_URL)

Base = declarative_base()
