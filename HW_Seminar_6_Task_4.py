# Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('Чтобы найти произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Задайте список из нескольких чисел.')
a = list(map(float, input('Введите числа списка через пробел: ').split()))
print(f'Ваш список: {a}')

# b =[]
# for i in a:
#     b = b + [i - (i * 10 // 10)]
# print(f'Ваш список: {b}')
# print(f'Разница между максимальным и минимальным значением дробной части элементов: {round(max(b) - min(b), 2)}')

b = list(map((lambda x: x - (x * 10 // 10)), a))
print(f'Разница между максимальным и минимальным значением дробной части элементов: {round(max(b) - min(b), 2)}')