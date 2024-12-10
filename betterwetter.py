import requests
import json
import pgeocode
import pandas
import os
from dotenv import load_dotenv

country = pgeocode.Nominatim('us')
zip_code = int(input("Which ZIP code area are you in now? > "))
zip_location = country.query_postal_code(zip_code)

location_data = str(pandas.Series(zip_location, index = ["place_name", "state_code"]))
location_data = location_data.split()
del location_data[0], location_data[1], location_data[2:]
filtered_location_data = ', '.join(location_data)
print(filtered_location_data)
