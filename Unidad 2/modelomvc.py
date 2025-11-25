# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 20:06:20 2025

@author: ke802
"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Led:
    def _init_(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)


class Boton:
    def _init_(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def esta_presionado(self):
        return GPIO.input(self.pin)==GPIO.LOW