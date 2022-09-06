# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

print('Чтобы задать список из n чисел последовательности (1+1/n)^n и вывести их сумму на экран:')

n = int(input("Введите размер списка: ")) 
a = []
sumElements = 0

for i in range(n):  
    new_element = ((1+1/(i+1))**(i+1))
    a.append(new_element)
print(f'Ваш список: {a}')

sumElements = sum(a)
print(f'Сумма Вашего списока: {sumElements}')