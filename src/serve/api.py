import csv

import pandas as pd
import requests
from flask import Flask, request, jsonify, render_template
import pickle
import os
#
app = Flask(__name__, template_folder='../client', static_folder='../client/static')

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'model.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)


@app.route('/air/predict', methods=['POST'])
def predict():
    data = request.get_json()

    input_data = [
        [data['temp'], data['pressure'], data['humidity'], data['wind_speed'], data['year'], data['month'], data['day'],
         data['hour']]]

    prediction = model.predict(input_data)

    return jsonify({'prediction': prediction[0]}), 200, {'Content-Type': 'application/json'}


@app.route('/')
def index():
    air_df = pd.read_csv('../../data/processed/air/obdelani_podatki_air.csv')
    air_last = air_df.tail(1)

    # air quality
    no2 = air_last['no2'].values[0]
    pm25 = air_last['pm2.5'].values[0]
    benzen = air_last['benzen'].values[0]
    pm10 = air_last['pm10'].values[0]

    # highest, lowest air quality
    no2_high = air_df['no2'].max()
    no2_low = air_df['no2'].min()
    pm25_high = air_df['pm2.5'].max()
    pm25_low = air_df['pm2.5'].min()
    benzen_high = air_df['benzen'].max()
    benzen_low = air_df['benzen'].min()
    pm10_high = air_df['pm10'].max()
    pm10_low = air_df['pm10'].min()

    # percentage air quality
    no2_percentage = no2 / no2_high * 100
    pm25_percentage = pm25 / pm25_high * 100
    benzen_percentage = benzen / benzen_high * 100
    pm10_percentage = pm10 / pm10_high * 100

    pm10_df = air_df[['year', 'month', 'day', 'time', 'pm10']].tail(20)
    pm10_df['date_time'] = pm10_df.apply(lambda row: f"{row['year']}-{row['month']}-{row['day']} {row['time']}", axis=1)
    pm10_df = pm10_df[['date_time', 'pm10']]

    last_date = pm10_df['date_time'].values[0]

    weather_df = pd.read_csv('../../data/processed/weather/obdelani_podatki_weather.csv')
    weather_last = weather_df.tail(1)

    # weather
    temp = int(weather_last['temp'].values[0])
    pressure = weather_last['pressure'].values[0]
    humidity = weather_last['humidity'].values[0]
    wind_speed = weather_last['wind_speed'].values[0]


    #pm10 forecast
    last_3_days = pd.read_csv('../../data/processed/weather/last_3_days.csv')
    data_last = last_3_days.to_dict('records')
    print(data_last)

    future_3_days = pd.read_csv('../../data/processed/weather/future_3_days.csv')
    data_future = future_3_days.to_dict('records')


    return render_template('index.html', last_date=last_date, no2=no2, pm25=pm25, benzen=benzen, pm10=pm10,
                           temperature=temp, pressure=pressure, humidity=humidity, wind_speed=wind_speed,
                           no2_high=no2_high, no2_low=no2_low, pm25_high=pm25_high, pm25_low=pm25_low,
                           benzen_high=benzen_high, benzen_low=benzen_low, pm10_high=pm10_high, pm10_low=pm10_low,
                           no2_percentage=no2_percentage, pm25_percentage=pm25_percentage,
                           benzen_percentage=benzen_percentage, pm10_percentage=pm10_percentage,
                           data_future=data_future, data_last=data_last)

if __name__ == '__main__':
    app.run(debug=True)
