# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Чтобы получить набор произведений цифр в числе введите в натуральное число N:')
# N = int(input('N = '))

# sum = 1
# for i in range(N):
#     sum = sum * (i + 1)
#     print(sum, end=" ")

from math import factorial

n = int(input('Введите число N: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
listN = list( f(i) for i in range(1, n +1))
print(listN)