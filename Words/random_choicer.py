import random
import words_data

eng_words = words_data.eng_words
rus_words = words_data.rus_words


def work():
    pre_word_index = ""
    answer = 123
    while answer != 0:
        word_index = random.randrange(0, len(eng_words))
        if word_index == pre_word_index:
            break
        answer = input(f'Как переводится слово {eng_words[word_index]}: ')
        if answer == rus_words[word_index]:
            print('Да, это верно')
        elif answer == '':
            exit()
        else:
            print(f'Нет, верно {rus_words[word_index]}')
        pre_word_index = word_index
work()