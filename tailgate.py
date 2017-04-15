#!/usr/bin/python

from sf10 import SF10
from lightingArduino import LightingArduino
import time
NUM_LEDS = 144

"""
Sets the scaling for the leds
"""
def scale(lower, upper, number):
    number = ((number - lower)*NUM_LEDS) / (upper - lower)
    if number < 0:
        number = 0
    return number

laser = SF10()
lights = LightingArduino(NUM_LEDS)
oldMeters = 0

while(True):
    #get a laser value
    meters = laser.getMeters()

    if meters != oldMeters:
        oldMeters = meters

        #scale the value to the number of lights we want to turn on
        numLights = int(scale(1.0, 10, meters))
        numLights = NUM_LEDS - numLights

        if numLights < 0:
            numLights = 0
        if numLights > NUM_LEDS:
            numLights = NUM_LEDS

        print(meters, numLights)

        #send that to the arduino
        print lights.sendMessage(numLights)
