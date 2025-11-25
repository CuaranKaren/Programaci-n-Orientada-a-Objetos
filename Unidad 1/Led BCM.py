# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 14:26:37 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings (False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

while True:
      GPIO.output(18,True)
      time.sleep(1)
      GPIO.output(18,False) 
      time.sleep(1)