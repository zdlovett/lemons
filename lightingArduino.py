#!/usr/bin/python

import serial
import serial.tools.list_ports

"""
Designed to interface to arduinos that are attached to
144 led string neo pixels.

The software sends a serial packet containing the number to of leds to
turn on.
"""
class LightingArduino:
    def __init__(self, numLEDs=0):
        self.numLEDs = numLEDs
        self.connection = None

        ports = serial.tools.list_ports.comports()
        for port in ports:
            if (port.vid == 9025 and port.pid == 66) or (port.pid == 24577 and port.vid == 1027) :
                self.connection = serial.Serial(port=port.device, baudrate=115200)

    def sendMessage(self, number):
        bytesSent = 0
        if self.connection is not None:
            if number <= self.numLEDs:
                data = str(number)
                bytesSent = self.connection.write(data + '\n')
        return bytesSent
