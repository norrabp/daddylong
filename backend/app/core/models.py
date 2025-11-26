import uuid

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func

from app.core.database import Base


class Model(Base):
    """Base model class with UUID id and timestamps"""

    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)

    @declared_attr
    def __tablename__(self):
        """Generate table name from class name"""
        return self.__name__.lower() + "s"


class SoftDeleteModel(Model):
    """Base model with soft delete functionality"""

    __abstract__ = True

    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)

    @property
    def is_deleted(self) -> bool:
        """Check if the record is soft deleted"""
        return self.deleted_at is not None

    def soft_delete(self):
        """Mark the record as deleted"""
        from sqlalchemy import func

        self.deleted_at = func.now()

    def restore(self):
        """Restore a soft deleted record"""
        self.deleted_at = None
