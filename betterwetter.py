import requests
import json
import pgeocode
import os
from dotenv import load_dotenv

country = pgeocode.Nominatim('us')
zip_code = int(input("Which ZIP code area are you in now? > "))
location_data = country.query_postal_code(zip_code)

