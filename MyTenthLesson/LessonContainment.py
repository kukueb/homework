'''
class Human:
    name = 'Ivan'
    hair_color = 'red'
    height = 190
    weight = 90

human_object = Human()
print(dir(Human))

class Human:
    def __init__(self, name, hair_color, height, weight):
        self.name = name
        self.hair_color = hair_color
        self.height = height
        self.weight = weight
human_1 = Human('ivan', 'black', 190, 90)
print(human_1.name)
human_1.name = 'Alex'
human_1.height = 4000

print(human_1.name)

class A:
    def one(self):
        print(1)
    def two(self):
        print(2)
class B(A):
    def two(self):
        print('two')
    def three(self):
        print(3)

print('B')
b = B()
b.one()
b.two()
b.three()

print('A')
a = A()
a.one()
a.two()
a.three()
'''
import random


class Tank:
    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health
    def print_info(self):
        print(f'Модель танка {self.model}, имеет {self.armor} брони, при {self.health}, урон {self.damage}')
    def damage_taken(self, enemy_damage):
        self.health -= enemy_damage
        print(f"\n{self.model}:\nПо экипажу {self.model} попали, у нас осталось {self.health} здоровья")
    def shot(self, enemy):
        if self.health <= 0 or self.damage >= self.damage:
            self.health = 0
            print(f'Экипаж танка {self.model} уничтожен, гг вп.')
        else:
            enemy.health_down(enemy.damage)
            print("Точно в цель! У противника осталось")