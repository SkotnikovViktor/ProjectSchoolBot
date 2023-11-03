from re import *
message = input()
if findall('расписание',message) == ['расписание'] or findall('Расписание',message) == ['Расписание']:
    if findall('1А',message) == ['1А'] or findall('1а',message) == ['1а']:
        print("1А")
    elif findall('1Б',message) == ['1Б'] or findall('1б',message) == ['1б']:
        print("1Б")
    elif findall('1Г',message) == ['1Г'] or findall('1г',message) == ['1г']:
        print("1Г")
    elif findall('1В',message) == ['1В'] or findall('1в',message) == ['1в']:
        print("1В")
elif findall('объявление',message)==['объявление'] or findall('Объявление',message) == ['Объявление']:
    print("Вы попали в раздел Объявления школы!")

