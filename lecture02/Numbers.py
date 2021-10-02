import math

number = int(input("Введите число от 0 до 99: "))

first_list = ["ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
teen_list = ["десять","одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
tens_list =["двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто"]


if number <= 9:
    print(first_list[number].capitalize())
elif number >= 10 and number <= 19:
    tens = number % 10
    print(teen_list[tens].capitalize())
elif number > 19 and number <= 99:
    ones = math.floor(number/10)
    duos = ones - 2
    tens = number % 10
    if tens == 0:
        print(tens_list[duos].capitalize())
    elif tens != 0:
        print(tens_list[duos].capitalize() + " " + first_list[tens])