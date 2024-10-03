day = int(input("Введите день: ")) # Запрашиваем ввод числа дня.
month = int(input("Введите месяц(числом): ")) # Запрашиваем ввод числа месяца.
if month<1 or month>12: # Проверяем на корректный месяц.
    print("Ошибка месяца") # Выводим что у нас некорректный месяц.
elif day<1 or day>31: # Проверяем на корректный день.
    print ("Некорректный день")
else:
    if (month == 3 and day >= 1) or (month == 4) or (month == 5 and day <= 31):
        season = "Весна" # Присваиваем сезон "Весна".
    elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 8 and day <= 31):
        season = "Лето" # Присваиваем сезон "Лето".
    elif (month == 9 and day >= 1) or (month == 10) or (month == 11 and day <= 30): 
        season = "Осень" # Присваиваем сезон "Осень".
    else: 
        season = "Зима" # Присваиваем сезон "Зима".
    print(f"Это: {season}") 
