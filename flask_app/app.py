import requests
import random

from flask import Flask, request, render_template
from flask_cors import CORS
from geopy.geocoders import Nominatim


app = Flask(__name__)
CORS(app)

KEY = ""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def process():
    input_data = request.get_json()["data"]
    # Process the data
    result = get_coffee_shop(input_data)
    return {"result": result}


def get_coffee_shop(city, radius=2000):
    latitude, longitude = get_location_cordinates(city)
    params = {
        "location": f"{latitude},{longitude}",
        "radius": radius,
        "keyword": "coffee shop",
        "key": KEY,
    }

    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params
    )

    result = response.json()
    len_results = len(result["results"])

    if len_results == 0:
        return "No coffee found, try a different city!"

    selected_idx = random.randint(0, len_results - 1)
    name = result["results"][selected_idx]["name"]
    address = result["results"][selected_idx]["vicinity"]

    return f"{name}, {address}"


def get_location_cordinates(city):
    geolocator = Nominatim(user_agent="ThirdWave")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude


if __name__ == "__main__":
    app.run("localhost", 5000)
