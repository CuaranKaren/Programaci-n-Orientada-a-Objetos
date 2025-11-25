# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 17:18:19 2025

@author: ke802
"""
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.IN)

while True:
    
      if GPIO.input(25):
          GPIO.output(18,False)
          
      else:
              GPIO.output(18,True)