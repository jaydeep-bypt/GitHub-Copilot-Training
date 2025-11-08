"""
Real-time Weather Check for Ahmedabad using Open-Meteo API
"""

import requests
import time


def fetch_real_weather(city, latitude, longitude):
    """Fetch real weather data from Open-Meteo API"""
    print(f"\n🌍 Fetching real-time weather for {city}...")
    print(f"📍 Coordinates: {latitude}°N, {longitude}°E")
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "temperature_unit": "celsius",
        "windspeed_unit": "kmh"
    }
    
    try:
        print("⏳ Connecting to API...")
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        
        data = response.json()
        print("✅ Successfully fetched weather data!")
        
        return data
    except requests.exceptions.Timeout:
        print("❌ Request timed out. API might be slow or unreachable.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Check your internet connection.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def display_weather(data, city):
    """Display weather data in a nice format"""
    if not data:
        print("\n❌ No weather data available.")
        return
    
    print("\n" + "=" * 60)
    print(f"🌦️  CURRENT WEATHER FOR {city.upper()}")
    print("=" * 60)
    
    current = data.get('current_weather', {})
    
    print(f"\n🌡️  Temperature: {current.get('temperature', 'N/A')}°C")
    print(f"💨 Wind Speed: {current.get('windspeed', 'N/A')} km/h")
    print(f"🧭 Wind Direction: {current.get('winddirection', 'N/A')}°")
    print(f"🕐 Time: {current.get('time', 'N/A')}")
    
    # Weather code interpretation
    weather_code = current.get('weathercode', 0)
    weather_desc = {
        0: "☀️  Clear sky",
        1: "🌤️  Mainly clear",
        2: "⛅ Partly cloudy",
        3: "☁️  Overcast",
        45: "🌫️  Foggy",
        48: "🌫️  Depositing rime fog",
        51: "🌦️  Light drizzle",
        61: "🌧️  Slight rain",
        63: "🌧️  Moderate rain",
        65: "🌧️  Heavy rain",
        80: "🌦️  Slight rain showers",
        95: "⛈️  Thunderstorm"
    }
    
    print(f"🌈 Condition: {weather_desc.get(weather_code, '🌤️  Unknown')}")
    
    print(f"\n📍 Location: {data.get('latitude', 'N/A')}°N, {data.get('longitude', 'N/A')}°E")
    print(f"🌏 Timezone: {data.get('timezone', 'N/A')}")
    
    print("\n" + "=" * 60)


def main():
    print("=" * 60)
    print("🌍 REAL-TIME WEATHER CHECK")
    print("=" * 60)
    
    # Cities to check
    cities = {
        "Ahmedabad, India": {"lat": 23.03, "lon": 72.58},
        "Mumbai, India": {"lat": 19.08, "lon": 72.88},
        "Delhi, India": {"lat": 28.61, "lon": 77.21},
    }
    
    print("\nAvailable cities:")
    for i, city in enumerate(cities.keys(), 1):
        print(f"  {i}. {city}")
    
    print("\n" + "-" * 60)
    
    # Fetch weather for Ahmedabad (default)
    city = "Ahmedabad, India"
    coords = cities[city]
    
    start_time = time.time()
    weather_data = fetch_real_weather(city, coords['lat'], coords['lon'])
    elapsed = time.time() - start_time
    
    if weather_data:
        display_weather(weather_data, city)
        print(f"⏱️  Response Time: {elapsed:.2f} seconds")
    else:
        print("\n" + "=" * 60)
        print("❌ UNABLE TO FETCH REAL-TIME WEATHER")
        print("=" * 60)
        print("\n💡 Possible reasons:")
        print("   • Network connectivity issues")
        print("   • API service temporarily down")
        print("   • Firewall blocking the request")
        print("   • DNS resolution problems")
        print("\n🔧 Troubleshooting:")
        print("   1. Check internet connection: ping google.com")
        print("   2. Try in browser: https://api.open-meteo.com/v1/forecast?latitude=23.03&longitude=72.58&current_weather=true")
        print("   3. Check proxy/VPN settings")
        print("   4. Try different network")
    
    print("\n✨ Demo script completed!")


if __name__ == "__main__":
    main()
