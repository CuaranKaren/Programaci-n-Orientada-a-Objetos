# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:15:14 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Dispositivo:
    def __init__(self, pin):
        self.pin = pin

class Led(Dispositivo):
    def __init__(self, pin):
        super().__init__(pin)
        GPIO.setup(self.pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)
        import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Dispositivo:
    def __init__(self, pin):
        self.pin = pin

class Led(Dispositivo):
    def __init__(self, pin):
        super().__init__(pin)
        GPIO.setup(self.pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)