from datetime import datetime
from typing import Any


def filter_by_state(items: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Сортирует словари из полученного списка в новый список со словарями по значению state.

    Item - получаемый список
    State - параметр отбора
    Result - обновленный список словарей,отобранных по заданному параметру
    """
    result = []  # создаем пустой список
    for item in items:
        current_state = item.get("state")  # получаем значение state
        if current_state == state:  # сравниваем значение с требованием
            result.append(item)
    return result

def sort_by_date(items: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Функция,сортирующая список словарей по дате в порядке убывания
    """
    prepared = []  # создаем пустой список
    for item in items:
        raw = item.get("date")  # получаем значения дат для дальнейшей сортировки
        if isinstance(raw, datetime):
            dt = raw
        elif isinstance(raw, str):
            for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
                try:
                    dt = datetime.strptime(raw, fmt)
                    break
                except ValueError:
                    continue  # проверяем дату по требуемым условиям
            else:
                raise ValueError(f"Не удалось распознать дату: {raw!r}")
        else:
            raise TypeError(f"Неподдерживаемый тип даты: {type(raw)}")
        prepared.append((dt, item))

    # Сортируем по дате (первый элемент кортежа)
    prepared.sort(key=lambda x: x[0], reverse=reverse)

    # Возвращаем только словари
    return [item for _, item in prepared]



