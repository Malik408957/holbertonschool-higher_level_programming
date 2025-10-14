from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with empty users dictionary for testing
users = {}

@app.route('/')
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Return list of all usernames"""
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def get_status():
    """API status endpoint"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Get user by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add new user via POST request"""
    try:
        # Parse JSON data from request
        data = request.get_json()
        
        # Check if request contains valid JSON
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400
        
        # Check if username is provided
        if 'username' not in data:
            return jsonify({"error": "Username is required"}), 400
        
        username = data['username']
        
        # Check if username already exists
        if username in users:
            return jsonify({"error": "Username already exists"}), 409
        
        # Create new user object
        new_user = {
            "username": username,
            "name": data.get('name', ''),
            "age": data.get('age', ''),
            "city": data.get('city', '')
        }
        
        # Add user to dictionary
        users[username] = new_user
        
        # Return success response
        return jsonify({
            "message": "User added",
            "user": new_user
        }), 201
        
    except Exception as e:
        return jsonify({"error": "Invalid JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
