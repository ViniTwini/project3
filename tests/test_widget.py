import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def mixed_inputs() -> list:
    """Фикстура с картами и счетами вперемешку."""
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7158300734726758", "Maestro 7158 30** **** 6758"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ]


class TestMaskAccountCard:
    def test_recognizes_card_and_account(self, mixed_inputs): #проверка правильности работы функции
        for raw, expected in mixed_inputs:
            assert mask_account_card(raw) == expected


    @pytest.mark.parametrize(
        "bad",
        ["", "Visa Platinum", "Счёт", "нет числа тут", 12345],
    )
    def test_invalid_input(self, bad): #проверка на некорректный ввод
        with pytest.raises((ValueError, TypeError, AttributeError, IndexError)):
            mask_account_card(bad)


class TestGetDate:
    def test_correct_conversion(self): #проверка работы функции
        assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    @pytest.mark.parametrize(
        "raw, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2024-01-01T00:00:00.000000", "01.01.2024"),
            ("1999-12-31T23:59:59", "31.12.1999"),
        ],
    )
    def test_various_formats(self, raw, expected): #проверка на различные вводные данные
        assert get_date(raw) == expected

    @pytest.mark.parametrize("bad", ["", "не дата", None, "2024-13-45T00:00:00"]) #проверка на некорректный ввод
    def test_invalid_or_missing_date(self, bad):
        with pytest.raises((ValueError, TypeError, AttributeError)):
            get_date(bad)