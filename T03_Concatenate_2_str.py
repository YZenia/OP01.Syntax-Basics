def main():
    print("Добро пожаловать в ХОРРОР ВЕСЕЛУЮ программу!")
    print("Эта программа соберет две строки вместе, создавая что-то ужасное и веселое!\n")

    # Запрос пользователю двух строк для конкатенации
    string1 = input("Введите первую строку (например, 'котенок'): ")
    string2 = input("Введите вторую строку (например, 'зомби'): ")

    # Конкатенация строк (объединение строк)
    horror_string = string1 + string2 + "!"

    # Вывод результирующей строки
    print("\nДа здравствует монстр из вашего кошмара:")
    print(horror_string)
    print("Не бойтесь, он больше болтается, чем кусается!")

if __name__ == "__main__":
    main()
