"""Unit tests for APIClient.

This module tests the API client functionality including
error handling, validation, and network communication.
"""

import pytest
from unittest.mock import Mock, patch
import requests
from src.api_client import APIClient


def test_api_client_initialization():
    """Test API client initializes with correct configuration."""
    client = APIClient()
    assert client.base_url == "https://api.open-meteo.com/v1/forecast"


def test_api_client_invalid_city():
    """Test API client validates city input."""
    client = APIClient()
    
    with pytest.raises(ValueError, match="Invalid city name"):
        client.fetch_weather("")
    
    with pytest.raises(ValueError, match="Invalid city name"):
        client.fetch_weather(None)
    
    with pytest.raises(ValueError, match="Invalid city name"):
        client.fetch_weather(123)


def test_api_client_empty_city():
    """Test API client rejects empty city names."""
    client = APIClient()
    
    with pytest.raises(ValueError, match="City name cannot be empty"):
        client.fetch_weather("   ")


@patch('src.api_client.requests.get')
def test_api_client_successful_request(mock_get):
    """Test API client handles successful requests."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "current_weather": {
            "temperature": 20.5,
            "windspeed": 12.3
        }
    }
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response
    
    client = APIClient()
    result = client.fetch_weather("Berlin")
    
    assert result["current_weather"]["temperature"] == 20.5
    mock_get.assert_called_once()


@patch('src.api_client.requests.get')
def test_api_client_timeout(mock_get):
    """Test API client handles timeout errors."""
    mock_get.side_effect = requests.exceptions.Timeout("Connection timeout")
    
    client = APIClient()
    
    with pytest.raises(requests.exceptions.Timeout, match="API request timed out"):
        client.fetch_weather("Berlin")


@patch('src.api_client.requests.get')
def test_api_client_http_error(mock_get):
    """Test API client handles HTTP errors."""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mock_get.return_value = mock_response
    
    client = APIClient()
    
    with pytest.raises(requests.exceptions.HTTPError, match="API returned error status"):
        client.fetch_weather("Berlin")


@patch('src.api_client.requests.get')
def test_api_client_request_exception(mock_get):
    """Test API client handles general request exceptions."""
    mock_get.side_effect = requests.exceptions.RequestException("Network error")
    
    client = APIClient()
    
    with pytest.raises(requests.exceptions.RequestException, match="API request failed"):
        client.fetch_weather("Berlin")


@patch('src.api_client.requests.get')
def test_api_client_timeout_setting(mock_get):
    """Test API client uses correct timeout."""
    mock_response = Mock()
    mock_response.json.return_value = {}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response
    
    client = APIClient()
    client.fetch_weather("Berlin")
    
    # Verify timeout is set to 5 seconds
    call_args = mock_get.call_args
    assert call_args.kwargs['timeout'] == 5
