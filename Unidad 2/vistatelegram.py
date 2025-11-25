# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 20:25:36 2025

@author: ke802
"""

def mensaje_led_encendido():
    return "LED encendido"

def mensaje_led_apagado():
    return "LED apagado"

def mensaje_sensor(temp, humedad):
    return f"Temp: {temp}°C, Humedad: {humedad}%"

def mensaje_error_sensor():
    return "Error al leer el sensor"