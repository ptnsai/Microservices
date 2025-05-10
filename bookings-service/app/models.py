from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
# PostgreSQL connection URI format: postgresql://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost:5432/bookings_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
# Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    showtime_id = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
 
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "showtime_id": self.showtime_id,
            "seats": self.seats
        }
 
# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()
 
# Routes
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([booking.to_dict() for booking in bookings]), 200
 
@app.route('/bookings', methods=['POST'])
def add_booking():
    data = request.get_json()
    new_booking = Booking(
        user_id=data['user_id'],
        movie_id=data['movie_id'],
        showtime_id=data['showtime_id'],
        seats=data['seats']
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify(new_booking.to_dict()), 201
 
if __name__ == '__main__':
    app.run(port=5002, debug=True)
