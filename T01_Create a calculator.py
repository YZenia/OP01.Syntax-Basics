def main():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        print("Сложение:", num1 + num2)
        print("Вычитание:", num1 - num2)
        print("Умножение:", num1 * num2)
        print("Деление:", num1 / num2)
    except ValueError:
        print("Ошибка: Введите числа корректно.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")

if __name__ == "__main__":
    main()
