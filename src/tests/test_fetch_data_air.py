import requests

def test_response():
    url = "https://arsoxmlwrapper.app.grega.xyz/api/air/archive"
    response = requests.get(url)

    assert response.status_code == 200