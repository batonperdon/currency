Импорт библиотеки

import requests


 requests: Библиотека для работы с HTTP-запросами. Она используется для отправки запросов к API и получения данных.

Функция получения курса валют

def get_exchange_rate():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/RUB")
        data = response.json()
        return data['rates']['USD']
    except Exception as e:
        print("Ошибка при получении курса валют:", e)
        return None


 get_exchange_rate(): Функция для получения актуального курса рубля к доллару.

  requests.get(...): Отправляет GET-запрос к указанному URL, который возвращает данные о курсах валют.

  response.json(): Преобразует ответ в формате JSON в словарь Python.

  Возвращает курс USD, если запрос успешен. Если возникает ошибка (например, проблемы с сетью), выводит сообщение об ошибке и возвращает None.

Функция конвертации

def convert_rub_to_usd(rubles, exchange_rate):
    return rubles * exchange_rate


 convert_rub_to_usd(rubles, exchange_rate): Функция для конвертации суммы в рублях в доллары.

   Умножает количество рублей на курс доллара и возвращает результат.

Основная функция

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


main(): Основная функция программы.

   Выводит приветственное сообщение.

   Вызывает get_exchange_rate() для получения курса валют.

   Если курс не был получен, программа завершает работу.

   Выводит актуальный курс рубля к доллару.

   Запускает бесконечный цикл, в котором запрашивает у пользователя сумму в рублях.

     Если пользователь вводит число, программа конвертирует его в доллары и выводит результат.

     Если вводится некорректное значение (например, текст), возникает исключение ValueError, программа выводит сообщение о завершении ввода и выходит из цикла.
