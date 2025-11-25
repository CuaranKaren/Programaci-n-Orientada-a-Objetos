# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 17:27:41 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT) 
GPIO.setup(22, GPIO.IN)

while True:
    if GPIO.input(22):
        GPIO.output(12,False)
        
    else:
        GPIO.output(12,True)
    time.sleep(0.1)