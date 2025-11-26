from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Database
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Redis
redis_client = Redis.from_url(settings.REDIS_URL, decode_responses=True)

# Redis Cache
redis_cache_client = Redis.from_url(settings.REDIS_CACHE_URL, decode_responses=True)


def get_redis():
    """Dependency to get Redis client"""
    return redis_client


def get_redis_cache():
    """Dependency to get Redis cache client"""
    return redis_cache_client
