from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {}

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# POST new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"message": "User added", "user_id": user_id}), 201

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)
