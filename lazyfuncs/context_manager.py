"""with open('text.txt', 'w') as file:
    file.write('Hello World!')
    print(file.closed)
print(file.closed)
"""
import contextlib

@contextlib.contextmanager
def str_reverse(my_str):
    print('Входим в контекстный менеджер: ')
    yield my_str[::-1]
    print('Выходим из контекстного менеджера: ')

with str_reverse('Hello world!') as str2:
    print(f'Выполняется код: {str2}')


@contextlib.contextmanager
def exc_handler(exc):
    try:
        yield True
    except exc:
        ('Произошло исключение')

with exc_handler(IndexError):
    my_l = [1, 2]
    print(my_l[3])