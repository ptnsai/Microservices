from flask import Flask, jsonify, request
app = Flask(__name__)
# Sample in-memory data
showtimes = [
{"id": 1, "movie_id": 1, "start_time": "2025-05-10T18:00:00", "available_seats": 50}
]
@app.route('/showtimes', methods=['GET'])
def get_showtimes():
return jsonify(showtimes), 200
@app.route('/showtimes', methods=['POST'])
def add_showtime():
data = request.get_json()
showtimes.append(data)
return jsonify(data), 201
if __name__ == '__main__':
app.run(port=5003, debug=True)
