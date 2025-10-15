from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_products():
    """Read products from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def read_csv_products():
    """Read products from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to integer and price to float
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except FileNotFoundError:
        return []

@app.route('/products')
def display_products():
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error="Wrong source. Use 'json' or 'csv'.")
    
    # Read data based on source
    if source == 'json':
        products = read_json_products()
    else:  # source == 'csv'
        products = read_csv_products()
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html',
                                     error="Product not found")
            products = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                 error="Invalid product ID")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
