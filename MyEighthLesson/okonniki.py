from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

root = Tk()
root.title('Курс валют')
root.geometry('400x350+300+300')

root.resizable(0, 0)

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today()
today = today.strftime('%d/%m/%Y')

payload = {'date_req' : today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'html.parser')

def getCourse(id):
    return xml.find('valute', {'id':id}).value.text
img_bank = PhotoImage(file='bank.png')
bank = Label(root, image=img_bank)
bank.place(x=0, y=0)


lab = Label(root, text='Курс валют \n классного банка', fg='#3cae33',bg='white', font='Veranda 20' )
lab.place(x=100, y=15)
course_info = Label(root, text=f'Курс на '+today.replace('/','.'),font= 'Veranda',bg='white', fg='#3cae33')
course_info.place(x=80,y=325)
usd_course = Label(root, text='USD: '+getCourse('R01235'), font='Veranda',bg='white', fg='#3cae33')
usd_course.place(x=260 ,y=305)

cny_course = Label(root, text='CNY: '+getCourse('R01375'), font='Veranda',bg='white', fg='#3cae33')
cny_course.place(x=260 ,y=325)

root.mainloop()