import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

svmotor = GPIO.PWM(12, 50)
svmotor.start(0)

while True:
    direction = float(input("Direction (2~7.5~12) : "))
    if 2 <= direction <= 12:
        svmotor.ChangeDutyCycle(direction)
    elif direction == 0:
         svmotor.ChangeDutyCycle(7.5)
         break

svmotor.stop()
GPIO.cleanup
