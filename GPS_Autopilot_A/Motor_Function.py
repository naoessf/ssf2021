import math as m
import RPi.GPIO as GPIO
import operator

# GPIO Setup

def gpiosetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

def dcmotor():
    dcmotor = GPIO.PWM(11, 50)
    dcmotor.start(0)
    dcmotor.ChangeDutyCycle(7.5)

def svmotor():
    svmotor = GPIO.PWM(12,50)
    svmotor.start(0)
    svmotor.ChangeDutyCycle(7.5)

# DCmotor
def forward():
    dcmotor = GPIO.PWM(11, 50)
    forward = dcmotor.ChangeDutyCycle(8)
    return forward

def cleanup():
    GPIO.cleanup()