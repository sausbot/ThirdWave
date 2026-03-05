# ThirdWave

ThirdWave is a web application that helps users find coffee shops in any city using the Google Places API. It leverages Flask for the backend and a simple HTML interface for user interaction.

## Demo

![ThirdWave Demo](demo.gif)

## Features

- Search for coffee shops in any city.
- Randomly selects a coffee shop from the search results.
- Displays the name and address of the selected coffee shop.
- Uses the Google Places API for accurate and up-to-date results.
- Geocoding is powered by the Geopy library.

## Project Structure

- **`app.py`**: The main Flask application that handles API requests and serves the frontend.
- **`place_search.ipynb`**: A Jupyter Notebook for testing and experimenting with the Google Places API.
- **`templates/index.html`**: The frontend HTML file for user interaction.

## Prerequisites

- Docker Compose version v2.13.0
- Google Places API key

## Run with Docker

Run the following commands

```bash
docker-compose build
docker-compose up
```

Access the app at `http://localhost:5000`

## Test

```
docker-compose run --rm test
```

## Usage

Enter the name of a city in the input field.
Click the "Find me a cafe" button.
The app will display the name and address of a randomly selected coffee shop in the specified city.

## Notes
Ensure that your Google Places API key has the necessary permissions for the Places API and Geocoding API. The project is for educational purposes and should not be used in production without proper security measures.