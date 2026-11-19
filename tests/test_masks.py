import pytest
from typing import Any
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers() -> list[tuple[str, str]]:
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982411519745", "6831 98** **** 9745"),
    ]


class TestGetMaskCardNumber:
    def test_correct_masking(self, card_numbers: list[tuple[str, str]]) -> None:  # проверка правильности работы функции
        for number, expected in card_numbers:
            assert get_mask_card_number(number) == expected

    def test_returns_str(self) -> None:  # проверка на возврат строки
        assert isinstance(get_mask_card_number("7000792289606361"), str)

    @pytest.mark.parametrize("empty", ["", None])  # проверка на отсутствие номера
    def test_missing_number(self, empty: Any) -> None:
        result = get_mask_card_number(empty)
        assert isinstance(result, str)
        assert result != ""

    def test_non_standard_length(self) -> None:  # проверка на длинну
        result = get_mask_card_number("123")
        assert result != "123"


class TestGetMaskAccount:
    def test_correct_masking(self) -> None:  # проверка правильности работы функции
        assert get_mask_account("73654108430135874305") == "**4305"

    @pytest.mark.parametrize("short", ["123", "", "4305", None])  # проверка на длинну
    def test_account_shorter_than_expected(self, short: Any) -> None:
        result = get_mask_account(short)
        assert isinstance(result, str)
