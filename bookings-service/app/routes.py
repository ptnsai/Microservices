# BookingService
Handles tickets booking.
from flask import Flask, jsonify, request
app = Flask(__name__)
# Sample in-memory data
bookings = [
{"id": 1, "user_id": 1, "movie_id": 2, "showtime_id": 1, "seats": 2}
]
@app.route('/bookings', methods=['GET'])
def get_bookings():
return jsonify(bookings), 200
@app.route('/bookings', methods=['POST'])
def add_booking():
data = request.get_json()
bookings.append(data)
return jsonify(data), 201
if __name__ == '__main__':
app.run(port=5002, debug=True)
