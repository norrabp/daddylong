from uuid import UUID

from sqlalchemy.orm import Session

from app.auth.models import User
from app.item.models import Item
from app.item.schemas import ItemCreate, ItemUpdate


def get_item_by_id_query(db: Session, item_id: UUID) -> Item | None:
    """Get item by ID"""
    return db.query(Item).filter(Item.id == item_id).first()


def get_items_query(
    db: Session, skip: int = 0, limit: int = 100, include_deleted: bool = False
) -> list[Item]:
    """Get list of items with optional pagination"""
    query = db.query(Item)
    if not include_deleted:
        query = query.filter(Item.deleted_at.is_(None))
    return query.offset(skip).limit(limit).all()


def get_items_by_owner_query(
    db: Session, owner_id: UUID, skip: int = 0, limit: int = 100
) -> list[Item]:
    """Get items by owner ID"""
    return (
        db.query(Item)
        .filter(Item.owner_id == owner_id, Item.deleted_at.is_(None))
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_item_query(db: Session, item_in: ItemCreate, owner_id: UUID) -> Item:
    """Create a new item"""
    item = Item(**item_in.dict(), owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item_query(db: Session, item: Item, item_in: ItemUpdate) -> Item:
    """Update item information"""
    update_data = item_in.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(item, field, value)

    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete_item_query(db: Session, item: Item) -> bool:
    """Soft delete an item"""
    item.soft_delete()
    db.add(item)
    db.commit()
    return True


def restore_item_query(db: Session, item: Item) -> Item:
    """Restore a soft deleted item"""
    item.restore()
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_items_by_owner_with_pagination_query(
    db: Session, owner_id: UUID, skip: int = 0, limit: int = 100
) -> list[Item]:
    """Get items by owner with pagination"""
    return (
        db.query(Item)
        .filter(Item.owner_id == owner_id, Item.deleted_at.is_(None))
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_all_items_for_user_query(
    db: Session, user: User, skip: int = 0, limit: int = 100
) -> list[Item]:
    """Get all items for a user (including superuser access)"""
    if user.is_superuser:
        return get_items_query(db, skip=skip, limit=limit)
    else:
        return get_items_by_owner_query(db, user.id, skip=skip, limit=limit)
