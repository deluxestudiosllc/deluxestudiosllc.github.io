// static/script.js
async function loadDeals() {
    const container = document.getElementById('deals-container');

    try {
        container.innerHTML = `
            <div class="col-12 text-center">
                <div class="spinner-border text-primary"></div>
                <p>Loading deals from Python API...</p>
            </div>
        `;

        // Fetch from your Render app API
        const response = await fetch('/api/deals');
        const data = await response.json();

        // Update stats
        document.getElementById('deals-count').textContent = data.total;
        document.getElementById('update-time').textContent =
            new Date(data.timestamp).toLocaleTimeString();

        // Calculate average price
        if (data.deals.length > 0) {
            const avg = data.deals.reduce((sum, deal) => sum + deal.price, 0) / data.deals.length;
            document.getElementById('avg-price').textContent = `€${Math.round(avg)}`;
        }

        // Display deals
        if (data.deals.length === 0) {
            container.innerHTML = `
                <div class="col-12">
                    <div class="alert alert-warning">
                        No deals found at the moment. Check back soon!
                    </div>
                </div>
            `;
            return;
        }

        container.innerHTML = '';

        data.deals.forEach(deal => {
            const card = `
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <span class="badge bg-danger float-end">
                                Save €${deal.savings}
                            </span>
                            <h5 class="card-title">${deal.from} → ${deal.to}</h5>
                            <h2 class="text-primary">€${deal.price}</h2>
                            <p class="text-muted">
                                <s>Normal: €${deal.normalPrice}</s>
                            </p>
                            <p class="mb-1">✈️ ${deal.airline}</p>
                            <p class="mb-3">📅 ${deal.dates}</p>
                            <a href="${deal.link}" target="_blank" class="btn btn-primary w-100">
                                View Deal
                            </a>
                        </div>
                        <div class="card-footer text-muted">
                            Found: ${new Date(deal.found).toLocaleTimeString()}
                        </div>
                    </div>
                </div>
            `;
            container.innerHTML += card;
        });

    } catch (error) {
        console.error("Error loading deals:", error);
        container.innerHTML = `
            <div class="col-12">
                <div class="alert alert-danger">
                    <h5>⚠️ API Error</h5>
                    <p>${error.message}</p>
                    <p>Make sure your Render app is running.</p>
                </div>
            </div>
        `;
    }
}

// Auto-refresh every 30 seconds
setInterval(loadDeals, 30000);

// Load on page load
document.addEventListener('DOMContentLoaded', loadDeals);