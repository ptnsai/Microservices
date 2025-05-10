from flask import Flask, jsonify, request
app = Flask(__name__)
# Sample in-memory data
movies = [
{"id": 1, "title": "Inception", "genre": "Sci-Fi", "duration": 148},
{"id": 2, "title": "The Godfather", "genre": "Crime", "duration": 175}
]
@app.route('/movies', methods=['GET'])
def get_movies():
return jsonify(movies), 200
@app.route('/movies', methods=['POST'])
def add_movie():
data = request.get_json()
movies.append(data)
return jsonify(data), 201
if __name__ == '__main__':
app.run(port=5001, debug=True)
