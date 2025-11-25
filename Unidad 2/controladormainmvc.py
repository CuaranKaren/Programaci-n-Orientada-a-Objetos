# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 20:15:00 2025

@author: ke802
"""

from modelomvc import Led, Boton
from vistamvc import mostrar_estado
import time
import RPi.GPIO as GPIO

led = Led(18)
boton = Boton(17)

try:
    mostrar_estado("INICIO: LED parpadeará sin botón durante 10 segundos")

    tiempo_inicio = time.time()
    while time.time() - tiempo_inicio < 10:
        led.encender()
        mostrar_estado("LED encendido")
        time.sleep(1)

        led.apagar()
        mostrar_estado("LED apagado")
        time.sleep(1)

    mostrar_estado("AHORA: LED dependerá del botón durante 10 segundos")
    
    tiempo_inicio = time.time()
    while time.time() - tiempo_inicio < 10:
        if boton.esta_presionado():
            led.encender()
            mostrar_estado("Botón presionado → LED encendido")
        else:
            led.apagar()
            mostrar_estado("Botón NO presionado → LED apagado")

        time.sleep(0.2)

    mostrar_estado("Proceso finalizado.")
    led.apagar()

except KeyboardInterrupt:
    print("Interrumpido por el usuario.")