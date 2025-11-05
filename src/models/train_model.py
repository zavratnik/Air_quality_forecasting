import pandas as pd
import numpy as np
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score

df_train = pd.read_csv("data/processed/train.csv", sep=",", decimal=".", index_col=False)
df_test = pd.read_csv("data/processed/test.csv", sep=",", decimal=".", index_col=False)

df_vhod_train = df_train.drop('pm10', axis=1)
df_izhod_train = df_train['pm10']

df_vhod_test = df_test.drop('pm10', axis=1)
df_izhod_test = df_test['pm10']

X_train = df_vhod_train.values
y_train = df_izhod_train.values

X_test = df_vhod_test.values
y_test = df_izhod_test.values

reg = LinearRegression()
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

var = explained_variance_score(y_test, y_pred)

metrike = 'mean_absolute_error: ' + str(mae) + '\nmean_squared_error: ' + str(mse) + '\nexplained_variance_score: ' + str(var)
with open('reports/train_metrics.txt', 'w') as f:
    f.write(metrike)

with open("models/model.pkl", "wb") as f:
    pickle.dump(reg, f)
