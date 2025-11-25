# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:02:40 2025

@author: ke802
"""

from robotshert import RobotConstructor, RobotExplorador, RobotMedico
from modelohert import LogModel
from vistahert import View
import threading

class Controller:
    def _init_(self, bot):
        self.bot = bot

    def comando_start(self, message):
        texto = (
            "Bienvenido al Smart Robots Bot.\n"
            "Comandos:\n"
            "/constructor - Activar robot constructor\n"
            "/explorador - Activar robot explorador\n"
            "/medico - Activar robot medico\n"
            "/log - Ver logs"
        )
        View.enviar_mensaje(self.bot, message.chat.id, texto)
def comando_constructor(self, message):
        robot = RobotConstructor("Constructor")
        t = threading.Thread(
            target=self.activar_robot,
            args=(robot, message, lambda r: View.respuesta_robot_constructor())
        )
        t.start()

    def comando_explorador(self, message):
        robot = RobotExplorador("Explorador")
        t = threading.Thread(
            target=self.activar_robot,
            args=(robot, message, self.mensaje_explorador)
        )
        t.start()

    def comando_medico(self, message):
        robot = RobotMedico("Medico")
        t = threading.Thread(