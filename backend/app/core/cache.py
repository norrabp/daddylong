import json
from functools import wraps
from typing import Any

from app.core.database import get_redis_cache


class CacheManager:
    """Redis cache manager for application caching"""

    def __init__(self):
        self.redis_client = get_redis_cache()

    def set(self, key: str, value: Any, expire: int = 3600) -> bool:
        """Set a key-value pair in cache with expiration"""
        try:
            if isinstance(value, dict | list):
                value = json.dumps(value)
            return self.redis_client.setex(key, expire, str(value))
        except Exception:
            return False

    def get(self, key: str) -> Any | None:
        """Get a value from cache"""
        try:
            value = self.redis_client.get(key)
            if value is None:
                return None

            # Try to parse as JSON, fallback to string
            try:
                return json.loads(value)
            except (json.JSONDecodeError, TypeError):
                return value
        except Exception:
            return None

    def delete(self, key: str) -> bool:
        """Delete a key from cache"""
        try:
            return bool(self.redis_client.delete(key))
        except Exception:
            return False

    def exists(self, key: str) -> bool:
        """Check if a key exists in cache"""
        try:
            return bool(self.redis_client.exists(key))
        except Exception:
            return False

    def clear_pattern(self, pattern: str) -> int:
        """Clear all keys matching a pattern"""
        try:
            keys = self.redis_client.keys(pattern)
            if keys:
                return self.redis_client.delete(*keys)
            return 0
        except Exception:
            return 0


# Global cache instance
cache = CacheManager()


def cached(expire: int = 3600, key_prefix: str = ""):
    """Decorator to cache function results"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key from function name and arguments
            args_str = str(args) + str(sorted(kwargs.items()))
            cache_key = f"{key_prefix}:{func.__name__}:{hash(args_str)}"

            # Try to get from cache
            cached_result = cache.get(cache_key)
            if cached_result is not None:
                return cached_result

            # Execute function and cache result
            result = func(*args, **kwargs)
            cache.set(cache_key, result, expire)
            return result

        return wrapper

    return decorator
