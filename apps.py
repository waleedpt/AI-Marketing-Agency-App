from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

SERVICES_DB = [
    {"id": 1, "title": "HVAC Installation & Repair", "provider": "Master Technicians Network", "commission_rate": "15%"},
    {"id": 2, "title": "Residential Electrical Wiring", "provider": "Local Expert Electricians", "commission_rate": "10%"}
]

PRODUCTS_DB = [
    {"id": 1, "title": "Smart Automatic Anti-Barking Dog Trainer", "owner": "Local Pet Store Hub", "price": 18.40, "commission": 3.00},
    {"id": 2, "title": "G1 Garlic Seeds (Premium Quality)", "owner": "Swabi Agri Farms", "price": 25.00, "commission": 4.50}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Commission Brokerage Agency</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f9; margin: 0; padding: 20px; color: #333; }
        .container { max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        h1 { color: #007bff; text-align: center; }
        .section { margin-top: 30px; padding: 20px; background: #fafafa; border-radius: 8px; border: 1px solid #e1e4e8; }
        h2 { font-size: 20px; color: #444; border-bottom: 2px solid #007bff; padding-bottom: 5px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px; }
        .card { background: white; padding: 15px; border-radius: 6px; border: 1px solid #ddd; }
        button { background: #28a745; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; margin-top: 10px; width: 100%; font-weight: bold; }
        button:hover { background: #218838; }
        input, select { width: 100%; padding: 8px; margin-top: 5px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌍 AI Global Commission & Service Agency</h1>
        <p style="text-align: center; color: #666;">Shariah-Compliant Brokerage for Technical Services & Local Products</p>

        <div class="section">
            <h2>🛠️ Technical & HVAC Services (Commission Model)</h2>
            <div class="grid">
                {% for service in services %}
                <div class="card">
                    <h3>{{ service.title }}</h3>
                    <p><b>Provider:</b> {{ service.provider }}</p>
                    <p><b>Our Commission:</b> {{ service.commission_rate }}</p>
                    <form action="/book-service" method="POST">
                        <input type="hidden" name="service_id" value="{{ service.id }}">
                        <input type="text" name="customer_name" placeholder="Your Name" required>
                        <input type="text" name="customer_phone" placeholder="WhatsApp / Phone Number" required>
                        <button type="submit">Book Service & Lock Commission</button>
                    </form>
                </div>
                {% endfor %}
            </div>
        </div>

        <div class="section">
            <h2>📦 Local Products Marketplace (Reselling Brokerage)</h2>
            <div class="grid">
                {% for product in products %}
                <div class="card">
                    <h3>{{ product.title }}</h3>
                    <p><b>Owner:</b> {{ product.owner }}</p>
                    <p><b>Price:</b> ${{ product.price }} (Your Commission: ${{ product.commission }})</p>
                    <form action="/buy-product" method="POST">
                        <input type="hidden" name="product_id" value="{{ product.id }}">
                        <input type="text" name="buyer_name" placeholder="Buyer Name" required>
                        <input type="text" name="buyer_address" placeholder="Delivery Address / City" required>
                        <button type="submit" style="background: #007bff;">Order via UBL Gateway</button>
                    </form>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, services=SERVICES_DB, products=PRODUCTS_DB)

@app.route("/book-service", methods=["POST"])
def book_service():
    name = request.form.get("customer_name")
    return f"""
    <div style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h2 style="color: green;">✅ Service Booked Successfully!</h2>
        <p>Thank you <b>{name}</b>. Our technical partner has been notified.</p>
        <br><a href="/" style="padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Back to Home</a>
    </div>
    """

@app.route("/buy-product", methods=["POST"])
def buy_product():
    buyer_name = request.form.get("buyer_name")
    return f"""
    <div style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h2 style="color: #007bff;">💳 UBL Payment & Order Gateway</h2>
        <p>Buyer: <b>{buyer_name}</b></p>
        <p style="font-size: 18px; color: green;">UBL Account: <b>PK36UNIL0109000234567801</b></p>
        <br><a href="/" style="padding: 10px 20px; background: #333; color: white; text-decoration: none; border-radius: 5px;">Back to Home</a>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
