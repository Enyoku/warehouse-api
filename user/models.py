from sqlalchemy import Column, Integer, String, DateTime, sql

from db.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String(25), unique=True)
    password = Column(String)
    full_name = Column(String(50))
    email = Column(String)
    position = Column(String)
    created_on = Column(DateTime(timezone=True), server_default=sql.func.now())
