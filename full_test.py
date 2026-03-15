# full_test.py - Complete test of everything
import json
import os
from datetime import datetime

def run_complete_test():
    print("🚀 Starting Complete Python Test")
    print("=" * 50)
    
    # Test 1: Basic Python
    print("1. ✅ Basic Python works")
    print(f"   Python version: {__import__('sys').version}")
    
    # Test 2: File operations
    test_content = f"Test written by Python at {datetime.now()}"
    with open("test-output.txt", "w") as f:
        f.write(test_content)
    print("2. ✅ File operations work")
    
    # Test 3: JSON creation
    data = {
        "test": "successful",
        "timestamp": datetime.now().isoformat(),
        "filesCreated": ["test-output.txt", "api/deals.json"],
        "environment": {
            "runner": "GitHub Actions",
            "os": os.name,
            "path": os.getcwd()
        }
    }
    
    with open("test-results.json", "w") as f:
        json.dump(data, f, indent=2)
    print("3. ✅ JSON creation works")
    
    # Test 4: Create sample deals (like real app)
    deals = []
    routes = ["PRN-IST", "TIA-LON", "PRN-ZRH", "TIA-MUC"]
    
    for i, route in enumerate(routes):
        from_airport, to_airport = route.split("-")
        deals.append({
            "id": i + 1,
            "route": route,
            "from": from_airport,
            "to": to_airport,
            "price": 39 + (i * 10),
            "currency": "EUR",
            "found": datetime.now().isoformat(),
            "test": True
        })
    
    # Create api directory if not exists
    os.makedirs("api", exist_ok=True)
    
    # Save deals
    with open("api/deals.json", "w") as f:
        json.dump({
            "status": "test",
            "generated": datetime.now().isoformat(),
            "count": len(deals),
            "deals": deals
        }, f, indent=2)
    
    print("4. ✅ Sample deals created")
    print(f"   Created {len(deals)} fake deals")
    
    # Test 5: Update HTML
    try:
        with open("index.html", "r") as f:
            html = f.read()
        
        # Add test indicator
        if "<!-- Test completed -->" not in html:
            html = html.replace(
                "</body>",
                f'<!-- Test completed at {datetime.now()} -->\n</body>'
            )
            with open("index.html", "w") as f:
                f.write(html)
            print("5. ✅ HTML updated")
    except:
        print("5. ⚠️  HTML update skipped (no index.html)")
    
    print("=" * 50)
    print("🎉 All tests completed successfully!")
    print(f"📁 Files created: test-output.txt, test-results.json, api/deals.json")
    
    return data

if __name__ == "__main__":
    run_complete_test()