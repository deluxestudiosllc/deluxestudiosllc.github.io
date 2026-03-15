import json
from datetime import datetime

data = {
    "status": "SUCCESS",
    "time": datetime.now().isoformat(),
    "python": "working",
    "message": "✅ Python updated this file!"
}

with open("test.json", "w") as f:
    json.dump(data, f, indent=2)

print("Updated test.json")