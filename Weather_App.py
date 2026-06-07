import requests
import json
import os


while True:
    city_name = input("Enter the city name: ")

    API_url_geocoding = "http://api.openweathermap.org/geo/1.0/direct?"

    params = {
    "q" : city_name,
    "appid" : "Your_appid",
    "limit" : 1
    }

    response = requests.get(API_url_geocoding, params=params)

    if response.status_code != 200:
        print("Connection Error.Try again.")
        continue
    
    data = response.json() # Here data is a list

    if len(data) == 0:
        print("Invalid Location")
        continue
    else:
        break
    


#Finding the index value for latitude and longitude from dict inside a list
latitude = data[0]["lat"]
longitude = data[0]["lon"]

current_weather = "https://api.openweathermap.org/data/2.5/weather"

params_new = {
    "lat" : latitude,
    "lon" : longitude,
    "units" : "metric",
    "appid" : "2d4b12f7677dd9c521c7cd119dacf347"
}


weather = requests.get(current_weather, params = params_new)

final = weather.json()
print("City : ",city_name)
print("Country : ", final["sys"]["country"])
print("weather : ",final["weather"][0]["main"])
print("temp : ",final["main"]["temp"],"Celsius")
print("Wind Speed : ",final["wind"]["speed"],"m/s")
print("Humidity levels : ",final["main"]["humidity"])

info = {
    "City" : city_name,
    "Country": final["sys"]["country"],
    "weather": final["weather"][0]["main"],
    "temp": final["main"]["temp"],
    "Wind Speed": final["wind"]["speed"],
    "Humidity levels": final["main"]["humidity"]
}

data = []


if os.path.exists("Weather.json") and os.path.getsize('Weather.json')>0:
    with open("Weather.json", "r") as file:
        data = json.load(file)

data.append(info)

with open("Weather.json","w") as f:
    json.dump(data,f,indent= 4)














