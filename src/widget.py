from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number

#print(get_mask_card_number(12345678987654))
#print(get_mask_account(123456789))



def get_date(only_date: str) -> str:
    '''Принимает строку с форматом "2024-03-11T02:26:18.671407" и вовзращает строку в формате "ДД.ММ.ГГГГ" '''
    dt = datetime.strptime(only_date, '%Y-%m-%dT%H:%M:%S.%f')
    return dt.strftime('%d.%m.%Y')

input_date = "2024-03-11T02:26:18.671407"
result = get_date(input_date)
print(result)

