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