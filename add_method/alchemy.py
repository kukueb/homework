from tkinter import *
from random import randint


window = Tk()
window.geometry('600x600')

class Lightning:
    image = PhotoImage(file='lightning.png').subsample(4,4)

class Steam:
    image = PhotoImage(file='steam.png').subsample(4,4)

class Clay:
    image = PhotoImage(file='clay.png').subsample(4, 4)

class Fire:
    image = PhotoImage(file="fire.png").subsample(4, 4)
    
    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Wind):
            return Lightning()

class Water:
    image = PhotoImage(file='water.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Clay()
    
class Earth:
    image = PhotoImage(file='earth.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay()
    
class Wind:
    image = PhotoImage(file='wind.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Wind):
            return Lightning()
        
canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Fire(), Earth(), Water(), Wind()]


for elem in elements:
    img = canvas.create_image(randint(50, 550),randint(50, 550), image = elem.image)

def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)

    if len(images_id) == 2:
        elem_id_1, elem_id_2 = images_id[0], images_id[1]
        element_1 = elements[elem_id_1 - 1]
        element_2 = elements[elem_id_2 - 1]

        new_element = element_1 + element_2
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image = new_element.image)
                elements.append(new_element)
    canvas.coords(images_id, event.x, event.y)


window.bind('<B1-Motion>', move)

window.mainloop()