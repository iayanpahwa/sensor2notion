from sense_hat import SenseHat
from time import sleep

def display(status):
    '''
    Display status and bitmaps on dotmatrix display
    works only with senseHAT
    Generate bitmaps at https://www.pixilart.com/draw/8x8-0a612fc3d41c517
    and add them to assets folder
    '''
    if status == 200:
        sense = SenseHat()
        sense.clear() 
        sense.show_message("Success !", text_colour=[255, 0, 0], scroll_speed=0.1)
        sleep(0.2)
        sense.load_image("./assets/smile.png")  
        sleep(5)
        sense.clear()    
    else: 
        sense = SenseHat()
        sense.clear() 
        sense.show_message("Failed !", text_colour=[255, 0, 0], scroll_speed=0.1)
        sleep(0.2) 
        sense.load_image("./assets/sad.png")
        sleep(5)
        sense.clear()   
