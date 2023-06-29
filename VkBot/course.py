import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'lxml')


def get_course(valute_name):
    name = xml.find('name', string = valute_name) 
    valute_id = name.parent
    return valute_id.value.text

print(get_course('Австралийский доллар'))

