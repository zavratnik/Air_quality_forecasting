import pandas as pd
import datetime

df_air = pd.read_csv('data/processed/air/obdelani_podatki_air.csv')
df_weather = pd.read_csv('data/processed/weather/obdelani_podatki_weather.csv')

df = pd.merge(df_air, df_weather, on=['year', 'month', 'day', 'time'], how='inner')

df['year'] = df.pop('year')
df['month'] = df.pop('month')
df['day'] = df.pop('day')
df['time'] = df.pop('time')

df.drop(['no2'], axis=1, inplace=True)
df.drop(['pm2.5'], axis=1, inplace=True)
df.drop(['benzen'], axis=1, inplace=True)

df.to_csv('data/processed/current_data.csv', index=False)

print(df)

last_3_days_df = df

last_3_days_df['datetime'] = pd.to_datetime(last_3_days_df[['year', 'month', 'day']])
three_days_ago = datetime.datetime.now() - datetime.timedelta(days=4)
df_filtered = last_3_days_df[last_3_days_df['datetime'] > three_days_ago]

df_grouped = df_filtered.groupby(['year', 'month', 'day']).agg({
    'pm10': 'mean',
    'temp': ['max', 'min'],
    'wind_speed': 'mean'
}).reset_index()

df_grouped.columns = ['year', 'month', 'day', 'mean_pm10', 'max_temp', 'min_temp', 'mean_wind_speed']

df_grouped.to_csv('data/processed/weather/last_3_days.csv', index=False)
