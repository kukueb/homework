import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

today = datetime.today()
today = today.strftime('%d/%m/%Y')

payload = {'date_req' : today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'html.parser')



def course(valute_from, valute_to, amount):
    if valute_from != 'RUR':
        chr_from = xml.find('charcode', string = valute_from)
        valute_id_from = chr_from.parent
        value_from = float(valute_id_from.value.text.replace(',', '.'))
    else:
        value_from = 1
    chr_to = xml.find('charcode', string = valute_to) 
    valute_id_to = chr_to.parent
    value_to = float(valute_id_to.value.text.replace(',', '.'))
    return float(amount) * (value_from / value_to)


valute_from_inp = input('Из какой валюты переводим? ').upper()
valute_to_inp = input('В какую валюту переводим? ').upper()
amount = input(f'Сколько {valute_from_inp} нужно перевести? ')

print(course(valute_from_inp, valute_to_inp, amount))