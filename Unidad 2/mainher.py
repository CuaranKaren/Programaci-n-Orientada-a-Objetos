# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:04:10 2025

@author: ke802
"""

import telebot
from controladorhert import Controller

TOKEN = "8307770333:AAEDknqHTN2L6VtFBNqYgLQfiwAU26J5LFw"
bot = telebot.TeleBot(TOKEN)

controller = Controller(bot)

@bot.message_handler(commands=['start'])
def iniciar(message):
    controller.comando_start(message)

@bot.message_handler(commands=['constructor'])
def activar_constructor(message):
    controller.comando_constructor(message)

@bot.message_handler(commands=['explorador'])
def activar_explorador(message):
    controller.comando_explorador(message)

@bot.message_handler(commands=['medico'])
def activar_medico(message):
    controller.comando_medico(message)
@bot.message_handler(commands=['log'])
def mostrar_log(message):
    controller.comando_log(message)

print("Bot corriendo...")
bot.infinity_polling()