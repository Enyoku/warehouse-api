from sqlalchemy.orm import Session
from fastapi import HTTPException, status

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


def update_item(id: int, request: ItemBase, db: Session):
    item = db.query(Item).filter(Item.id == id)

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")

    item.update({
        Item.item_name: request.item_name,
        Item.article: request.article,
        Item.category: request.category,
        Item.price: request.price,
        Item.description: request.description,
        Item.amount: request.amount
    })
    db.commit()
    return "updated"


def delete_item(id: int, db: Session):
    item = db.query(Item).filter(Item.id == id).first()

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")

    db.delete(item)
    db.commit()
    return "deleted"
