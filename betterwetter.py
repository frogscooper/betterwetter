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

##Shitty code that filters the data received from pgeocode into just (City, State)
location_data = str(pandas.Series(zip_location, index = ["place_name", "state_code"]))
location_data = location_data.split()
del location_data[0], location_data[1], location_data[2:]
city_name = ','.join(location_data)


load_dotenv()
api_key = os.environ.get("Your_API_Key")
base_weather_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_weather_url = base_weather_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_weather_url)
print(response)
