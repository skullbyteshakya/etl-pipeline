from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the root endpoint
@app.route('/')
def hello():
    return 'Hello, Nakama!'
#
# @app.route('/data')
# def hello():
#     return '/api/data'


# Define a route for an API endpoint
@app.route('/api/data')
def get_data():
    # Hardcoded JSON data
    data = [
        {
            "island_id": 1,
            "name": "Alabasta",
            "terrain": "Desert",
            "climate": "Hot"
        },
        {
            "island_id": 2,
            "name": "Dressrosa",
            "terrain": "Plateau",
            "climate": "Mild"
        },
        {
            "island_id": 3,
            "name": "Wano Country",
            "terrain": "Mountain",
            "climate": "Cold"
        },
        {
            "island_id": 4,
            "name": "Water 7",
            "terrain": "City",
            "climate": "Mild"
        },
        {
            "island_id": 5,
            "name": "Whole Cake Island",
            "terrain": "Island",
            "climate": "Warm"
        },
        {
            "island_id": 6,
            "name": "Enies Lobby",
            "terrain": "Island",
            "climate": "Warm"
        },
        {
            "island_id": 7,
            "name": "Skypiea",
            "terrain": "Sky Island",
            "climate": "Cloudy"
        },
        {
            "island_id": 8,
            "name": "Fish-Man Island",
            "terrain": "Underwater",
            "climate": "Humid"
        },
        {
            "island_id": 9,
            "name": "Drum Island",
            "terrain": "Winter Island",
            "climate": "Cold"
        }
    ]

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
