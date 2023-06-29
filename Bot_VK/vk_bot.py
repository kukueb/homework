import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from course import get_course
from wiki import get_wiki_article
import requests


token = "vk1.a.rDtakXd_bdWRm6zmTiyDotrtoyhrvgtgJTHXFqRm5NO7qWXrqR7z7aW6RDN0E9kdaNEjSqLgOKJeVBUY3eJbFew0RTYepiJJk7pS6KS9EkEaFsHmNFi3NIkW7Fl8q2z0jVIKWPmWIPQVWCztOrcSfbcA_5FKOJOY1Pz9xsFtthSHhnXaQps1A3Nkd4xY2ZPOVSsUA1oAGqW3alp-oeZmWw"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id

        random_id = random.randint(1, 10 ** 10)
        if msg.startswith("-к"):
            valute_name = event.text.strip('-к ')
            response = f'Курс валюты {valute_name}: {get_course(valute_name)}'
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)
        elif msg.startswith('-в'):
            article = msg[2:]
            response = get_wiki_article(article)
        elif msg == 'планеты':
            url = 'https://swapi.dev/api/planets/'
            response_url = requests.get(url)
            data = response_url.json()
            planets_list = data['results']
            planet_with_max_diameter = max(planets_list, key=lambda planet: int(planet['diameter']))
            response = f"Планета с наибольшим диаметром: {planet_with_max_diameter['name']}"
        elif msg == 'корабли':
            url = 'https://swapi.dev/api/starships/'
            response_url = requests.get(url)
            data = response_url.json()
            starships_list = data['results']
            # Фильтруем корабли, исключая те, у которых значение max_atmosphering_speed равно "n/a"
            filtered_starships = filter(lambda starship: starship['max_atmosphering_speed'] != "n/a", starships_list)   
            fastest_starship = max(filtered_starships, key=lambda starship: starship['max_atmosphering_speed'])
            response = f"Самый быстрый корабль: {fastest_starship['name']}"
        else:
            response = "Неизвестная команда"

        vk.messages.send(user_id=user_id, random_id=random_id, message=response)
