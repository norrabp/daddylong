from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.core.models import SoftDeleteModel


class User(SoftDeleteModel):
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # Relationship
    items = relationship("Item", back_populates="owner")
