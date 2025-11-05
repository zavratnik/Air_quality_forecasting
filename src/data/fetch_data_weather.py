import json
import requests
import process_data_air

first_date_unix = process_data_air.first_date_unix
last_date_unix = process_data_air.last_date_unix

current_time = first_date_unix

API_key = "insert here"

all_data = []

while current_time <= last_date_unix:
    next_time = current_time + (86400 * 7)
    if next_time > last_date_unix:
        next_time = last_date_unix
        history_data = f"https://history.openweathermap.org/data/2.5/history/city?lat=46.55&lon=15.65&type=hour&start={current_time}&end={next_time}&appid={API_key}"
        response = requests.get(history_data)

        if response.status_code == 200:
            data = json.loads(response.text)
            all_data.append(data)
        else:
            print(f"Error: {response.status_code}")
        break

    history_data = f"https://history.openweathermap.org/data/2.5/history/city?lat=46.55&lon=15.65&type=hour&start={current_time}&end={next_time}&appid={API_key}"
    response = requests.get(history_data)

    if response.status_code == 200:
        data = json.loads(response.text)
        all_data.append(data)
    else:
        print(f"Error: {response.status_code}")

    current_time = next_time

with open('data/raw/weather/neobdelani_podatki.json', 'w') as f:
    json.dump(all_data, f)


future_data = f"https://api.openweathermap.org/data/2.5/forecast/daily?lat=46.55&lon=15.65&cnt=3&appid={API_key}"
response = requests.get(future_data)
if response.status_code == 200:
    data_future = json.loads(response.text)
    with open('data/raw/weather/future_3_days.json', 'w') as f:
        json.dump(data_future, f)
else:
    print(f'Error: {response.status_code}')

