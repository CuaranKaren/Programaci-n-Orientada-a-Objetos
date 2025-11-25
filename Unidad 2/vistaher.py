# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:02:00 2025

@author: ke802
"""

class View:

    @staticmethod
    def enviar_mensaje(bot, chat_id, mensaje):
        bot.send_message(chat_id, mensaje)

    @staticmethod
    def respuesta_robot_constructor():
        return "Robot Constructor trabajando... LED parpadeando."

    @staticmethod
    def respuesta_robot_explorador_activo():
        return "Robot Explorador: Exploracion activa. LED verde encendido."

    @staticmethod
    def respuesta_robot_explorador_inactivo():
        return "Robot Explorador: Exploracion detenida. LED rojo encendido."

    @staticmethod
    def respuesta_robot_medico(nombre, estado, temp, hum):
        return f"""?? Robot Mdico:
Nombre: {nombre}
Estado: {estado}
Temperatura: {temp} C
Humedad: {hum}%"""