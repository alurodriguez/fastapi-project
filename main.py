from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None
    tags: List[str] = []

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
                "tags": ["rock", "metal", "bar"],
            }
        }


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get("/items/", tags=["items"])
async def read_items():
    return items


@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=["items"],
    summary="Create an item",
)
async def create_item(item_id: str, item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    item_encoded = jsonable_encoder(item)
    items[item_id] = item_encoded
    return item_encoded


@app.get("/items/{item_id}", response_model=Item, tags=["items"])
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item, tags=["items"])
async def update_item(item_id: str, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        update_item_encoded = jsonable_encoder(item)
        items[item_id] = update_item_encoded
        return update_item_encoded


@app.delete("/items/{item_id}", tags=["items"])
async def delete_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        del items[item_id]
        return {"message": "Item has been deleted succesfully"}
