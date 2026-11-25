def get_mask_card_number(number_card: str) -> str:
    """Функция маскирования номера карты"""
    s_number_card = str(number_card)
    if len(s_number_card) != 16:
        return "Укажите 16 символов" """Уточняем о требовании в 16 символов"""

    else:
        number_card_code = s_number_card[0:4] + " " + s_number_card[4:6] + "** **** " + s_number_card[12:]
        """ Маскируем номер карты"""
        return number_card_code


def get_mask_account(account: str) -> str:
    """Функция маскирования аккаунта"""
    s_account = str(account)
    if len(s_account) < 4:
        return "Неверно указан аккаунт. Требуется более 3х символов." """Исключаем вариативность менее 4-х символов"""
    else:
        account_code = "**" + s_account[-4:]
        """Маскируем номер аккаунта"""
        return account_code
