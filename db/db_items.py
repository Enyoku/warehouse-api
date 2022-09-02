from sqlalchemy.orm import Session

from warehouse.schemas import ItemBase
from warehouse.model import Item


def create_item(db: Session, request: ItemBase):
    new_item = Item(
        item_name=request.item_name,
        article=request.article,
        category=request.category,
        description=request.description,
        price=request.price,
        amount=request.amount
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_all_items(db: Session):
    return db.query(Item).all()

