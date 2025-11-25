# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:17:34 2025

@author: ke802
"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)