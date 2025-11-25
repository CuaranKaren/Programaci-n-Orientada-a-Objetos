# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 20:26:01 2025

@author: ke802
"""

import telebot
import modelotel
import vistatel

TOKEN = "8307770333:AAEDknqHTN2L6VtFBNqYgLQfiwAU26J5LFw"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['led_on'])
def led_on(message):
    modelotel.encender_led()
    bot.reply_to(message, vistatel.mensaje_led_encendido())

@bot.message_handler(commands=['led_off'])
def led_off(message):
    modelotel.apagar_led()
    bot.reply_to(message, vistatel.mensaje_led_apagado())

@bot.message_handler(commands=['estado'])
def estado(message):
    humedad, temp = modelotel.leer_sensor()
if humedad is not None and temp is not None:
        bot.reply_to(message, vistatel.mensaje_sensor(temp, humedad))
  else:
        bot.reply_to(message, vistatelpy.mensaje_error_sensor())

def iniciar_bot():
    print("Bot iniciado...")
    bot.polling(none_stop=True)