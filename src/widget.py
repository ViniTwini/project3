from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    account_info = account_info.strip()

    # Определяем тип по наличию слова «счет»
    is_account = "счет" in account_info.lower()

    # Находим номер как часть после последнего пробела
    last_space_index = account_info.rfind(" ")
    if last_space_index == -1:
        # Нет пробела — формат некорректен, возвращаем как есть
        return account_info

    prefix = account_info[:last_space_index]
    number = account_info[last_space_index + 1 :]

    # Применяем нужную функцию маскировки
    masked_number = get_mask_account(number) if is_account else get_mask_card_number(number)

    return f"{prefix} {masked_number}"


def get_date(only_date: str) -> str:
    """Принимает строку с форматом "2024-03-11T02:26:18.671407" и вовзращает строку в формате "ДД.ММ.ГГГГ" """
    dt = datetime.strptime(only_date, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")


print(mask_account_card("Счет 64686473678894779589"))
print(get_date("2024-03-11T02:26:18.671407"))
