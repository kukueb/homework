import random
'''
food = ['булочки с корицей','котлетница','суши', 'шаурма', 'бургер']
rand = random.choice(food)


print('На, жри', rand)'''

'''print(random.randint(1, 100500))'''
#Цикл, который повторяется оперделённое количество раз
'''for i in range(10):
    print("Python")'''

# Цикл "пока"
'''n = 4
k = 0
while n > 0:
    n -= 1     # n = n - 1
    k += 1     # k = k + 1
print( k)'''

halfyear = []
for i in range(1, 7):
    summ = int(input(f"Ваши доходы за {i} месяц составили: " ) )
    halfyear.append(summ * 0.3)
print("Ваши накопления составят:", sum(halfyear))