from flask import Flask, request, jsonify
from flasgger import Swagger  # Import Flasgger

app = Flask(__name__)
swagger = Swagger(app)  # Initialize Swagger

users = {}  # In-memory database

@app.route("/users", methods=["GET"])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
    """
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """
    Get a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Returns user details
      404:
        description: User not found
    """
    user = users.get(user_id)
    return jsonify(user) if user else ("User not found", 404)

@app.route("/users", methods=["POST"])
def create_user():
    """
    Create a new user
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Alice"
            email:
              type: string
              example: "alice@example.com"
    responses:
      201:
        description: User created successfully
    """
    data = request.json
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"id": user_id, "message": "User created"}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Update a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id] = data
    return jsonify({"id": user_id, "message": "User updated"})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Delete a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"id": user_id, "message": "User deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

try:
    print(response.json())
except Exception:
    print(response.text)