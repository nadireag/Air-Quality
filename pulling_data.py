import csv
import matplotlib.pyplot as plt
import requests
import pandas as pd
from config import api_key

# base_url = 'https://api.census.gov/data/timeseries/qwi/se'

base_url = f'api.census.gov/data/timeseries/qwi/sa?get=Emp&for=county:198&in=state:02&year=2012&quarter=1&sex=1&sex=2&agegrp=A02&agegrp=A07&ownercode=A05&firmsize=1&seasonadj=U&industry=11&key=[{api_key}]'
response = requests.get(base_url).json()

print(api_key)
print(response)
