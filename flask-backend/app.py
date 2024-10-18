from flask import Flask, jsonify, request
from flask_cors import CORS
from recommendation import get_recommendations  # Import the recommendation function
import logging

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Flask server is running!"


@app.route("/api/recommend", methods=["POST"])
def recommend_wines():
    try:
        data = request.json
        logging.info("Received data: %s", data)

        # Input validation could be added here
        if "country" not in data or "taste" not in data:
            return jsonify({"error": "Missing data for country or taste"}), 400

        country_preference = data.get("country", "").capitalize()
        taste_preference = data.get("taste", "").lower()

        # Get the recommendations from the recommendation system
        recommendations = get_recommendations(country_preference, taste_preference)
        return jsonify(recommendations)

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        return (
            jsonify({"error": "An error occurred while processing your request"}),
            500,
        )


if __name__ == "__main__":
    app.run(debug=True)
