# secrets_manager.py (After Fix)
import os

def get_api_key():
    # ✅ Secure: environment variable, no hard-coded secrets
    return os.getenv("API_KEY", "default_placeholder")
