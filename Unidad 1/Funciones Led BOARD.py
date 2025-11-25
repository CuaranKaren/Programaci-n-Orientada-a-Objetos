# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 17:44:00 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

def prender_led():
    GPIO.output(12, True)

def apagar_led():
    GPIO.output(12, False)

def parpadear_led():
    prender_led()
    time.sleep(1)
    apagar_led()
    time.sleep(1)

while True:
   parpadear_led()