even = []
uneven = []
for i in range(1, 11):
    a = int(input(f'Введите число номер {i}: '))
    if a%2 == 0:
        even.append(a)
    else:
        uneven.append(a)

print('Чётные числа:', even, '\n' + 'Нечётные числа:', uneven)