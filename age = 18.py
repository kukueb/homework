import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Функция {func.__name__} выполнялась {run_time} секунд")
        return result
    return wrapper


@timing_decorator
def numbers_load():
    numbers_2 = [i for i in range(0, 20001, 2)]
    return 'numbers_1'
@timing_decorator
def numbers_load_2():
    numbers = []
    for i in range(0, 20001, 2):
        numbers.append(i)
    return 'numbers_2'
@timing_decorator
def numbers_load_3(val):
    numbers_3 = [i for i in range(val) if i%2 == 0]
    return 'numbers_3'
val = 20001
print(numbers_load())
print(numbers_load_2())
print(numbers_load_3(val))
