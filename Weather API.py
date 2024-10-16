def main():
    #importing necessary libraries
    import os
    import subprocess
    import sys
    import pip
    import pymeteosource
    from datetime import datetime, timedelta
    from pymeteosource.api import Meteosource
    from pymeteosource.types import tiers

    #API key
    api_key = 'YOUR_API_KEY' #Your API key here

    #Tiers
    tier = tiers.FREE

    #Initializing the API
    meteosource = Meteosource(api_key, tier)

    #Getting the weather data
    from pymeteosource.types import sections, langs, units
    forecast = meteosource.get_point_forecast(
        
        lat =32.271191,  #Latitude of the location
        lon =72.901138,  #Longitude of the location
        place_id= None,
        sections=[sections.CURRENT, sections.HOURLY],
        tz = 'UTC',
        lang= langs.ENGLISH,
        units= units.METRIC
    )

    #Printing the weather data
    print("Forecast Weather")
    print(forecast)
    print("Current Weather")
    print(forecast.current)
    print(forecast.current['summary'])
    print("Hourly Weather")
    print(forecast.hourly)

    #Hourly Weather
    print("Hourly temperature in degree celsius", forecast.hourly[0]['temperature'])
    print("Hourly summary", forecast.hourly[0]['summary'])
    print('Hourly wind speed in km/h', forecast.hourly[0]['wind']['speed'])

if __name__ == '__main__':
    main()

