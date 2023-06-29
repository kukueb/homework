import requests
from bs4 import BeautifulSoup
from datetime import datetime
import contextlib


url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'lxml')

@contextlib.contextmanager
def get_course_info(currency):
    valute_block = xml.find("valute", {'id': currency})
    course = valute_block.find('value').text
    nominal = valute_block.find('nominal').text
    valute_name = valute_block.find('name').text
    yield f'({nominal} шт.) {valute_name} стоит(ят) {course} руб.'

with get_course_info('R01010') as currency:
    print(currency)