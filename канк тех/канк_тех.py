import math

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Ошибка: деление на ноль")
    return x / y

def exponentiation(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Ошибка: извлечение квадратного корня из отрицательного числа")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Ошибка: факториал отрицательного числа не определен")
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: некорректный ввод числа")

def get_menu_choice():
    print("Меню:")
    print("1. Вычитание")
    print("2. Умножение")
    print("3. Деление")
    print("4. Возведение в степень")
    print("5. Квадратный корень")
    print("6. Факториал")
    print("7. Синус")
    print("8. Косинус")
    print("9. Тангенс")
    print("0. Выход")
    choice = input("Выберите операцию (0-9): ")
    return choice

while True:
    choice = get_menu_choice()

    if choice == "0":
        break

    try:
        if choice in ["1", "2", "3", "4"]:
            x = get_float_input("Введите первое число: ")
            y = get_float_input("Введите второе число: ")

            if choice == "1":
                result = subtraction(x, y)
                print("Результат:", result)
            elif choice == "2":
                result = multiplication(x, y)
                print("Результат:", result)
            elif choice == "3":
                result = division(x, y)
                print("Результат:", result)
            elif choice == "4":
                result = exponentiation(x, y)
                print("Результат:", result)

        elif choice in ["5", "6", "7", "8", "9"]:
            x = get_float_input("Введите число: ")

            if choice == "5":
                result = square_root(x)
                print("Результат:", result)
            elif choice == "6":
                result = factorial(x)
                print("Результат:", result)
            elif choice == "7":
                result = sine(x)
                print("Результат:", result)
            elif choice == "8":
                result = cosine(x)
                print("Результат:", result)
            elif choice == "9":
                result = tangent(x)
                print("Результат:", result)

        else:
            print("Ошибка: некорректный выбор операции")
    except ValueError as e:
        print(str(e))
