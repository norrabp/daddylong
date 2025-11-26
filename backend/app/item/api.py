from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.auth.models import User
from app.item.queries import (
    create_item_query,
    delete_item_query,
    get_all_items_for_user_query,
    get_item_by_id_query,
    update_item_query,
)
from app.item.schemas import Item as ItemSchema
from app.item.schemas import ItemCreate, ItemUpdate

router = APIRouter()


@router.get("/", response_model=list[ItemSchema])
def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve items.
    """
    items = get_all_items_for_user_query(db, current_user, skip=skip, limit=limit)
    return items


@router.post("/", response_model=ItemSchema)
def create_item_endpoint(
    *,
    db: Session = Depends(deps.get_db),
    item_in: ItemCreate,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    item = create_item_query(db, item_in, current_user.id)
    return item


@router.put("/{id}", response_model=ItemSchema)
def update_item_endpoint(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    item_in: ItemUpdate,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an item.
    """
    item = get_item_by_id_query(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = update_item_query(db, item, item_in)
    return item


@router.get("/{id}", response_model=ItemSchema)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    item = get_item_by_id_query(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


@router.delete("/{id}")
def delete_item_endpoint(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item = get_item_by_id_query(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    delete_item_query(db, item)
    return {"ok": True}
