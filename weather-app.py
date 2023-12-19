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

def get_weather_data(latitude, longitude):
    # https://open-meteo.com/en/docs
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&hourly=temperature_2m&forecast_days=1"
    result = requests.get(url)

    # Serializing json
    json_object = json.dumps(result.json(), indent=4)
    
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    f = open('sample.json',)
    json_result = json.load(f)

    f.close()

    print(json_result['hourly']['temperature_2m'])
    

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="WeatherApp")

    location = geolocator.geocode(city_name)

    get_weather_data(location.latitude, location.longitude)
    #print(f"The latitude of {city_name} is: ", location.latitude)
    #print(f"The longitude of {city_name} is: ", location.longitude)

def main():
    root = Tk()
    root.title("Weather Application by Josef Swadi Johansson")
    root.geometry("400x400")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="City : ").grid(column=0, row = 0)

    city_input = ttk.Entry(root)
    city_input.grid(column=1, row = 0)
    
    ttk.Button(frm, text="Search", command=(lambda:get_coordinates(city_input.get()))).grid(column = 2, row=0)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column = 0, row=2)
    root.mainloop()

main()
