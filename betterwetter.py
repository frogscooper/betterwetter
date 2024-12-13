import requests
import json
import pgeocode
import pandas
import os
from dotenv import load_dotenv

## Uses the pgeocode library to get information about an area from the ZIP code
country = pgeocode.Nominatim('us')
zip_code = int(input("Which ZIP code area are you in now? > "))
zip_location = country.query_postal_code(zip_code)

##Shitty code that filters the data received from pgeocode into just Latitude and Longitude
location_data = str(pandas.Series(zip_location, index = ["latitude", "longitude"]))
location_data = location_data.split()
del location_data[0], location_data[1], location_data[2:]

##Queries OpenWeatherMap for the weather
load_dotenv()
api_key = os.environ.get("Your_API_Key")
base_weather_url = str(f"http://api.openweathermap.org/data/2.5/weather?")
complete_weather_url = base_weather_url + "lat=" + location_data[0] + "&lon=" + location_data[1] + "&appid=" + api_key
response = requests.get(complete_weather_url)
weather = response.json()
print(weather)
