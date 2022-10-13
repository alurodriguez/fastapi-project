from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def create_user_item(
        self, db: Session, *, obj_in: ItemCreate, user_id: int
    ) -> Item:
        db_obj = Item(
            title=obj_in.title,
            description=obj_in.description,
            owner_id=user_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


item = CRUDItem(Item)
