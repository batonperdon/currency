import requests

def get_exchange_rate():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/RUB")
        data = response.json()
        return data['rates']['USD']
    except Exception as e:
        print("Ошибка при получении курса валют:", e)
        return None

def convert_rub_to_usd(rubles, exchange_rate):
    return rubles * exchange_rate

def main():
    print("Добро пожаловать в конвертер валют!")
    exchange_rate = get_exchange_rate()

    if exchange_rate is None:
        print("Не удалось получить курс валют. Закрытие программы.")
        return

    print(f"Актуальный курс: 1 RUB = {exchange_rate:.2f} USD")

    while True:
        try:
            rubles = float(input("Введите сумму в рублях (или 'exit' для выхода): "))
            dollars = convert_rub_to_usd(rubles, exchange_rate)
            print(f"{rubles} RUB = {dollars:.2f} USD")
        except ValueError:
            print("Ввод завершен. Выход из программы.")
            break

if __name__ == "__main__":
    main()
