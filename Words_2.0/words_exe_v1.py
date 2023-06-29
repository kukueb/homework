import random

words = {
'coward': 'трус' ,
'frown':'хмуриться' ,
'slightest': 'малейший',
'sob':'всхлипывать' ,
'exclaime':'восклицать' ,
'twinkle': 'блестеть',
'chatter': 'болтать',
'scold':'ругать' , 
'tight':'крепко' ,
'stroke': 'гладить',
'tease' : 'дразнить',
'beg': 'просить',
'behave':'вести себя',
'crowd':'толпа',
'urgent':'срочный',
'provide':'предоставлять'
}

def ordered():
    
    for i in range(len(words)):
        words_keys = list(words)
        word = words_keys[i]
        answer = input(f'Как переводится слово {word}: ').lower()
        if answer == words[word]:
            print('Верно!')
        elif answer == '':
            exit()
        else:
            print('Неверно, а правильный ответ был:', words[word])

def random_test():
    random_word = "1"
    pre_word = "asdasdasd"
    while True:
        random_word = random.choice(list(words))
        if pre_word == random_word:        
            break
        answer = input(f'Как переводится слово {random_word}: ').lower()
        if answer == words[random_word]:
            print('Верно!')
        elif answer == "":
            exit()
        else:
            print('Неверно, а правильный ответ был:', words[random_word])
        pre_word = random_word
print('Какой режим используем? \n 1 - Случайный \n 2 - Проход по списку')

choice = int(input())

if choice == 1:
    user_choice = random_test()
elif choice == 2:
    user_choice = ordered()

user_choice