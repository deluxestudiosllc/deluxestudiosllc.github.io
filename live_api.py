# live_api.py - Creates an API endpoint via static JSON
import json
from datetime import datetime
import pytz  # Install: pip install pytz

def create_live_endpoint():
    """Create a 'live' API endpoint (static file)"""
    
    # Get time in Balkan timezones
    albania_tz = pytz.timezone('Europe/Tirane')
    kosovo_tz = pytz.timezone('Europe/Belgrade')  # Same timezone
    
    now_utc = datetime.now(pytz.utc)
    now_albania = now_utc.astimezone(albania_tz)
    now_kosovo = now_utc.astimezone(kosovo_tz)
    
    api_response = {
        "api": "BalkanFlightAI Test API",
        "status": "online",
        "serverTimeUTC": now_utc.isoformat(),
        "localTimes": {
            "Albania": {
                "time": now_albania.strftime("%H:%M:%S"),
                "date": now_albania.strftime("%Y-%m-%d"),
                "timezone": "Europe/Tirane"
            },
            "Kosovo": {
                "time": now_kosovo.strftime("%H:%M:%S"),
                "date": now_kosovo.strftime("%Y-%m-%d"),
                "timezone": "Europe/Belgrade"
            }
        },
        "message": "Python is working! This updates every minute.",
        "endpoints": {
            "deals": "/deals.json",
            "status": "/status.json",
            "test": "/api-test.json"
        },
        "nextUpdateIn": "60 seconds",
        "visitorCount": 1  # You can increment this
    }
    
    # Save as JSON file
    with open("api/live.json", "w") as f:
        json.dump(api_response, f, indent=2, ensure_ascii=False)
    
    print("🌍 Created live API endpoint:")
    print(json.dumps(api_response, indent=2))
    
    return api_response

if __name__ == "__main__":
    create_live_endpoint()