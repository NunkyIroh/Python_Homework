# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print('Чтобы найти произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Задайте список из нескольких чисел.')
a = list(map(int, input('Введите числа списка через пробел: ').split()))
print(f'Ваш список: {a}')

b = []
for i in a:
    ans = a[::len(a)-1]
    a.pop(0)
    a.pop(len(a)-1)
    b = b + [ans[0]*ans[1]]

if len(a) >= 1:
    print(f'произведение пар чисел списка: {b+[a[0]*a[0]]}')
