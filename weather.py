import requests

def fetch_weather(settings):
    '''
    Read current weather using OpenWeatherMap API
    Requires:
    - Latitude
    - Longitude
    - API Key
    '''
    BASE_WEATHER = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}&units={3}"
    weather_url = BASE_WEATHER.format(settings["LAT"],settings["LON"],settings["WEATHER_API_KEY"],settings["TEMP_UNIT"])
    try:
        weather_data = requests.get(weather_url).json()	 
    except requests.exceptions.RequestException as e:
        print("Failed to featch from openweathermap, check connection or API Key !!")
        return -1
    else:
        temperature = weather_data['main']['temp'] 
        return temperature

def fetch_aqi(settings):
    '''
    Read current Air Quality using OpenWeatherMap API
    Requires:
    - Latitude
    - Longitude
    - API Key
    '''
    BASE_AQI = "http://api.openweathermap.org/data/2.5/air_pollution?lat={0}&lon={1}&appid={2}"
    aqi_url = BASE_AQI.format(settings["LAT"],settings["LON"],settings["WEATHER_API_KEY"])
    try:
        aqi_data = requests.get(aqi_url).json()
    except requests.exceptions.RequestException as e:
        print("Failed to featch from openweathermap, check connection or API Key !!")
        return -1
    else:
        aqi = aqi_data['list'][0]['main']['aqi']
        return aqi
