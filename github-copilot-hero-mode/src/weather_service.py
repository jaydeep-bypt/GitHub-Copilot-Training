"""Weather Service with Caching.

This module orchestrates weather data retrieval with intelligent caching
to reduce API calls and improve performance.
"""

from .api_client import APIClient
from .cache_manager import CacheManager


class WeatherService:
    """Weather service with caching to reduce API calls."""

    def __init__(self, cache_ttl: int = 600):
        """Initialize weather service with API client and cache.
        
        Args:
            cache_ttl: Cache time-to-live in seconds (default: 600 = 10 minutes).
        """
        self.api = APIClient()
        self.cache = CacheManager(ttl=cache_ttl)
        self.cache_hits = 0
        self.cache_misses = 0

    def get_weather(self, city: str):
        """Return weather data using cache when available.
        
        This method first checks the cache for recent weather data.
        If found, returns cached data (cache hit). Otherwise, fetches
        fresh data from the API, caches it, and returns it (cache miss).
        
        Args:
            city: Name of the city to get weather for.
            
        Returns:
            dict: Weather data including current conditions.
            
        Raises:
            ValueError: If city name is invalid.
            requests.exceptions.RequestException: If API request fails.
        """
        if not city or not isinstance(city, str):
            raise ValueError("Invalid city name.")
        
        # Normalize city name for consistent cache keys
        cache_key = city.strip().lower()
        
        # Try to get from cache
        cached = self.cache.get(cache_key)
        if cached:
            self.cache_hits += 1
            return cached
        
        # Cache miss - fetch from API
        self.cache_misses += 1
        data = self.api.fetch_weather(city)
        
        # Store in cache
        self.cache.set(cache_key, data)
        
        return data

    def clear_cache(self) -> None:
        """Clear all cached weather data."""
        self.cache.clear()

    def get_cache_stats(self):
        """Get cache performance statistics.
        
        Returns:
            dict: Cache statistics including hits, misses, and hit rate.
        """
        total_requests = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            'cache_hits': self.cache_hits,
            'cache_misses': self.cache_misses,
            'total_requests': total_requests,
            'hit_rate_percent': round(hit_rate, 2),
            'cache_size': self.cache.size()
        }
