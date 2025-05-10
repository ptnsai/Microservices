from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
# PostgreSQL connection URI format: postgresql://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost:5432/users_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
 
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
 
# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()
 
# Routes
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200
 
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        email=data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201
 
if __name__ == '__main__':
    app.run(port=5004, debug=True)
