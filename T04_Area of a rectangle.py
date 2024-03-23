def main():
    language = input("Choose your language (Выберите ваш язык) [ru/en]: ").lower()

    if language == "ru":
        print("Программа для вычисления площади прямоугольника")
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))

        # Вычисление площади
        area = length * width

        print("Площадь прямоугольника равна:", area)
    elif language == "en":
        print("Program to calculate the area of a rectangle")
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        # Calculating the area
        area = length * width

        print("The area of the rectangle is:", area)
    else:
        print("Unsupported language! (Неподдерживаемый язык!)")


if __name__ == "__main__":
    main()
