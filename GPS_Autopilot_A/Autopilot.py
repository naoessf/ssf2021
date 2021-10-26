## import Functions
# import GPS
from GPS import parsing

# import Destinaion
from Destination import Latitude
from Destination import Longitude

# import Basic Functions
import math as m
import RPi.GPIO as GPIO


## Destination List
# Numbering of Destination
n = int(input("Number of Destination : "))
 
# Load Function of Destination
latitude = Latitude(n)
longitude = Longitude(n)
print(latitude)
print(longitude)

## Motor Setup
# GPIO Setup
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(15, False)

dcmotor = GPIO.PWM(11, 50)
dcmotor.start(0)
dcmotor.ChangeDutyCycle(7.5)

svmotor = GPIO.PWM(12,50)
svmotor.start(0)
svmotor.ChangeDutyCycle(7.5)

## Main
# Setup Coefficient
i = 0
ps = 1
UK = 0.004348
direct = 0.0
while True:
    # GPS
    position = parsing()
    if position is None:
        pass
    elif position[0] == "$GNRMC":
        i += 1
        if position[4] == "V":
            print("Parsing Number({})".format(i))
            print("Parsing Failed")
            dcmotor.ChangeDutyCycle(7.5)
        elif position[4] == "A":
            print("Parsing Number({})".format(i))
            print("latitude : {}\tlongitude : {}\tship direction : {}".format(position[1], position[2], position[3]))
            dcmotor.ChangeDutyCycle(8)
            # Movement
            if position[3] == "":
                pass
            else:
                position[1] = float(position[1])
                position[2] = float(position[2])
                position[3] = float(position[3])
                if ps == (n+1):
                    print("Mission Completed")
                    break
                elif (latitude[ps] - 0.0011) < position[1] < (latitude[ps] + 0.0011) and (longitude[ps] - 0.0011) < position[2] < (longitude[ps] + 0.0011) :
                    ps += 1
                    print("Position Change Completed")
                    pass
                else:
                    print("Position : ", position)
                    print("direct : ", direct)
                    print("Position Coefficient(ps) : {}".format(ps))
                    # The position of the ship in the 1st quadrant
                    if (longitude[ps]) < (position[2]) and (latitude[ps]) < (position[1]) :
                        difference = (270 - m.atan((position[1] - latitude[ps])/(position[2] - longitude[ps]))) - position[3]
                        direct = difference*UK
                        svmotor.ChangeDutyCycle(7.5 + direct)

                    # The position of the ship in the 2nd quadrant
                    elif position[1] > latitude[ps] and position[2] < longitude[ps] :
                        difference = (90 + m.atan((position[1] - latitude[ps])/(longitude[ps] - position[2]))) - position[3]
                        direct = difference*UK
                        svmotor.ChangeDutyCycle(7.5 + direct)

                    # The position of the ship in the 3rd quadrant
                    elif position[1] < latitude[ps] and position[2] < longitude[ps] :
                        difference = (90 - m.atan((latitude[ps] - position[1])/(longitude[ps] - position[2]))) - position[3]
                        direct = difference*UK
                        svmotor.ChangeDutyCycle(7.5 + direct)

                    # The position of the ship in the 4th quadrant
                    elif position[1] < latitude[ps] and position[2] > longitude[ps]  :
                        difference = (270 + m.atan((latitude[ps] - position[1])/(position[2] - longitude[ps]))) - position[3]
                        direct = difference*UK 
                        svmotor.ChangeDutyCycle(7.5 + direct)

#GPIO Cleanup
cleanup = GPIO.cleanup()
cleanup
