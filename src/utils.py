import json
from datetime import datetime


def get_data():
    """считывает данные"""
    with open("../data/operations.json") as file:
        return json.load(file)


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
    return date_format.strptime("%d.%m.%Y")


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








