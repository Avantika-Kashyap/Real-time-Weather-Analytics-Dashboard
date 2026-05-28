import requests
import os
from dotenv import load_dotenz
load_dotenz()
API_KEY = os.environ.get("MY_WEATHER_KEY")
if not API_KEY:
    API_KEY = "YOUR_API_KEY_HERE"
CITY = "Lucknow"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    # API ko request bhej rahe hain
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("--- LIVE DATA FETCHED SUCCESSFULLY ---")
        
        # Data mein se zaroori cheezein nikalna (Data Extraction)
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        print(f"City: {CITY}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_desc.title()}")
        print(f"Wind Speed: {wind_speed} m/s")
        
    else:
        print(f"Error Code: {response.status_code}")
        print("Tip: Agar error 401 hai, toh thoda 5-10 minute wait karein, naye account ki key activate hone mein thoda time leti hai.")

except Exception as e:
    print(f"An error occurred: {e}")
    import requests
import pandas as pd # Agar error aaye toh terminal mein 'pip install pandas' chalana
from datetime import datetime

# Un cities ki list jinka data humein chahiye
CITIES = ["Lucknow", "Delhi", "Mumbai", "Bangalore", "Kolkata"]

# Khali list jisme saari cities ka data jama hoga
weather_data_list = []

print("--- FETCHING REAL-TIME DATA FOR MULTIPLE CITIES ---")

for city in CITIES:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Data Extraction & Cleaning
        city_weather = {
            "City": city,
            "Temperature (°C)": data['main']['temp'],
            "Humidity (%)": data['main']['humidity'],
            "Wind Speed (m/s)": data['wind']['speed'],
            "Condition": data['weather'][0]['description'].title(),
            "Last Updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Real-time Timestamp
        }
        
        weather_data_list.append(city_weather)
        print(f"✅ Successfully fetched data for {city}")
    else:
        print(f"❌ Failed for {city} (Error: {response.status_code})")

# 1. Convert to Pandas DataFrame (Table Format)
df = pd.DataFrame(weather_data_list)

# 2. Output ko screen par dekhna
print("\n--- PROCESSED DATA FRAME ---")
print(df)

df.to_csv("live_weather_data.csv", index=False)
print("\n💾 Data saved successfully as 'live_weather_data.csv'!")

