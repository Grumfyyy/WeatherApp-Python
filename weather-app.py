#tkinter documentation - https://docs.python.org/3/library/tkinter.html
#tkinter entry documentation - https://python-course.eu/tkinter/entry-widgets-in-tkinter.php
from tkinter import *
from tkinter import ttk

#Geopy example - https://www.tutorialspoint.com/how-to-get-the-longitude-and-latitude-of-a-city-using-python
from geopy.geocoders import Nominatim

#requests - https://www.w3schools.com/python/module_requests.asp
import requests 
#json documentation - https://www.w3schools.com/python/python_json.asp
import json

#datetime documentation - https://www.w3schools.com/python/python_datetime.asp
import datetime

#delete file - https://www.w3schools.com/python/python_file_remove.asp
import os

class WeatherApp():

    def __init__(self):
        self.temperature = ""

    def get_weather_data(self, latitude, longitude, city_name):
        # https://open-meteo.com/en/docs
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&hourly=temperature_2m&forecast_days=1"
        result = requests.get(url)

        # Serializing json
        json_object = json.dumps(result.json(), indent=4)
        
        #writing to json data to a json file
        with open("output.json", "w") as outfile:
            outfile.write(json_object)

        #read and load the json file, that was just created
        f = open('output.json',)
        json_result = json.load(f)

        #close and delete the file
        f.close()
        os.remove('output.json')

        #print(json_result['hourly']['temperature_2m'])

        #get the current time, but i only need the current hour of the current day since i have a list of 24 values, because we have 24 hours
        current_time = datetime.datetime.now()
        current_hour = current_time.strftime('%H')

        temperature_list = json_result['hourly']['temperature_2m']
        current_temperature = temperature_list[int(current_hour)] # get the current temperature from the list of 24 values with the help of the current hour as an index

        #print out the current temperature to the prompt
        #print(f'current temperature in {city_name} = {current_temperature} \u00b0C ')

        self.temperature = str(current_temperature)
        self.temperatureText.set(f"Current temperature in {city_name} is : {current_temperature} \u00b0C")
        
    def get_coordinates(self, city_name):
        geolocator = Nominatim(user_agent="WeatherApp")

        location = geolocator.geocode(city_name)

        self.get_weather_data(location.latitude, location.longitude, city_name)
        #print(f"The latitude of {city_name} is: ", location.latitude)
        #print(f"The longitude of {city_name} is: ", location.longitude)

    def updateTemperatureText(self):
        pass

    def main(self):
        root = Tk()
        root.title("Weather Application by Josef Swadi Johansson")
        root.geometry('400x400')

        ttk.Label(root, text="City : ").place(x=5, y=5)

        city_input = ttk.Entry(root)
        city_input.place(x=50, y=5)
        
        search_button = ttk.Button(root, text="Search", command=(lambda:self.get_coordinates(city_input.get())))
        search_button.place(x = 200, y=5)

        self.temperatureText = StringVar()

        temperature_label = ttk.Label(root, textvariable=self.temperatureText)
        temperature_label.place(x=5, y=30)

        root.mainloop()

app = WeatherApp()
app.main()
