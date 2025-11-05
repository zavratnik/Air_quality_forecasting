import time
import requests

def test_response():
    API_key = "facbbd327383c3c420b0a461707dc933"
    present_time = int(time.time())
    past_time = present_time - (7*24*60*60)

    url = f"https://history.openweathermap.org/data/2.5/history/city?lat=46.55&lon=15.65&type=hour&start={past_time}&end={present_time}&appid={API_key}"
    response = requests.get(url)

    assert response.status_code == 200