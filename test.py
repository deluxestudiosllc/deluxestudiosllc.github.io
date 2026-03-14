with open("test.json", "w") as f:
    f.write('{"status": "success", "time": "' + __import__('datetime').datetime.now().isoformat() + '"}')
print("Created test.json")