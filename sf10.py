#!/usr/bin/python

import serial
import serial.tools.list_ports

class SF10:
    def __init__(self):
        self.connected = False
        self.connection = None

        #look for the sf10 and open the connection
        ports = serial.tools.list_ports.comports()
        laserID = "FT230X Basic UART" #this is a dumb way to look for the laser.
        for port in ports:
            if laserID in port.description:
                self.connection = serial.Serial(port=port.device, baudrate=115200)
                self.connected = True

    #get the latest data
    def read(self):
        data = ""
        if self.connected:
            data = self.connection.readline()
        return data

    def getMeters(self):
        inString = self.read()
        output = -1
        if inString != "":
            try:
                output = float(inString.split("m")[0].strip())
            except ValueError:
                output = -1
        return output

    #close the connection
    def close(self):
        if self.connected:
            self.connection.close()
            self.connected = False


if __name__ == "__main__":
    laser = SF10()
    laser.read()
    while laser.connected:
        reading = laser.getMeters()
        print(reading)
