from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str | None = None
    description: str | None = None


class ItemCreate(ItemBase):
    title: str


class ItemUpdate(ItemBase):
    pass


class ItemInDBBase(ItemBase):
    id: UUID | None = None
    owner_id: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


class Item(ItemInDBBase):
    pass


class ItemInDB(ItemInDBBase):
    pass
