from typing import Any, List

from app import crud, deps, models, schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=List[schemas.Item])
def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve items.
    """
    items = crud.item.get_multi_by_owner(
        db=db, owner_id=current_user.id, skip=skip, limit=limit
    )
    return items


@router.post("/", response_model=schemas.Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.ItemCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=current_user.id)
    return item


@router.put("/{item_id}", response_model=schemas.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
    item_in: schemas.ItemUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an item.
    """
    item = crud.item.get(db=db, id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{item_id}", response_model=schemas.Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    item = crud.item.get(db=db, id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", response_model=schemas.Item)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item = crud.item.get(db=db, id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.item.remove(db=db, id=item_id)
    return item
