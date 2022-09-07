# Реализуйте алгоритм перемешивания списка.


import random

N = int(input("Введите размер списка: "))
a = []

for i in range(N):
    new_element = random.randint(-N, N)
    a.append(new_element)
print(f'Ваш список: {a}')

random.shuffle(a)
print(f'Ваш перемешанный список: {a}')
