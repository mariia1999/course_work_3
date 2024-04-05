import json
from datetime import datetime


def get_data():
    """считывает данные"""
    with open("data/operations.json") as file:
        return json.load(file)


def get_transactions(data):
    for transaction in data:
        if 'from' in transaction:
            transaction['from'] = mask_card(data['from'])
        elif 'to' in transaction:
            transaction['to'] = mask_account(data['to'])
    return data


def filter_data(data):
    """фильтр по операциям Executed"""
    filter_operations = [operation for operation in data if "state" in operation and operation["state"] == 'EXECUTED']
    return filter_operations


def sort_operations(data):
    """Сортировка последних пяти операций и их вывод"""
    sorted_operation = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_operation[:5]


def format_date(date: str):
    """Возваращет дату в виде ДД.ММ.ГГГГ"""
    date_format = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_format.strftime("%d.%m.%Y")


def mask_account(account: str):
    """защифровка счета"""
    masked_account = "**" + account[-4:]
    return f"Счет {masked_account}"


def mask_card(card: str):
    """Зашифровка карты"""
    card = card.split()
    card_number = card.pop()
    card_name = " ".join(card)
    secret_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_name} {secret_number}"


def format_amount(amount):
    return amount['amount']


def format_transaction(data):
    #{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
    # 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
    # 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}

    #14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
    # 82771.72 руб.
    date = format_date(data['date'])
    payment_from = mask_card(data.get('from', ''))
    payment_to = mask_account(data.get('to', ''))
    amount = format_amount(data['operationAmount']['currency']['name'])
    return f'{date} {data['description']}\n{payment_from} -> {payment_to}\n{amount}'


def print_transactions(data):
    for transaction in data:
        print(format_transaction(transaction))








