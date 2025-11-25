# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 19:55:31 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class LED:
    def _init_(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)


class Button:
    def _init_(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def pressed(self):
        return GPIO.input(self.pin) == GPIO.LOW

class Controller:
    def _init_(self, led, button):
        self.led = led
        self.button = button

    def run(self):
        while True:
            if self.button.pressed():
                self.led.on()
            else:
                self.led.off()
            time.sleep(0.02)