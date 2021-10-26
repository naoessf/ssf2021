# import data
import serial


# get serial
gps = serial.Serial("/dev/ttyACM0", baudrate = 38400, timeout = 0.01)

def parsing():
    line = gps.readline()
    data = line.decode().split(",")
    position = []
    if data[0] == "$GNRMC":
        position.append(data[0])
        position.append(data[3])
        position.append(data[5])
        position.append(data[8])
        position.append(data[2])
        return position
