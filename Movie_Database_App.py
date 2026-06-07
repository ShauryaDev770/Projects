import json
import requests
import os

while True:
    movie_name = input("Search the movie name: ").lower()
    url ="http://www.omdbapi.com/?"
    params = {
    "t" : movie_name,
    "apikey" : "your_api_key"
    }
    response = requests.get(url,params=params)
    data = response.json()
    
    validation = data["Response"]
    if validation == 'False' :
        print("Invalid Name, Try again.")
        continue
    else:
        break

info = {
    "Title" : data["Title"],
    "Release date": data["Released"],
    "Rated" : data["Rated"],
    "Genre" : data["Genre"],
    "Actors" : data["Actors"],
    "Plot" : data["Plot"],
    "Awards" : data["Awards"],
    "IMDB Rating": data['Ratings'][0]['Value']
}

print(info)
d = []
if os.path.exists("Movie_Database.json") and os.path.getsize("Movie_Database.json") >0:
    with open("Movie_Database.json","r") as file:
       d =  json.load(file)

d.append(info)

with open("Movie_Database.json","w") as f:
    json.dump(d,f,indent =4)
