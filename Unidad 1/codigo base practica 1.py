# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:11:27 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Modo BCM
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

print("Encendiendo LED por 5 segundos...")
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(5)
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()