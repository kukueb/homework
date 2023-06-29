class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other

    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, int):
            return self.price * other
        elif isinstance(other, float):
            return self.price * other

    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.price / other.price
        elif isinstance(other, int):
            return self.price / other

item_1 = Item('Видеокарта', 60000, 0.8)
item_2 = Item('Процессор', 10000, 1)

price_difference = item_1 - item_2
print(price_difference)

new_price = item_1 * 1.05
print(new_price)

price_ratio = item_1 / item_2
print(price_ratio)