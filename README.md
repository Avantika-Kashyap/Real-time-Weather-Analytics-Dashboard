# 🌤️ Real-Time Weather Analytics Dashboard

A Python-based data analytics project that fetches live weather data from an API, stores it in a structured format, and visualizes key insights through an interactive frontend dashboard.

## 📌 Project Overview
The goal of this project is to create a live data pipeline that tracks weather conditions for different locations. It fetches real-time data using an API, cleans and saves it into a CSV file, and displays the metrics visually on a web interface.

## 🛠️ Tech Stack Used

* *Language:* Python
* *Data Ingestion:* requests library (for API integration)
* *Data Storage:* CSV File (live_weather_data.csv)
* *Dashboard/UI:* Streamlit
* *Charts/Visuals:* Plotly

## 📊 Insights & Key Metrics Captured

* *Hottest City:* Dynamically finds the city with the highest temperature.
* *Coolest City:* Tracks the city with the lowest temperature drop.
* *Average Humidity:* Calculates the overall moisture levels across all cities.
* *Data Consistency:* The script safely handles data ingestion and appends clean rows into the CSV file without creating duplicates.

## 🚀 Main Features

* *Live API Pipeline:* Fetches real-time, current weather data instantly.
* *Interactive Dashboard:* Dynamic UI with live-updating KPIs and responsive charts.
* *Local Data Store:* Maintains a clean log of historical fetches for data tracking.

## 🎥 Project Demo



https://github.com/user-attachments/assets/fc7705bd-05ee-4b2c-8cab-3787d0f9eb1a




# Ab code automatic environment se key utha lega
API_KEY = os.getenv("OPENWEATHER_API
