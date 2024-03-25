def mask_account(card: str):
    masked_account = "**" + card[-4:]
    return f"Счет {masked_account}"


print(mask_account("Счет 38976430693692818358"))


def mask_card(card: str):
    """Зашифровка счетов"""
    card = card.split()
    card_number = card.pop()
    card_name = " ".join(card)
    secret_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_name} {secret_number}"


print(mask_card("Visa Classic 6831982476737658"))