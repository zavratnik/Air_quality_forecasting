import pandas as pd
import numpy as np

current_data = pd.read_csv('data/processed/current_data.csv')

common_columns = ['pm10','temp','pressure','humidity','wind_speed','year','month','day','time']

train_data = current_data.sample(frac=0.9, random_state=42)
test_data = current_data.drop(train_data.index)

train_data = train_data[common_columns]
test_data = test_data[common_columns]

train_data.to_csv('data/processed/train.csv', index=False)
test_data.to_csv('data/processed/test.csv', index=False)
