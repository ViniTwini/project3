from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Маскирует карту или счёт в строке вида 'Visa Platinum 7000792289606361'."""
    if not isinstance(card_info, str) or not card_info.strip():
        raise ValueError("Некорректный ввод: ожидается непустая строка")

    parts = card_info.split()
    if len(parts) < 2:
        raise ValueError("Некорректный ввод: нет номера после названия")

    number = parts[-1]
    label = " ".join(parts[:-1])

    if len(number) == 16 and number.isdigit():  # карта
        return f"{label} {get_mask_card_number(number)}"
    if len(number) == 20 and number.isdigit():  # счёт
        return f"{label} {get_mask_account(number)}"

    raise ValueError(f"Не удалось распознать номер: {number}")


def get_date(date_string: str) -> str:
    """Переводит дату из формата '2024-03-11T02:26:18.671407' в '11.03.2024'."""
    if not isinstance(date_string, str) or not date_string:
        raise ValueError("Некорректная дата")

    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S"):
        try:
            dt = datetime.strptime(date_string, fmt)
            return dt.strftime("%d.%m.%Y")
        except ValueError:
            continue

    raise ValueError(f"Не удалось распознать дату: {date_string}")


print(mask_account_card("Счет 64686473678894779589"))
print(get_date("2024-03-11T02:26:18.671407"))
