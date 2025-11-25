# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 20:58:19 2025

@author: ke802
"""

import datetime

class LogModel:
    FILE = "log.txt"

    @staticmethod
    def escribir(mensaje: str):
        tiempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LogModel.FILE, "a") as f:
            f.write(f"[{tiempo}] {mensaje}\n")

    @staticmethod
    def leer():
        try:
            with open(LogModel.FILE, "r") as f:
                return f.read()
        except FileNotFoundError:
            return ""