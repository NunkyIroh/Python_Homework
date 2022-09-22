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

# b = [1, 1, 2, 3, 3, 4, 5]
#  a = []
#  for i in b:
#     if b.count(i) == 1:
#          a.append(i)



# inp = list(map(int, input('Insert numbrers: ').split()))
# print(set(inp))

# a= [1,2,2,2,2,3,1,4]
# print(set(a))