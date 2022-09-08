# Задача про Орлы и Решки.

print('Для подсчета наибольшего количества выпавших Решек ПОДРЯД введите строку текста, состоящую из букв русского алфавита "О" и "Р". Буква "О" - соответствует выпадению Орла, а буква "Р" - соответствует выпадению Решки.')
listOorP = input(("Введите Орлы и Решки: "))

count = 0
max = 0
for i in range(len(listOorP)):
    if listOorP[i] == 'Р':
        count += 1
    if listOorP[i] == 'р':
        count += 1
    if count > max:
        max = count
    if i + 1 < len(listOorP):
        if listOorP[i + 1] == 'О':
            count = 0
        if listOorP[i + 1] == 'о':
            count = 0
print(f'Наибольшее количество выпавших Решек ПОДРЯД: {max}')