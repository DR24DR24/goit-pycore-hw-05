import typing
#from typing import Callable


def caching_fibonacci()->typing.Callable[[int], int]:
    #Створити порожній словник cache
    cache: typing.Dict[int, int]={0:0,1:1} #Якщо n == 1, повернути 1
    def fibonacci(n:int)->int:
        nonlocal cache
        if n<0:           # Якщо n <= 0, повернути 0
            return 0
        if n not in cache:#Якщо n у cache, повернути cache[n]
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]#Повернути cache[n]
    
    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(-9))  # Виведе 0
print(fib(0))  # Виведе 0
print(fib(1))  # Виведе 1
print(fib(2))  # Виведе 1
print(fib(15))  # Виведе 610