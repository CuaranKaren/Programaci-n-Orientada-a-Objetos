# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:14:15 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 18
BUTTON_PIN = 23
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def encender_led():
    GPIO.output(LED_PIN, GPIO.HIGH)

def apagar_led():
    GPIO.output(LED_PIN, GPIO.LOW)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            encender_led()
        else:
            apagar_led()
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()