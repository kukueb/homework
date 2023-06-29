class User:
    def __init__(self,name, health, damage):
        self.health = health
        self.damage = damage
        self.name = name
    def damage_take(self, enemy_damage):
        self.health -= enemy_damage
        print(f'Персонажа {self.name} поразили на {enemy_damage}, у него осталось {self.health} здоровья')
    def damage_deal(self, enemy):
        if enemy.health <= 0 or self.damage >= self.health:
            self.health = 0
            print(f'Персонаж {enemy.name} был повержен.')
        else:
            enemy.damage_take(self.damage)

user1 = User('Анатолий', 100, 30)
user2 = User('Олежа', 300, 25)

for i in range(5):
    user2.damage_deal(user1)
