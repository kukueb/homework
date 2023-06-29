class InfiniteIterator:
    def __init__(self):
        self.current = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.current
        self.current += 1
        return result
    
for n in InfiniteIterator():
    print(n)
    if n == 100:  # Ограничу количество выводимых элементов, чтобы ПК не умер
        break