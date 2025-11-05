from src.serve.api import app
import requests
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict(client):
    data = {
        "no2": 43,
        "pm2.5": 17,
        "benzen": 3,
        "temp": 2,
        "pressure": 987,
        "humidity": 82,
        "wind_speed": 2.76,
        "year": 2023,
        "hour": 19,
        "day": 15,
        "month": 2
    }
    response = client.post('/air/predict', json=data)

    assert response.status_code == 200
