import telebot
import openai
import os

bot = telebot.TeleBot('6221499420:AAGJby0EKGEYr95PbsUooNVoGS-josNOscQ')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])

def handle_login(message):
    print(message.text) 
    sent = bot.send_message(message.chat.id, "Введите логин :")
    bot.register_next_step_handler(sent, save_login)

def save_login(message):
   Login = message.text
   sent = bot.send_message(message.chat.id, "Введите пароль :")
   bot.send_message(message.chat.id, Login)
   bot.register_next_step_handler(sent, save_pass)
   return Login

def save_pass(message):
   Password = message.text
   return Password

@bot.message_handler(commands=["logpass"])

def message_logpass(message):
   bot.send_message(message.chat.id, save_login(message= ["text"]) )
   bot.send_message(message.chat.id, save_pass(message= ["text"])  )

bot.polling(none_stop=True, interval=0)


####    py C:\Users\User\Desktop\Python\import_telebot1.py    ####