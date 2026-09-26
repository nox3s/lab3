"""
#Задание 1. Определение типов данных
integer = int(input("Введите целое число: "))
decimal = float(input("Введите дробное число: "))
text = input("Введите строку: ")
#Вывод типов и значений
print(f"Значение: {integer}, тип: {type(integer).__name__}")
print(f"Значение: {decimal}, тип: {type(decimal).__name__}")
print(f"Значение: {text}, тип: {type(text).__name__}")

#Задание 2. Арифметические операции
#Ввод данных
a = float(input("Введите первое число: ")) 
b = float(input("Введите второе число: "))
#Вычисление и вывод результатов
print(f"Сумма: {a + b}")
print(f"Разность: {a - b}")
print(f"Произведение: {a * b}")
print(f"Частное: {a / b}")
print(f"Целая часть от деления: {a // b}")
print(f"Остаток от деления: {a % b}")
print(f"Возведение в степень: {a ** b:.2f}")"""

#Задание 3. Преобразование секунд в часы:минуты:секунды
#Ввод данных
total_seconds = int(input("Введите количество секунд: "))
#Преобразование секунд в часы, минуты и секунды
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
#Вывод результата
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

#Дополнительное задание. Обратное преобразование из часов:минут:секунд в секунды
#Ввод данных
time_input = input("Введите время в формате ЧЧ:ММ:СС -> ")
#Разделение строки на часы, минуты и секунды
hours_str, minutes_str, seconds_str = time_input.split(':')
#Преобразование строк в целые числа
hours = int(hours_str)
minutes = int(minutes_str) 
seconds = int(seconds_str)
#Преобразование в секунды
total_seconds = hours * 3600 + minutes * 60 + seconds
#Вывод результата
print(f"Общее количество секунд: {total_seconds}")
