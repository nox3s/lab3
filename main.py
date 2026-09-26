integer = int(input("Введите целое число: "))
decimal = float(input("Введите дробное число: "))
text = input("Введите строку: ")
#Вывод типов и значений
print(f"Значение: {integer}, тип: {type(integer).__name__}")
print(f"Значение: {decimal}, тип: {type(decimal).__name__}")
print(f"Значение: {text}, тип: {type(text).__name__}")