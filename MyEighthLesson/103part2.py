import json
import requests

url = 'https://swapi.dev/api/'
response = requests.get(url).json()

#получаем доступ к api с персонажами
people_api = response.get('people')

def check_people(url):
    #вывести информацию о 5 персонажах
    for i in range(1,6):
        response = requests.get(f'{url}/{i}').json()
        print(response)

check_people(people_api)
