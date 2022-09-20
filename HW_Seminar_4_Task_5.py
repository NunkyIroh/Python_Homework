# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


def sumPoly (polinomial1, polinomial2):
    for i in range(len(polinomial1)):
        for j in polinomial2:
            if polinomial1[i][1] == j[1]:
                polinomial1[i] = ((polinomial1[i][0] + j[0], polinomial1[i][1]))
                polinomial2.remove(j)
    sum = polinomial1 + polinomial2
    for i in sum:
        if i[0] == 0:
            sum.remove(i)
    sum = sorted(sum, key=lambda num: num[1])
    sum.reverse()
    return sum

with open("poly1.txt", "r") as f:
    M1 = []
    i = 0
    for line in f:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()
            if ln != '':
                num = int(ln)
                lst = lst + [num]
        M1 = M1 + [lst]
print("M1 = ", M1)


with open("poly2.txt", "r") as f2:
    M2 = []
    i = 0
    for line in f2:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()
            if ln != '':
                num = int(ln)
                lst = lst + [num]
        M2 = M2 + [lst]
print("M2 = ", M2)

res = open('sumPoly.txt', 'w')

result = sumPoly(M1, M2)

print(f'Сумма многочленов в виде списка кортежей: {result}')
res.write(str(result))

f.close()
f2.close()
res.close()

# ffile1 = open('file1.txt', 'r')
# ffile2 = open('file2.txt', 'r')
# ffile3 = open('file3.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):
#     if file1[i-1] != '^':
#         if file1[i].isnumeric():
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close


# import random
# def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
#     if b > 0:
#         res += '+' + str(b) + '*x'
#     if c > 0:
#         res += '+' + str(c)
#     return f'{a}*x^2' + res

# def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
#     if b > 0:
#         res += '+' + str(b) + '*x'
#     if c > 0:
#         res += '+' + str(c)
#     return f'{a}*x^2' + res

# f = open('dz40.txt', 'w')
# f.write(nmnogochlen1())
# print(nmnogochlen1())
# f.close()

# f = open('dz41.txt', 'w')
# f.write(nmnogochlen2())
# print(nmnogochlen2())
# f.close()

# f = open('dz40.txt', 'r')
# list_5 = str(f.readline()).split('x')
# c1 = b1 = a1 = 0
# if len(list_5) == 3:
#     c1 = list_5[2][1:]
# if len(list_5) >= 2:
#     b1 = list_5[1][3:-1]
# a1 = list_5[0][:-1]
# f.close()

# f = open('dz41.txt', 'r')
# list_51 = str(f.readline()).split('x')
# c2 = b2 = a2 = 0
# if len(list_51) == 3:
#     c2 = list_51[2][1:]
# if len(list_51) >= 2:
#     b2 = list_51[1][3:-1]
# a2 = list_51[0][:-1]
# f.close()

# f = open('dz42.txt', 'w')
# f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# f.close()