from typing import List

from app import crud, deps
from app.schemas.item import Item, ItemCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/users/{user_id}/items/", response_model=Item)
def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(deps.get_db)
):
    return crud.item.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    items = crud.item.get_items(db, skip=skip, limit=limit)
    return items
