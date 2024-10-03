day = int(input("Введите день: ")) 
month = int(input("Введите месяц: ")) 
if month < 1 or month>12:
    print("Ошибка месяца")
elif day<1 or day>31: 
    print ("Некорректный день")
else:
    if (month == 3 and day >= 1) or (month == 4) or (month == 5 and day <= 31):
        elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 8 and day <= 31): 
    elif (month == 9 and day >= 1) or (month == 10) or (month == 11 and day <= 30): 
else:
    print(f"Это: {season}") 
