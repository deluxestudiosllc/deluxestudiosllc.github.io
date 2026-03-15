# update_website.py - Updates HTML dynamically
from datetime import datetime
import json

def update_index_html():
    """Update website with current time"""
    
    # Read current index.html
    with open("index.html", "r") as f:
        html = f.read()
    
    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Simple update: Add/update a div with timestamp
    if "Last Python Update:" in html:
        # Replace existing timestamp
        import re
        html = re.sub(
            r'Last Python Update:.*?</div>',
            f'Last Python Update: {timestamp}</div>',
            html
        )
    else:
        # Add timestamp before closing body
        insert_html = f'''
        <!-- Auto-updated by Python -->
        <div style="position:fixed;bottom:10px;right:10px;background:#0d6efd;color:white;padding:5px 10px;border-radius:5px;font-size:12px;">
            Last Python Update: {timestamp}
        </div>
        '''
        html = html.replace('</body>', insert_html + '\n</body>')
    
    # Write back
    with open("index.html", "w") as f:
        f.write(html)
    
    print(f"✅ Updated index.html at {timestamp}")
    
    # Also create a status JSON
    status = {
        "updated": True,
        "timestamp": timestamp,
        "file": "index.html",
        "action": "auto-update"
    }
    
    with open("status.json", "w") as f:
        json.dump(status, f, indent=2)
    
    return status

if __name__ == "__main__":
    update_index_html()