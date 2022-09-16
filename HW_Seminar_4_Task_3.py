# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

print('Чтобы вывести список неповторяющихся элементов, задайте последовательность чисел!')
userList = list(map(int, input('Введите числа списка через пробел: ').split()))
print(f'Ваш список: {userList}')

# uniqueList = list(set(userList))
# a = userList - uniqueList

# print(f'Cписок неповторяющихся элементов {uniqueList} вашего списка {userList}!') # просто убирает повторения в списке

uniqueList = []

for i in range(len(userList)):
    for j in range(len(userList)):
        if i != j and userList[i] == userList[j]:
            break
    else:
        uniqueList.append(userList[i]) 



print(f'Cписок неповторяющихся элементов {uniqueList} вашего списка {userList}!')

