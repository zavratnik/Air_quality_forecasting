import json
import requests
import pandas as pd
import numpy as np
import pprint
import datetime

MB_Titova = []
with open('data/raw/weather/neobdelani_podatki.json', 'r') as f:
    data = json.load(f)

rows = []
for d in data:
    for item in d['list']:
        row = {
            'datetime': pd.to_datetime(item['dt'], unit='s'),
            'temp': item['main']['temp'],
            'pressure': item['main']['pressure'],
            'humidity': item['main']['humidity'],
            'wind_speed': item['wind']['speed']
        }
        rows.append(row)

df = pd.DataFrame(rows)

df['temp'] = df['temp'].apply(lambda x: x - 273.15)

df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['time'] = df['datetime'].dt.hour

df.drop(['datetime'], axis=1, inplace=True)

df.to_csv('data/processed/weather/obdelani_podatki_weather.csv', index=False)


with open('data/raw/weather/future_3_days.json', 'r') as f:
    data_3_days = json.load(f)

rows_3_days = []
for item in data_3_days['list']:
    row = {
        'datetime': pd.to_datetime(item['dt'], unit='s'),
        'temp_max': item['temp']['max'],
        'temp_min': item['temp']['min'],
        'temp': item['temp']['day'],
        'pressure': item['pressure'],
        'humidity': item['humidity'],
        'wind_speed': item['speed']
    }
    rows_3_days.append(row)

df_3_days = pd.DataFrame(rows_3_days)

df_3_days['temp_max'] = df_3_days['temp_max'].apply(lambda x: x - 273.15)
df_3_days['temp_min'] = df_3_days['temp_min'].apply(lambda x: x - 273.15)
df_3_days['temp'] = df_3_days['temp'].apply(lambda x: x - 273.15)

df_3_days['year'] = df_3_days['datetime'].dt.year
df_3_days['month'] = df_3_days['datetime'].dt.month
df_3_days['day'] = df_3_days['datetime'].dt.day
df_3_days['time'] = df_3_days['datetime'].dt.hour

df_3_days.drop(['datetime'], axis=1, inplace=True)

df_3_days.to_csv('data/processed/weather/future_3_days.csv', index=False)

