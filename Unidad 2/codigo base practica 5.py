# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:20:21 2025

@author: ke802
"""

import telebot
import RPi.GPIO as GPIO
import Adafruit_DHT

TOKEN = "TU_TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

GPIO.setmode(GPIO.BCM)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)
sensor = Adafruit_DHT.DHT11
sensor_pin = 4

@bot.message_handler(commands=['led_on'])
def led_on(message):
    GPIO.output(LED_PIN, GPIO.HIGH)
    bot.reply_to(message, "LED encendido")

@bot.message_handler(commands=['led_off'])
def led_off(message):
    GPIO.output(LED_PIN, GPIO.LOW)
    bot.reply_to(message, "LED apagado")
    @bot.message_handler(commands=['status'])
def status(message):
    humedad, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)
    if humedad is not None and temp is not None:
        bot.reply_to(message, f"Temp: {temp}°C, Humedad: {humedad}%")
    else:
        bot.reply_to(message, "Error al leer el sensor")

bot.polling()