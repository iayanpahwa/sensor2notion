from sense_hat import SenseHat
from time import sleep

def readSensorValues():
    try:
        sense = SenseHat()
        sense.clear()
        temp = sense.get_temperature_from_humidity()
        humidity = sense.get_humidity()
        sensors = [temp, humidity]
        return sensors
    except:
        print("Failed to read values from sense hat, check connection")
        sensors = [-1, -1]
        return sensors
