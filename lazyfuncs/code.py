import time

"""my_iter = [time.sleep(x) for x in range(1, 3)]

print(my_iter)

my_iter_2 = (time.sleep(x) for x in range(1, 3))

print(my_iter_2)
"""
def my_lazy(items):
    for item in items:
        yield item

def my_lazy(items):
    yield from items
    
for item in my_lazy([1, 2, 3, 4, 5]):
    print(item)

items = ['Яблоко', "Банан", "Апельсин"]

for i in my_lazy(items):
    print(i)