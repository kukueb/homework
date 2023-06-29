import random
choices = []
a = int(input("Введите количество выборочных элементов: "))
for i in range(a):
    choices.append(input(f"Введите {i + 1} выбор: "))
    if choices[i] == "" or choices[i] == " ":
        choices.pop(i)
        break

print(random.choice(choices))
