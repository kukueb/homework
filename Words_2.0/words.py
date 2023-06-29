import data_words
import random
import os 

words = data_words.words

def new_file():
    count_f_key = '0'
    file_name = input('Введите название базы: ')
    file = open(f'C:/Users/User/Desktop/Python/Words_2.0/{file_name}.py', 'w', encoding='utf8')
    file.write( file_name + '_words = {')
    while count_f_key != '':
        count_f_key = input('Введите слово на английском: ')
        if count_f_key == '':
            break
        count_f = input('Введите перевод на русский: ')
        file.write(f'"{count_f_key}":"{count_f}",')
    file.write('}')
    file.close()
    

def ordered():
    answer = '2'
    for i in range(len(words)):
        words_keys = list(words)
        word = words_keys[i]
        answer = input(f'Как переводится слово {word}: ')
        if answer == words[word]:
            print('Красава')
        elif answer == '':
            exit()
        else:
            print('Неверно, а ведь правильный ответ был:', words[word])


def random_test():
    random_word = "1"
    pre_word = "asdasdasd"
    answer = '2'
    while answer != '0':
        random_word = random.choice(list(words))
        if pre_word == random_word:        
            break
        answer = input(f'Как переводится слово {random_word}: ')
        if answer == words[random_word]:
            print('Верно!')
        elif answer == "":
            exit()
        else:
            print('Неверно, а правильный ответ был:', words[random_word])
        pre_word = random_word
print('Какой режим используем? \n 1 - Случайный \n 2 - Проход по списку \n 3 - Создать новый файл')

choice = int(input())

if choice == 1:
    user_choice = random_test()
elif choice == 2:
    user_choice = ordered()
elif choice == 3:
    user_choice = new_file()
user_choice