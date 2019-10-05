import csv
import matplotlib.pyplot as plt
import requests
import pandas as pd
from config2 import api_key
from pprint import pprint


def make_df(city_list):
    
    #We will be making a list of dictionaries that we will eventually turn into our dataframe
    dict_list = []
    
    #Loops through every city in the provided list. List format must be: [[city1, state1, country1], 
    #[city2, state2, country2]]. If it's a country without a state, just put the city name as the state in the list.
    #(Although some international cities have states.)
    for c in range(0, len(city_list)):
        
        #Locates the necessary info from the list.
        citi = city_list[c][0]
        state = city_list[c][1]
        country = city_list[c][2]
        
        
        #Builds our url.
        url = f"https://api.airvisual.com/v2/city?city={citi}&state={state}&country={country}&key="
        
        #Adds the api_key
        query_url = url + api_key

        #Pulls our response
        response = requests.get(query_url).json()

        #Only puts the state in the table if it's from the U.S.
        if country == 'USA':
            state = response['data']['state']
        else:
            state = 'N/A'
            
            
            api_key
        #Pulls the necessary information (feel free to add or paramets)
        city = response['data']['city']
        country = response['data']['country']
        temperature = response['data']['current']['weather']['tp']
        air_qual = response['data']['current']['pollution']['aqius']
        humidity = response['data']['current']['weather']['hu']
        pressure = response['data']['current']['weather']['pr']
        wind_speed = response['data']['current']['weather']['ws']
        time = response['data']['current']['weather']['ts']
        longitude= response['data']['location']['coordinates'][0]
        latitude= response['data']['location']['coordinates'][1]
        #Takes all that information and puts it into a dictionary whcih we will then append to our dict_list.
        data_dict = {'City' : city, 'State' : state, 'Country' : country, 'Longitude': longitude, 'Latitude': latitude, 
                     'Air Quality' : air_qual, 'Temperature' : temperature, 
                     'Humidity': humidity, 'Pressure' : pressure, 'Wind Speed' : wind_speed, 'Date' : time}
        dict_list.append(data_dict)
    
    #Turns our dict_list into a dataframe and returns it.
    dataframe = pd.DataFrame(dict_list)
    dataframe["Date"] = pd.to_datetime(dataframe["Date"])
    dataframe["Date"] = dataframe["Date"].dt.date
    return dataframe
    

#This is where our opportunity to loop into our cities.
#Each city in the list must be formatted as [[city, state, country]]
example_city_list = [['Beijing', 'Beijing', 'China'], ['Asheville', 'North Carolina', 'USA'], ['Austin', 'Texas', 'USA']]

make_df(example_city_list)