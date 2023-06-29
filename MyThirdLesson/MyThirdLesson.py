'''actor = input('Введите имя актёра: ')
rating = int(input('Введите желаемый рейтинг фильма: '))
my_favor = 'ева элфи'
actor.lower()

if actor == my_favor and rating > 7:
    print('Заходи на сайт, смотри быстрее!')
elif actor == my_favor or rating > 7:
    print('Ну, можешь конечно глянуть...')
else:
    print('Миша, иди домой.')'''

import random

computer_int = random.randint(1, 10)
player_int = int(input('Угадайте, какое я загадал число от 1 до 10: '))

diff = computer_int - player_int

if computer_int == player_int:
    print('Красавчик, вообще лучший')
elif diff == 1 or -1 :
    print('Вай, почти, а число то было:', computer_int)
else:
    print('Ну ты и лох конечно, число вообщето было:', computer_int)