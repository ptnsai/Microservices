from flask import Flask, jsonify, request
app = Flask(__name__)
# Sample in-memory data
users = [
{"id": 1, "name": "Alice Sharma", "email": "alice@example.com"},
{"id": 2, "name": "Rahul Mehta", "email": "rahul@example.com"}
]
@app.route('/users', methods=['GET'])
def get_users():
return jsonify(users), 200
@app.route('/users', methods=['POST'])
def add_user():
data = request.get_json()
users.append(data)
return jsonify(data), 201
if __name__ == '__main__':
app.run(port=5004, debug=True)
