"""Unit tests for WeatherService.

This module tests the weather service including caching behavior,
API integration, and error handling.
"""

import pytest
from unittest.mock import Mock, patch
from src.weather_service import WeatherService
from src.api_client import APIClient


def test_weather_service_initialization():
    """Test weather service initializes correctly."""
    service = WeatherService()
    assert service.cache.ttl == 600
    assert service.cache_hits == 0
    assert service.cache_misses == 0


def test_weather_service_custom_ttl():
    """Test weather service accepts custom cache TTL."""
    service = WeatherService(cache_ttl=300)
    assert service.cache.ttl == 300


def test_weather_service_fetch_from_api(monkeypatch):
    """Test weather service fetches from API on cache miss."""
    service = WeatherService()
    
    mock_data = {"current_weather": {"temperature": 20, "windspeed": 10}}
    monkeypatch.setattr(service.api, "fetch_weather", lambda city: mock_data)
    
    result = service.get_weather("Berlin")
    
    assert result == mock_data
    assert service.cache_misses == 1
    assert service.cache_hits == 0


def test_weather_service_cache_hit(monkeypatch):
    """Test weather service returns cached data on subsequent requests."""
    service = WeatherService()
    
    mock_data = {"current_weather": {"temperature": 20}}
    monkeypatch.setattr(service.api, "fetch_weather", lambda city: mock_data)
    
    # First call - cache miss
    result1 = service.get_weather("Berlin")
    assert service.cache_misses == 1
    assert service.cache_hits == 0
    
    # Second call - cache hit
    result2 = service.get_weather("Berlin")
    assert result2 == result1
    assert service.cache_misses == 1
    assert service.cache_hits == 1


def test_weather_service_invalid_city():
    """Test weather service validates city input."""
    service = WeatherService()
    
    with pytest.raises(ValueError, match="Invalid city name"):
        service.get_weather("")
    
    with pytest.raises(ValueError, match="Invalid city name"):
        service.get_weather(None)
    
    with pytest.raises(ValueError, match="Invalid city name"):
        service.get_weather(123)


def test_weather_service_cache_key_normalization(monkeypatch):
    """Test weather service normalizes cache keys."""
    service = WeatherService()
    
    mock_data = {"current_weather": {"temperature": 20}}
    call_count = 0
    
    def mock_fetch(city):
        nonlocal call_count
        call_count += 1
        return mock_data
    
    monkeypatch.setattr(service.api, "fetch_weather", mock_fetch)
    
    # Different casing should use same cache
    service.get_weather("Berlin")
    service.get_weather("berlin")
    service.get_weather("BERLIN")
    service.get_weather(" Berlin ")
    
    # Should only call API once
    assert call_count == 1
    assert service.cache_hits == 3
    assert service.cache_misses == 1


def test_weather_service_clear_cache(monkeypatch):
    """Test weather service can clear cache."""
    service = WeatherService()
    
    mock_data = {"current_weather": {"temperature": 20}}
    monkeypatch.setattr(service.api, "fetch_weather", lambda city: mock_data)
    
    # Cache some data
    service.get_weather("Berlin")
    assert service.cache.size() == 1
    
    # Clear cache
    service.clear_cache()
    assert service.cache.size() == 0
    
    # Next call should be cache miss
    service.get_weather("Berlin")
    assert service.cache_misses == 2


def test_weather_service_get_cache_stats(monkeypatch):
    """Test weather service provides cache statistics."""
    service = WeatherService()
    
    mock_data = {"current_weather": {"temperature": 20}}
    monkeypatch.setattr(service.api, "fetch_weather", lambda city: mock_data)
    
    # Make some requests
    service.get_weather("Berlin")  # miss
    service.get_weather("Berlin")  # hit
    service.get_weather("Berlin")  # hit
    service.get_weather("London")  # miss
    
    stats = service.get_cache_stats()
    
    assert stats['cache_hits'] == 2
    assert stats['cache_misses'] == 2
    assert stats['total_requests'] == 4
    assert stats['hit_rate_percent'] == 50.0
    assert stats['cache_size'] == 2


def test_weather_service_no_requests_stats():
    """Test cache stats with no requests."""
    service = WeatherService()
    stats = service.get_cache_stats()
    
    assert stats['cache_hits'] == 0
    assert stats['cache_misses'] == 0
    assert stats['total_requests'] == 0
    assert stats['hit_rate_percent'] == 0
    assert stats['cache_size'] == 0


def test_weather_service_api_error_propagation(monkeypatch):
    """Test weather service propagates API errors."""
    service = WeatherService()
    
    def mock_fetch_error(city):
        raise Exception("API Error")
    
    monkeypatch.setattr(service.api, "fetch_weather", mock_fetch_error)
    
    with pytest.raises(Exception, match="API Error"):
        service.get_weather("Berlin")


def test_weather_service_multiple_cities(monkeypatch):
    """Test weather service caches multiple cities independently."""
    service = WeatherService()
    
    city_data = {
        "Berlin": {"temp": 20},
        "London": {"temp": 15},
        "Paris": {"temp": 18}
    }
    
    def mock_fetch(city):
        return city_data.get(city.strip().lower().title(), {})
    
    monkeypatch.setattr(service.api, "fetch_weather", mock_fetch)
    
    # Fetch different cities
    berlin = service.get_weather("Berlin")
    london = service.get_weather("London")
    paris = service.get_weather("Paris")
    
    assert berlin == {"temp": 20}
    assert london == {"temp": 15}
    assert paris == {"temp": 18}
    
    # All should be cache misses
    assert service.cache_misses == 3
    assert service.cache.size() == 3


@patch('src.api_client.requests.get')
def test_weather_service_integration(mock_get):
    """Test weather service with mocked API client."""
    # Mock API response
    mock_response = Mock()
    mock_response.json.return_value = {
        "current_weather": {
            "temperature": 20.5,
            "windspeed": 12.3,
            "time": "2025-11-08T12:00"
        }
    }
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response
    
    service = WeatherService()
    result = service.get_weather("Berlin")
    
    assert result["current_weather"]["temperature"] == 20.5
    assert mock_get.call_count == 1
    
    # Second call should use cache
    result2 = service.get_weather("Berlin")
    assert result2 == result
    assert mock_get.call_count == 1  # Still 1, not called again
