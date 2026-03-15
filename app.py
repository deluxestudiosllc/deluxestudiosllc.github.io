from flask import Flask, render_template, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Store deals in memory (for demo)
# In production, use a database
flight_deals = []

@app.route('/')
def home():
    """Main website page"""
    return render_template('index.html')

@app.route('/api/deals')
def get_deals():
    """API endpoint for flight deals"""
    deals = [
        {
            "id": 1,
            "from": "PRN",
            "to": "IST",
            "price": 49,
            "normalPrice": 120,
            "airline": "Wizz Air",
            "dates": "Various",
            "link": "https://wizzair.com",
            "found": datetime.now().isoformat(),
            "savings": 71
        },
        {
            "id": 2,
            "from": "TIA", 
            "to": "LON",
            "price": 39,
            "normalPrice": 110,
            "airline": "Ryanair",
            "dates": "Apr 15-30",
            "link": "https://ryanair.com",
            "found": datetime.now().isoformat(),
            "savings": 71
        }
    ]
    
    return jsonify({
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "deals": deals,
        "total": len(deals),
        "message": "BalkanFlightAI - Cheapest flights Kosovo/Albania"
    })

@app.route('/api/update', methods=['POST'])
def update_deals():
    """Endpoint to trigger deal scraping (protected)"""
    # You can add authentication here
    # For now, just update with sample data
    global flight_deals
    
    # Simulate scraping
    new_deals = [
        {
            "id": len(flight_deals) + 1,
            "from": "PRN",
            "to": "ZRH",
            "price": 59,
            "normalPrice": 180,
            "airline": "Eurowings",
            "dates": "May 1-15",
            "found": datetime.now().isoformat()
        }
    ]
    
    flight_deals.extend(new_deals)
    
    return jsonify({
        "status": "updated",
        "added": len(new_deals),
        "total": len(flight_deals),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "BalkanFlightAI",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)