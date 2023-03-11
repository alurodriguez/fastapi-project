from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class ItemCreate(ItemBase):
    title: str


class ItemUpdate(ItemBase):
    pass


class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


class Item(ItemInDBBase):
    pass


class ItemInDB(ItemInDBBase):
    pass
