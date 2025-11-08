"""API Client for Weather Service.

This module handles secure communication with external weather APIs.
"""

import os
import requests


class APIClient:
    """Handles secure communication with external weather API."""

    def __init__(self):
        """Initialize API client with secure configuration.
        
        The API key is retrieved from the WEATHER_API_KEY environment variable.
        Uses Open-Meteo API which provides free weather data.
        """
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def fetch_weather(self, city: str):
        """Fetch current weather data for a city.
        
        Args:
            city: Name of the city to fetch weather for.
            
        Returns:
            dict: Weather data from the API.
            
        Raises:
            ValueError: If city name is invalid.
            requests.exceptions.RequestException: If API request fails.
            requests.exceptions.Timeout: If request times out.
            requests.exceptions.HTTPError: If API returns error status.
        """
        if not city or not isinstance(city, str):
            raise ValueError("Invalid city name.")
        
        # Validate city is not empty after stripping whitespace
        if not city.strip():
            raise ValueError("City name cannot be empty.")
        
        # For demonstration, using fixed coordinates (Berlin)
        # In production, would use geocoding service to convert city to coordinates
        params = {
            "latitude": 52.52,
            "longitude": 13.405,
            "current_weather": True
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise requests.exceptions.Timeout("API request timed out after 5 seconds")
        except requests.exceptions.HTTPError as e:
            raise requests.exceptions.HTTPError(f"API returned error status: {e}")
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request failed: {e}")
