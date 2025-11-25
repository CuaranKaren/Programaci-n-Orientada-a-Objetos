# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:22:07 2025

@author: ke802
"""

class Logger:
    def __init__(self, archivo):
        self.archivo = archivo

    def escribir(self, mensaje):
        with open(self.archivo, 'a') as f:
            f.write(mensaje + '\n')

# Ejemplo de uso
logger = Logger("log.txt")
logger.escribir("Sistema iniciado")

# Puedes integrar esto con LED y sensor:
# logger.escribir(f"LED encendido a las {time.strftime('%H:%M:%S')}")
# logger.escribir(f"Temperatura: {temp}°C, Humedad: {hum}%")