from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
app = Flask(__name__)
 
# PostgreSQL connection URI format: postgresql://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost:5432/showtimes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
# Showtime model
class Showtime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
 
    def to_dict(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "start_time": self.start_time.isoformat(),
            "available_seats": self.available_seats
        }
 
# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()
 
# Routes
@app.route('/showtimes', methods=['GET'])
def get_showtimes():
    showtimes = Showtime.query.all()
    return jsonify([showtime.to_dict() for showtime in showtimes]), 200
 
@app.route('/showtimes', methods=['POST'])
def add_showtime():
    data = request.get_json()
    new_showtime = Showtime(
        movie_id=data['movie_id'],
        start_time=datetime.fromisoformat(data['start_time']),
        available_seats=data['available_seats']
    )
    db.session.add(new_showtime)
    db.session.commit()
    return jsonify(new_showtime.to_dict()), 201
 
if __name__ == '__main__':
    app.run(port=5003, debug=True)
