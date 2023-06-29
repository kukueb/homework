import requests
from bs4 import BeautifulSoup
from datetime import datetime


url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

today = datetime.today()
today = today.strftime('%d/%m/%Y')

payload = {'date_req' : today}

response = requests.get(url, params=payload) #  Это только подключение к сайту

xml = BeautifulSoup(response.content, 'html.parser')

def getCourse(id):
    return xml.find('valute', {'id': id}).value.text

print(getCourse('R01235'), 'рублей за 1 доллар США')
print(getCourse('R01239'), 'рублей за 1 евро')
print(getCourse('R01565'), 'рублей за 1 Польский злотый')
