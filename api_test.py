# api_test.py - Creates a JSON file
import json
from datetime import datetime

def create_test_api():
    """Create a simple API response"""
    data = {
        "status": "success",
        "message": "Python API is working!",
        "timestamp": datetime.now().isoformat(),
        "developer": "BalkanFlightAI",
        "service": "Flight Deal Finder",
        "nextUpdate": "2 hours from now",
        "routesAvailable": ["PRN-IST", "TIA-LON", "PRN-ZRH"],
        "testData": [
            {"from": "PRN", "to": "IST", "price": 49},
            {"from": "TIA", "to": "LON", "price": 39}
        ]
    }
    
    # Save to JSON file
    with open("api-test.json", "w") as f:
        json.dump(data, f, indent=2)
    
    print("✅ Created api-test.json")
    print(json.dumps(data, indent=2))
    
    return data

if __name__ == "__main__":
    create_test_api()