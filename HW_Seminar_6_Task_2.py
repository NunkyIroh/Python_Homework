# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

print('Чтобы получить сумму цифр в числе введите в число N:')
str_N = input('N = ')

import re
str_N1 = re.sub(r'[.,]', '', str_N)

print(f'Сумма чисел введенного Вами числа {str_N} -> {sum(map(int, str(str_N1)))}')