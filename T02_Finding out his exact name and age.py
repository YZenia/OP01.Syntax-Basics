from datetime import datetime


def calculate_age_in_months(age):
    return age * 12


def calculate_age_in_days(age):
    return age * 365 + age // 4 - age // 100 + age // 400


def calculate_age_in_hours(age):
    return age * 365 * 24 + age // 4 * 24 - age // 100 * 24 + age // 400 * 24


def get_birth_datetime():
    birth_year = int(input("Введите год вашего рождения (например, 1990): "))
    birth_month = int(input("Введите месяц вашего рождения (число от 1 до 12): "))
    birth_day = int(input("Введите день вашего рождения (число от 1 до 31): "))
    birth_hour = int(input("Введите час вашего рождения (число от 0 до 23): "))
    birth_minute = int(input("Введите минуту вашего рождения (число от 0 до 59): "))

    birth_datetime = datetime(birth_year, birth_month, birth_day, birth_hour, birth_minute)
    return birth_datetime


def main():
    name = input("Введите ваше имя: ")
    age = int(input("Введите ваш возраст: "))

    print(f"Привет, {name}! Тебе {age} лет.")

    calculate_more = input("Хотите узнать сколько это месяцев, дней и часов? (да/нет): ")
    if calculate_more.lower() == "да":
        months = calculate_age_in_months(age)
        days = calculate_age_in_days(age)
        hours = calculate_age_in_hours(age)
        print(f"Вы прожили примерно {months} месяцев, или {days} дней, или {hours} часов.")

        birth_time_response = input("Хотите ввести точное время вашего рождения? (да/нет): ")
        if birth_time_response.lower() == "да":
            birth_datetime = get_birth_datetime()
            current_time = datetime.now()
            age_delta = current_time - birth_datetime
            print(f"Прошло {age_delta.days} дней и {age_delta.seconds // 3600} часов с вашего рождения.")
    else:
        print("Хорошо, до свидания!")


if __name__ == "__main__":
    main()
