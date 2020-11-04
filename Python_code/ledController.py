import wiringpi
from ledDBConnection import dbConnect

LED_red = 15
LED_green = 4
LED_yellow = 10

def ledControl(color, mode):  
   
    init()

    red_status = wiringpi.digitalRead(LED_red)
    green_status = wiringpi.digitalRead(LED_green)
    yellow_status = wiringpi.digitalRead(LED_yellow)

    if 'r' in color:
        red_status = mode
    if 'g' in color:
        green_status = mode
    if 'y' in color:
        yellow_status = mode
    
    ledWrite(red_status,green_status,yellow_status)

    dbConnect(red_status, green_status, yellow_status)

def init():

    wiringpi.wiringPiSetup()
    wiringpi.pinMode(LED_red,1)
    wiringpi.pinMode(LED_green, 1)
    wiringpi.pinMode(LED_yellow, 1)

def ledWrite(red,green,yellow):
    
    wiringpi.digitalWrite(LED_red,red)
    wiringpi.digitalWrite(LED_green,green)
    wiringpi.digitalWrite(LED_yellow,yellow)

