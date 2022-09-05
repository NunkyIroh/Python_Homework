# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Чтобы узнать диапазон возможных координат точек в четверти (x и y) введите номер четверти! ')
numderQuarter = float(input('Введите номер четверти: '))

if (numderQuarter == 1):
    print ('x > 0 и y > 0')
elif (numderQuarter == 2):
    print ('x < 0 и y > 0')
elif (numderQuarter == 3):
    print ('x < 0 и y < 0')
elif (numderQuarter == 4):
    print ('x > 0 and y < 0')
else:
    print ('Введены некорректные данные!')