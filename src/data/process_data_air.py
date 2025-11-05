import json
import requests
import pandas as pd
import numpy as np
import pprint
import matplotlib.pyplot as plt

MB_Titova = []
jsonFile = open('data/raw/air/neobdelani_podatki.json', 'r')
values = json.load(jsonFile)
for val in values:
    json_object = json.loads(val["json"])
    MB_Titova.append(json_object["arsopodatki"]["postaja"][4])
df = pd.DataFrame(MB_Titova)

#print(df.columns)

df.drop(['merilno_mesto'], axis=1, inplace=True)
df.drop(['ge_sirina'], axis=1, inplace=True)
df.drop(['ge_dolzina'], axis=1, inplace=True)
df.drop(['nadm_visina'], axis=1, inplace=True)
df.drop(['datum_do'], axis=1, inplace=True)

# print(df.loc[df['sifra'] != 'E407'])
df.drop(['sifra'], axis=1, inplace=True)

df.sort_values(by="datum_od", inplace=True)

#print(df.head(10))
#print(df)

df['datum_od'] = pd.to_datetime(df['datum_od'], format='%Y-%m-%d %H:%M')
df = df.set_index('datum_od')

df = df.replace('', np.nan)
df.loc[df["pm2.5"] == "<2", "pm2.5"] = 0
df.loc[df["pm10"] == "<2", "pm10"] = 0

df = df.groupby(pd.Grouper(freq='1H'), group_keys=False).apply(lambda x: x.fillna(x.mean(numeric_only=True)).head(1))
df = df.fillna(df.mean(axis=0))
df = df.reset_index()
df = df.astype({'no2': 'int','pm2.5': 'int', 'benzen': 'int', 'pm10': 'int'})

df['year'] = df['datum_od'].dt.year
df['month'] = df['datum_od'].dt.month
df['day'] = df['datum_od'].dt.day
df['time'] = df['datum_od'].dt.hour

first_date = df['datum_od'].iloc[0]
first_date_unix = int(first_date.timestamp())
last_date = df['datum_od'].iloc[-1]
last_date_unix = int(last_date.timestamp())

df.drop(['datum_od'], axis=1, inplace=True)

df.to_csv('data/processed/air/obdelani_podatki_air.csv', index=False)
