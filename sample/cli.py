# -*- coding: utf-8 -*-
'''
Created on 31 déc. 2018

@author: rachid
'''
import click
import requests


SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

@click.command()
@click.option("--api-key", "-a", help="your API key for the OpenWeatherMap API")
@click.argument("location")
def main(location,api_key):
    '''
    A little weather tool that shows you the current weather in a location of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:
    1. London,UK
    2. Canmore
    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    '''
    weather = current_weather(location)
    print("The weather in {0} right now: {1}.".format(location, weather))

def current_weather(location, api_key=SAMPLE_API_KEY):
    url = "http://samples.openweathermap.org/data/2.5/weather"

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

if __name__ == '__main__':
    main()