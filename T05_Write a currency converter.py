def convert_currency(amount, from_currency, to_currency):
    # Приблизительные курсы валют (как пример)
    exchange_rates = {
        'pln': {'usd': 0.26, 'eur': 0.23, 'rub': 19.08},
        'usd': {'pln': 3.85, 'eur': 0.89, 'rub': 73.96},
        'eur': {'pln': 4.32, 'usd': 1.12, 'rub': 83.07},
        'rub': {'pln': 0.05, 'usd': 0.014, 'eur': 0.012}
    }

    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        print("Неверно указаны валюты")
        return None

    exchange_rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    print("Добро пожаловать в конвертер валют!")
    from_currency = input("Введите исходную валюту (pln, usd, eur, rub): ").lower()
    to_currency = input("Введите валюту, в которую хотите конвертировать (pln, usd, eur, rub): ").lower()
    amount = float(input("Введите сумму для конвертации: "))

    result = convert_currency(amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")

if __name__ == "__main__":
    main()
