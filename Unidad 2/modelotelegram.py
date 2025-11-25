# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 20:24:46 2025

@author: ke802
"""

import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

sensor = Adafruit_DHT.DHT11
sensor_pin = 4

def encender_led():
    GPIO.output(LED_PIN, GPIO.HIGH)

def apagar_led():
    GPIO.output(LED_PIN, GPIO.LOW)

def leer_sensor():
    humedad,temp = Adafruit_DHT.read_retry(sensor, sensor_pin)
    return humedad, temp