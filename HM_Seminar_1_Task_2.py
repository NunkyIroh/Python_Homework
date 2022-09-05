# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Чтобы узнать является ли утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинным введите значение предикат! ')
x = float(input('Введите значение X: '))
y = float(input('Введите значение Y: '))
z = float(input('Введите значение Z: '))

leftSide = not (x or y or z)
rightSide = not x and not y and not z
result = leftSide == rightSide

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')