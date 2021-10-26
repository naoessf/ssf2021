import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.cleanup(15)

while True:
    LED = float(input("1 : on, 0 : off, 2 : exit  >>  "))
    if LED == 0:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15, True)
    elif LED == 1:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15, False)
    else:
        break
