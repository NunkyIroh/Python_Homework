# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_for_numbers(data): # для чисел, но для этого метода не придумал как восстанавливать. Ну и тут просто вывод на экран.
    string = ''
    cout = 1
    for i in range(len(string)-1):
        if i <= len(string):
            if string[i] == string[i + 1]:
                cout += 1
            else:
                a = string[i]
                print(cout, string[i])
                cout = 1
    print(cout, string[i])

def rle_encode(data): # сжатие для любых символов, но некорректно будет работать с числами
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data): # восстановление для любых символов, кромы цифр
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open("RLEencode.txt", "r") as enterFile:
    enterData = enterFile.readline()
print(f'Ваша запись во входящем файле: {enterData}')

encoded_val = rle_encode(enterData) 
print(f'Ваша запись после RLE-сжатия: {encoded_val}')

decoded_val = rle_decode(encoded_val)
print(f'Ваша запись после RLE-восстановления: {decoded_val}')

with open("RLEdecode.txt", "w") as exitFile:
    exitFile.write(decoded_val)

enterFile.close()
exitFile.close()

# смысл сжатия и восстановления проработал, сейчас на вахте времени нет, 
# поэтому если будет время подумаю как модернизировать для любых символов, 
# думаю через список кортежей или список списков.

# def Compression(text): #алгоритм сжатия
#     compresdata = ''

#     i = 0
#     while i < len(text):
#         count = 1
#         while i + 1 < len(text) and text[i] == text[i + 1]:
#             count += 1
#             i += 1
#         compresdata += str(count) + text[i]
#         i += 1
    
#     return compresdata


# def Recovery(text): #алгоритм восстановления
#     datarecovery = ''

#     i = 0
#     while i < len(text):
#         datarecovery += str(text[i+1]) * int(text[i])
#         i+=2
    
#     return datarecovery


# with open('Text1.txt', 'r') as t1:
#     t1 = t1.read()    

# with open('Text2.txt', 'w+') as t2:
#     t2.write(Compression(t1))
#     t2.seek(0)                     #возврат курсора на начало строки
#     t2 = t2.read()
 
# with open('Text3.txt', 'w') as t3:
#     t3.write(Recovery(t2))