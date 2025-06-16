import os
import requests
import random

from flask import Flask, request, render_template
from flask_cors import CORS
from geopy.geocoders import Nominatim


app = Flask(__name__)
CORS(app)

# Get the Google API key from the environment variable
KEY = os.getenv("GOOGLE_API_KEY", "")
if not KEY:
    print("Warning: GOOGLE_API_KEY environment variable is not set.")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def process():
    "Process the data from the form"
    input_data = request.get_json()["data"]
    result = get_coffee_shop(input_data)
    return {"result": result}


def get_coffee_shop(city, radius=2000):
    "Find a coffee shop in the given city and radius"
    latitude, longitude = get_location_cordinates(city)
    if latitude is None or longitude is None:
        return {"message": "Could not find the specified city. Please try another."}
    params = {
        "location": f"{latitude},{longitude}",
        "radius": radius,
        "keyword": "coffee shop",
        "key": KEY,
    }

    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params
    )

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return {"message": "Failed to fetch data from Google Places API. Please try again later."}

    # Parse the JSON response
    result = response.json()
    len_results = len(result["results"])

    if len_results == 0:
        return "No coffee found, try a different city!"

    selected_idx = random.randint(0, len_results - 1)
    name = result["results"][selected_idx]["name"]
    address = result["results"][selected_idx]["vicinity"]

    return f"{name}, {address}"


def get_location_cordinates(city):
    "Get the latitude and longitude of the given city"
    geolocator = Nominatim(user_agent="ThirdWave")
    location = geolocator.geocode(city)
    if location is None:
        return None, None
    return location.latitude, location.longitude


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
