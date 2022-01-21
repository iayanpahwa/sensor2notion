import os
import weather
import sensors
import schedule
import dotmatrix
import post2notion
from time import sleep
from datetime import date

def main():
    # Setttings for weather API 
    weatherSetup = {
        'WEATHER_API_KEY' : os.environ.get('WEATHER_API_KEY'),
        'TEMP_UNIT' : os.environ.get('TEMP_UNIT'),
        'LAT' : os.environ.get('LAT'),
        'LON' : os.environ.get('LON')
        } 

    # Setttings for Notion API
    NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
    DATABASE_ID = os.environ.get('DATABASE_ID')

    headers = {
        "Authorization" : "Bearer " + NOTION_API_KEY,
        "Content-Type" : "application/json",
        "Notion-Version" : "2021-05-13"
    }

    #fetch current date
    today = str(date.today())
    print("Date: {0}".format(today))

    #fetch current weather and AQ
    print("Fetching outside temperature and Air Quality...")
    outsideTemperature = weather.fetch_weather(weatherSetup)
    print("Outside Temperature: {0}".format(outsideTemperature))

    AQI = weather.fetch_aqi(weatherSetup)

    if AQI == 5:
        outsideAQI = 'Very Poor'
    elif AQI == 4:
        outsideAQI = 'Poor'
    elif AQI == 3:
        outsideAQI = 'Moderate'
    elif AQI == 2:
        outsideAQI = 'Fair' 
    elif AQI == 1:
        outsideAQI = 'Good'     
    else:
        outsideAQI = "-1"  

    print("Outdoor Air Quality: {0}".format(outsideAQI))

    #fetch sensor values from sense hat
    print("Fetching indoor temperature and Humidity from sensors...")
    sensorVal = sensors.readSensorValues()
    homeTemperature = float("{:.2f}".format(sensorVal[0]))
    homeHumidity = float("{:.2f}".format(sensorVal[1]))

    print("Home Temperature: {0}".format(homeTemperature))
    print("Home Humidity: {0}".format(homeHumidity))

    notionData = {
        'date': today,
        'outsideTemperature' : outsideTemperature,
        'outsideAQI' : outsideAQI,
        'homeTemperature' : homeTemperature,
        'homeHumidity' : homeHumidity
        }

    print("Posting to Notion database...")
    ret = post2notion.createPage(DATABASE_ID,headers,notionData)
    print(ret)
    dotmatrix.display(ret)

print("New data will be fetched and posted to notion everyday at: {0}".format(os.environ.get('TIME')))
schedule.every().day.at(os.environ.get('TIME')).do(main)

while True:
    schedule.run_pending()
    sleep(10)
