'''english_dict = {'яблоко': "apple",'молоко' :'milk','кот' :'cat', 'котёнок': 'kitty'}
word = input('Введите слово: ').lower()
if word in english_dict:
    print(word, "на английском будет:", english_dict[word])
else:
    print('Такого слова в словаре нет... Вы обосрались.')
'''
'''favorite_actor = input('Актёр может быть? ').lower()
film = input('Введите фильм: ').lower()
films = {
    'матрица': 'киану ривз',
    'гарри поттер': "дэниел рэдклифф",
    "фантастические твари": "эдди редмэйн"
}

if film in films and favorite_actor == films[film]:
    print('Смотри скорее, блин, слоупочник.')
elif film in films:
    print('Ну можешь глянуть, но лучше не надо...')
else:
    print("Я даже таково фильма не знаю")'''

file = open('testfile.txt', 'r' )
for line in file.readlines():
    print(line)


file.close()

