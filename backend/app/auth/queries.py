from sqlalchemy.orm import Session

from app.auth.models import User
from app.auth.schemas import UserCreate, UserUpdate
from app.core.security import get_password_hash


def get_user_by_email_query(db: Session, email: str) -> User | None:
    """Get user by email address"""
    return db.query(User).filter(User.email == email).first()


def get_user_by_id_query(db: Session, user_id: str) -> User | None:
    """Get user by ID"""
    return db.query(User).filter(User.id == user_id).first()


def get_users_query(
    db: Session, skip: int = 0, limit: int = 100, include_deleted: bool = False
) -> list[User]:
    """Get list of users with optional pagination"""
    query = db.query(User)
    if not include_deleted:
        query = query.filter(User.deleted_at.is_(None))
    return query.offset(skip).limit(limit).all()


def create_user_query(db: Session, user_in: UserCreate) -> User:
    """Create a new user"""
    user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        full_name=user_in.full_name,
        is_superuser=user_in.is_superuser,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user_query(db: Session, user: User, user_in: UserUpdate) -> User:
    """Update user information"""
    update_data = user_in.dict(exclude_unset=True)

    # Handle password update separately
    if "password" in update_data:
        hashed_password = get_password_hash(update_data.pop("password"))
        update_data["hashed_password"] = hashed_password

    for field, value in update_data.items():
        setattr(user, field, value)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user_query(db: Session, user: User) -> bool:
    """Soft delete a user"""
    user.soft_delete()
    db.add(user)
    db.commit()
    return True


def restore_user_query(db: Session, user: User) -> User:
    """Restore a soft deleted user"""
    user.restore()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_active_users_query(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """Get list of active users"""
    return (
        db.query(User)
        .filter(User.is_active.is_(True), User.deleted_at.is_(None))
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_superusers_query(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """Get list of superusers"""
    return (
        db.query(User)
        .filter(User.is_superuser.is_(True), User.deleted_at.is_(None))
        .offset(skip)
        .limit(limit)
        .all()
    )
