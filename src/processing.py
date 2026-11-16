def filter_by_state(items, state='EXECUTED'):
    result = []
    for item in items:
        current_state = item.get('state')
        if current_state == state:
            result.append(item)
    return result

from datetime import datetime

def sort_by_date_verbose(items, reverse=True):
    prepared = []
    for item in items:
        raw = item.get('date')
        if isinstance(raw, datetime):
            dt = raw
        elif isinstance(raw, str):
            for fmt in ('%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S'):
                try:
                    dt = datetime.strptime(raw, fmt)
                    break
                except ValueError:
                    continue
            else:
                raise ValueError(f"Не удалось распознать дату: {raw!r}")
        else:
            raise TypeError(f"Неподдерживаемый тип даты: {type(raw)}")
        prepared.append((dt, item))

    # Сортируем по дате (первый элемент кортежа)
    prepared.sort(key=lambda x: x[0], reverse=reverse)

    # Возвращаем только словари
    return [item for _, item in prepared]