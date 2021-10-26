import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.cleanup(16)

while True:
    LED = float(input("1 : on, 0 : off, 2 : exit  >>  "))
    if LED == 0:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, True)
    elif LED == 1:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, False)
    else:
        break