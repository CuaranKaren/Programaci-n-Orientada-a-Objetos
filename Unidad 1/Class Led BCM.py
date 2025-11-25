# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 17:51:08 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class LED:
    def _init_(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def prender(self):
        GPIO.output(self.pin, True)

    def apagar(self):
        GPIO.output(self.pin, False)

    def parpadear(self, intervalo=1):
        self.prender()
        time.sleep(intervalo)
        self.apagar()
        time.sleep(intervalo)
led = LED(18)

while True:
    led.parpadear(1)