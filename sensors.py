from sense_hat import SenseHat
from time import sleep

def readSensorValues():
    '''
    Read sensor values from sense hat
    Temperature in *C and Humidity 
    '''
    try:
        sense = SenseHat()
        sense.clear()
        temp = sense.get_temperature_from_humidity()
        humidity = sense.get_humidity()
        sensors = [temp, humidity]
        return sensors
    except:
        print("Failed to read values from sense hat, check connection")
        # if failed to read sensor values return -1 as value
        sensors = [-1, -1]
        return sensors
