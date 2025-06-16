import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"city" in response.data  # Checks for the presence of the input field

def test_submit_route_empty(client):
    response = client.post("/submit", json={"data": ""})
    assert response.status_code == 200
    assert b"Could not find the specified city" in response.data or b"message" in response.data

def test_get_coffee_shop(monkeypatch):
    from app import get_coffee_shop

    def mock_get_location_cordinates(city):
        return 40.7128, -74.0060  # New York City coordinates

    def mock_requests_get(url, params):
        class MockResponse:
            status_code = 200
            def json(self):
                return {
                    "results": [
                        {
                            "name": "Test Cafe",
                            "vicinity": "123 Test St",
                            "photos": [{"photo_reference": "abc123"}]
                        }
                    ]
                }
        return MockResponse()

    import app as app_module
    monkeypatch.setattr(app_module, "get_location_cordinates", mock_get_location_cordinates)
    monkeypatch.setattr(app_module.requests, "get", mock_requests_get)

    result = get_coffee_shop("New York")
    assert "Test Cafe" in str(result)