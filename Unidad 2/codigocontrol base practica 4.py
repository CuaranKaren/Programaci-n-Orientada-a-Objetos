# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:18:04 2025

@author: ke802
"""

from modelo.dispositivos import Led
from vista.consola import mostrar_estado
import time

led = Led(18)

try:
    while True:
        led.encender()
        mostrar_estado("LED encendido")
        time.sleep(2)
        led.apagar()
        mostrar_estado("LED apagado")
        time.sleep(2)
except KeyboardInterrupt:
    print("Finalizando...")