"""Cache Manager for Weather Service.

This module provides in-memory caching with TTL (Time-To-Live) functionality.
"""

import time
from typing import Any, Optional


class CacheManager:
    """In-memory cache with TTL (time-to-live)."""

    def __init__(self, ttl: int = 600):
        """Initialize cache manager with configurable TTL.
        
        Args:
            ttl: Time-to-live in seconds (default: 600 = 10 minutes).
        """
        if ttl <= 0:
            raise ValueError("TTL must be positive")
        self.ttl = ttl
        self.cache = {}

    def get(self, key: str) -> Optional[Any]:
        """Retrieve value from cache if not expired.
        
        Args:
            key: Cache key to retrieve.
            
        Returns:
            Cached value if found and not expired, None otherwise.
        """
        if not isinstance(key, str):
            raise TypeError("Cache key must be a string")
            
        entry = self.cache.get(key)
        if entry and time.time() - entry['timestamp'] < self.ttl:
            return entry['data']
        
        # Remove expired entry
        if entry:
            del self.cache[key]
        
        return None

    def set(self, key: str, value: Any) -> None:
        """Store value in cache with current timestamp.
        
        Args:
            key: Cache key to store under.
            value: Data to cache.
        """
        if not isinstance(key, str):
            raise TypeError("Cache key must be a string")
            
        self.cache[key] = {
            'data': value,
            'timestamp': time.time()
        }

    def clear(self) -> None:
        """Clear all cached entries."""
        self.cache.clear()

    def size(self) -> int:
        """Get number of entries in cache.
        
        Returns:
            Number of cached entries.
        """
        return len(self.cache)

    def remove_expired(self) -> int:
        """Remove all expired entries from cache.
        
        Returns:
            Number of entries removed.
        """
        current_time = time.time()
        expired_keys = [
            key for key, entry in self.cache.items()
            if current_time - entry['timestamp'] >= self.ttl
        ]
        
        for key in expired_keys:
            del self.cache[key]
        
        return len(expired_keys)
