violator_songs = { 
    'World in My Eyes': 4.86 ,
    'Sweetest Perfection': 4.43 ,
    'Personal Jesus': 4.56 ,
    'Halo': 4.9 ,
    'Waiting for the Night': 6.07 ,
    'Enjoy the Silence': 4.20 ,
    'Policy of Truth': 4.76 ,
    'Blue Dress': 4.29 ,
    'Clean': 5.83
}
summ = 0
number_of_songs = int(input('Сколько песен? '))
for i in range(number_of_songs):
    name = input(f'Название {i + 1} песни: ')
    summ = summ + violator_songs[name]
print('Всего песни длятся', summ, 'минут.')
