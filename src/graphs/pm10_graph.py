import json
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('../../data/processed/air/obdelani_podatki_air.csv')

pm10_df = df[['year', 'month', 'day', 'time', 'pm10']].tail(50)
pm10_df['date_time'] = pm10_df.apply(lambda row: f"{row['year']}-{row['month']}-{row['day']} {row['time']}", axis=1)
pm10_df = pm10_df[['date_time', 'pm10']]

# Create plot
fig, ax = plt.subplots(figsize=(14, 5))
ax.bar(pm10_df['date_time'], pm10_df['pm10'], width=0.7, color='limegreen')

# Set title and axis labels
ax.set_title('PM10 Graph for Maribor', fontsize=18)
ax.set_ylabel('PM10 Level', fontsize=14)

# Format x-axis ticks
ax.xaxis.set_major_locator(plt.MaxNLocator(10))
ax.tick_params(axis='x', labelrotation=15, labelsize=10)

plt.savefig('../client/static/pm10_concentration.png')