from tkinter import *
import random
window = Tk()

w = 600
h = 600
window.geometry(str(w) + 'x' + str(h))

canvas = Canvas(window, width = w, height = h)
canvas.place(in_=window, x=0, y=0)

bg_photo = PhotoImage(file = 'bg_2.png')

#Класс рыцарь
class Knight:
    def __init__(self):
        #Координаты центра
        self.x = 70
        self.y = h // 2
        #Скорость движения
        self.v = 0
        self.photo = PhotoImage(file = 'knight.png')
    def up(self, event):
        self.v = -3
    def down(self, event):
        self.v = 3
    def stop(self, event):
        self.v = 0

class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100, 500)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file = 'dragon.png')

knight = Knight()

dragons = []

for i in range(3):
    dragons.append(Dragon())

def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image= knight.photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v
    dragon_to_kill = -1

    for dragon in dragons:
        dragon.x -= dragon.v

#эта строка последняя
window.mainloop()