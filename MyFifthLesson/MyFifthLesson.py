import telebot
import requests
import random
from bs4 import BeautifulSoup



token = '6025944388:AAHdhW0jo7npVMfOGQXVqqKzSyKmmW6K2hY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
    welcome_text = 'Ну привет, я кстати бот, если что вообщем дааа... Да... Определённо.'
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['poem'])

def send_poem(message):
    poem_text = 'Муха села на варенье, вот и всё стихотворенье'
    bot.send_message(message.chat.id,  poem_text)


@bot.message_handler(commands=['fact'])

def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)


bot.polling()