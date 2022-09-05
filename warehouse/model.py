from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, sql


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    item_name = Column(String(50))
    article = Column(Integer, unique=True)
    category = Column(String)
    description = Column(String(350))
    price = Column(Integer)
    amount = Column(Integer)
    created_on = Column(DateTime(timezone=True), server_default=sql.func.now())
    updated_on = Column(DateTime(timezone=True), server_default=sql.func.now(), onupdate=sql.func.now())


item = Item.__table__
