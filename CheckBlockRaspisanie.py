# Импорт
from re import *
from spellchecker import SpellChecker

# Создание нужных переменных
message_true = []
count_1A, count_1B, count_1G, count_1V = 0,0,0,0
#1А: count_1A
#1Б: count_1B
#1В: count_1V
#1Г: count_1G


# Определяем язык
spell = SpellChecker(language='ru')

## Справшиваем у пользователя сообщение
message_false = input("Введите слово для проверки орфографии: ").split()
print(message_false)


for i in message_false:
    print(type(i))

    # Блок проверки 1а и 1А
    if i == '1А':
        message_false.remove('1А')
        count_1A += 1
        print('count_1A',count_1A)
        print(message_false)
    elif i == '1а':
        message_false.remove('1а')
        count_1A += 1
        print('count_1A',count_1A)
        print(message_false)


# Блок проверки 1б и 1Б
    elif i == '1Б':
        message_false.remove('1Б')
        count_1B += 1
        print('count_1Б',count_1B)
    elif i=='1б':
        message_false.remove('1б')
        count_1A += 1
        print('count_1A',count_1A)
        print(message_false)


# Блок проверки 1В и 1в
    elif i == '1В':
        message_false.remove('1В')
        count_1V += 1
        print('count_1В',count_1V)
    elif i=='1в':
        message_false.remove('1в')
        count_1V += 1
        print('count_1В',count_1V)


# Блок проверки 1г и 1Г
    elif i == '1Г':
        message_false.remove('1Г')
        count_1G += 1
        print('count_1Г',count_1G)
    elif i == '1г':
        message_false.remove('1г')
        count_1G += 1
        print('count_1Г',count_1G)



    message_true += spell.candidates(i)



if count_1A == 1:
    message_true.append('1А')
    message_true.append('1а')
elif count_1B==1:
    message_true.append('1Б')
    message_true.append('1б')
elif count_1V==1:
    message_true.append('1В')
    message_true.append('1в')
elif count_1G==1:
    message_true.append('1Г')
    message_true.append('1г')

message_true = str(message_true)
print(message_true,type(message_true))




if findall('расписание',message_true) == ['расписание'] or findall('Расписание',message_true) == ['Расписание']:
    if findall('1А',message_true) == ['1А'] or findall('1а',message_true) == ['1а']:
        print("Держите расписание 1А класса")
    elif findall('1Б',message_true) == ['1Б'] or findall('1б',message_true) == ['1б']:
        print("Держите расписание 1Б класса")
    elif findall('1Г',message_true) == ['1Г'] or findall('1г',message_true) == ['1г']:
        print("Держите расписание 1Г класса")
    elif findall('1В',message_true) == ['1В'] or findall('1в',message_true) == ['1в']:
        print("Держите расписание 1В класса")
elif findall('объявление',message_true)==['объявление'] or findall('Объявление',message_true) == ['Объявление']:
    print("Вы попали в раздел Объявления школы!")

