def filter_by_currency(transactions, currency):
    '''Функция для поочередной выдаче транзакций'''
    return filter(lambda t: t.get("operationAmount", {}).get("currency", {}).get("name") == currency,transactions)

def transaction_descriptions(transactions):
    '''Генератор для возвращения каждой операции по очереди'''
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start, end):
    '''Генератор для номеров кард'''
    for i in range(start, end + 1):
        s = f"{i:016d}"          # 16 цифр с ведущими нулями
        yield f"{s[:4]} {s[4:8]} {s[8:12]} {s[12:]}"