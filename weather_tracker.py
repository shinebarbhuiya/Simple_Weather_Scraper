# A very basic program that shows the weather of a certain location.
# Scrapes the google page 

import requests
from bs4 import BeautifulSoup as BS


location = input("Enter your city: ")

URL = f"https://www.google.com/search?q={location}+weather"

page = requests.get(URL, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"})
soup = BS(page.content, "html.parser")


# Scraped the google page and quits if it shows no result for the location.
# It searches for the id "wob_tm" which only shows up when the location is correct.
temp_element = soup.find(id = "wob_tm")
if temp_element == None:
    print("Ehh! There's no such place.")
    quit()

def weather_cond():
    """Shows weather condition"""

    weather_condition= soup.find(id = "wob_dcp").text
    return weather_condition

def temp_celsius():
    """Scrapes the weather in Celsius from google"""
    
    celsius_temp = soup.find(id = "wob_tm").text 
    return celsius_temp

def temp_fahrenheit():
    """Scrapes the weather in fahrenheit"""

    fahrenheit_temp = soup.find(id = "wob_ttm").text
    return fahrenheit_temp

def show_weather():
    """Shows the weather in a good format."""

    print(f"\n{location.title()} is {weather_cond()} today.")
    print(f"... and the temp is {temp_celsius()}°C and {temp_fahrenheit()}°F.")

show_weather()



