# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 17:44:43 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import time

LED_PIN=18
BUTTON_PIN=25

def configurar_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN,GPIO.IN)

def leer_boton():
    return GPIO.input(BUTTON_PIN)

def encender_led():
    GPIO.output(LED_PIN, True)

def apagar_led():
    GPIO.output(LED_PIN,False)
def loop():
    while True:
        if leer_boton():
            apagar_led()
        else:
            encender_led()
        time.sleep(0.1)

configurar_gpio()
loop()