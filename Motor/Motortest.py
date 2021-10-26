import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

dcmotor = GPIO.PWM(11, 50)
dcmotor.start(0)
svmotor = GPIO.PWM(12, 50)
svmotor.start(0)

while True:
    direction = float(input("Direction (2~7.5~12) : "))
    svmotor.ChangeDutyCycle(direction)
    speed = float(input("Speed (2~7.5~12) : "))
    dcmotor.ChangeDutyCycle(speed)
    if direction == 0 or speed == 0:
        svmotor.ChangeDutyCycle(7.5)
        dcmotor.ChangeDutyCycle(7.5)
        break

svmotor.stop()
dcmotor.stop()
GPIO.cleanup
