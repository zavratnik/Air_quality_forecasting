# 🌤️ Air Quality Forecasting (Maribor – Titova Station)

A complete data pipeline and API for **PM10 concentration forecasting** using historical air-quality and weather data.  
The system performs data ingestion, preprocessing, model training, quality monitoring, and serves predictions through a Flask API and web interface.

---

## 🧭 Overview

This project predicts **PM10 levels** for the *Maribor – Titova* station using a **Linear Regression** model trained on air-quality and weather features.

The workflow includes:
1. **Data fetching** – automatic download of ARSO (air) and OpenWeather (weather) data.  
2. **Data processing** – cleaning, merging, resampling, and feature extraction.  
3. **Model training** – regression model using scikit-learn.  
4. **Monitoring** – data drift and stability reports with Evidently AI.  
5. **Deployment** – Flask API endpoint with a simple web dashboard.