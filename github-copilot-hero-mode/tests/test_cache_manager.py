"""Unit tests for CacheManager.

This module tests the caching functionality including TTL, expiration,
and basic cache operations.
"""

import time
import pytest
from src.cache_manager import CacheManager


def test_cache_initialization():
    """Test cache manager initializes with correct TTL."""
    cache = CacheManager(ttl=300)
    assert cache.ttl == 300
    assert cache.size() == 0


def test_cache_initialization_default_ttl():
    """Test cache manager uses default TTL of 600 seconds."""
    cache = CacheManager()
    assert cache.ttl == 600


def test_cache_initialization_invalid_ttl():
    """Test cache manager rejects invalid TTL values."""
    with pytest.raises(ValueError, match="TTL must be positive"):
        CacheManager(ttl=0)
    
    with pytest.raises(ValueError, match="TTL must be positive"):
        CacheManager(ttl=-10)


def test_cache_set_and_get():
    """Test basic cache set and get operations."""
    cache = CacheManager(ttl=2)
    cache.set("test_key", "test_data")
    assert cache.get("test_key") == "test_data"


def test_cache_get_nonexistent_key():
    """Test getting a non-existent key returns None."""
    cache = CacheManager()
    assert cache.get("nonexistent") is None


def test_cache_expiry():
    """Test cache entries expire after TTL."""
    cache = CacheManager(ttl=1)
    cache.set("temp", "old_data")
    
    # Should be available immediately
    assert cache.get("temp") == "old_data"
    
    # Wait for expiry
    time.sleep(1.5)
    
    # Should be expired
    assert cache.get("temp") is None


def test_cache_multiple_entries():
    """Test cache can store multiple entries."""
    cache = CacheManager(ttl=10)
    cache.set("key1", "value1")
    cache.set("key2", "value2")
    cache.set("key3", "value3")
    
    assert cache.get("key1") == "value1"
    assert cache.get("key2") == "value2"
    assert cache.get("key3") == "value3"
    assert cache.size() == 3


def test_cache_overwrite():
    """Test cache overwrites existing keys."""
    cache = CacheManager(ttl=10)
    cache.set("key", "value1")
    cache.set("key", "value2")
    
    assert cache.get("key") == "value2"
    assert cache.size() == 1


def test_cache_clear():
    """Test cache clear removes all entries."""
    cache = CacheManager(ttl=10)
    cache.set("key1", "value1")
    cache.set("key2", "value2")
    
    assert cache.size() == 2
    
    cache.clear()
    
    assert cache.size() == 0
    assert cache.get("key1") is None
    assert cache.get("key2") is None


def test_cache_size():
    """Test cache size tracking."""
    cache = CacheManager(ttl=10)
    assert cache.size() == 0
    
    cache.set("key1", "value1")
    assert cache.size() == 1
    
    cache.set("key2", "value2")
    assert cache.size() == 2
    
    cache.clear()
    assert cache.size() == 0


def test_cache_remove_expired():
    """Test manual removal of expired entries."""
    cache = CacheManager(ttl=1)
    cache.set("key1", "value1")
    cache.set("key2", "value2")
    
    time.sleep(1.5)
    
    # Add a fresh entry
    cache.set("key3", "value3")
    
    # Should have 3 entries (expired ones not auto-removed until accessed)
    assert cache.size() == 3
    
    # Manually remove expired
    removed = cache.remove_expired()
    assert removed == 2
    assert cache.size() == 1
    assert cache.get("key3") == "value3"


def test_cache_different_data_types():
    """Test cache can store different data types."""
    cache = CacheManager(ttl=10)
    
    cache.set("string", "text")
    cache.set("number", 42)
    cache.set("list", [1, 2, 3])
    cache.set("dict", {"key": "value"})
    
    assert cache.get("string") == "text"
    assert cache.get("number") == 42
    assert cache.get("list") == [1, 2, 3]
    assert cache.get("dict") == {"key": "value"}


def test_cache_key_type_validation():
    """Test cache validates key types."""
    cache = CacheManager(ttl=10)
    
    with pytest.raises(TypeError, match="Cache key must be a string"):
        cache.set(123, "value")
    
    with pytest.raises(TypeError, match="Cache key must be a string"):
        cache.get(123)


def test_cache_expiry_boundary():
    """Test cache expiry at exact TTL boundary."""
    cache = CacheManager(ttl=1)
    cache.set("key", "value")
    
    # Just before expiry
    time.sleep(0.9)
    assert cache.get("key") == "value"
    
    # Just after expiry
    time.sleep(0.2)
    assert cache.get("key") is None
