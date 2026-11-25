import pytest
from src.generation import filter_by_currency, transaction_descriptions, card_number_generator

SAMPLE = [
    {
        "id": 1,
        "description": "Перевод организации",
        "operationAmount": {"currency": {"name": "USD"}},
        "state": "EXECUTED",
    },
    {
        "id": 2,
        "description": "Перевод со счета на счет",
        "operationAmount": {"currency": {"name": "RUB"}},
        "state": "EXECUTED",
    },
    {
        "id": 3,
        "description": "Перевод организации",
        "operationAmount": {"currency": {"name": "USD"}},
        "state": "EXECUTED",
    },
]



def test_filter_by_currency_usd():
    '''Проверка на работу функции'''
    res = list(filter_by_currency(SAMPLE, "USD"))
    assert len(res) == 2
    assert res[0]["id"] == 1
    assert res[1]["id"] == 3


def test_filter_by_currency_no_matches():
    '''Проверка на остутствие SAMPLE'''
    assert list(filter_by_currency(SAMPLE, "EUR")) == []


def test_filter_by_currency_empty():
    '''Проверка на остутствие списка'''
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_missing_keys():
    '''проверка, что .get() спасает от KeyError'''
    broken = [{"id": 999}]
    assert list(filter_by_currency(broken, "USD")) == []



def test_transaction_descriptions():
    '''Проверка корректной работы функции'''
    assert list(transaction_descriptions(SAMPLE)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод организации",
    ]


def test_transaction_descriptions_empty():
    '''Проверка на пустой список'''
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]),
        (42, 42, ["0000 0000 0000 0042"]),
        (998, 1002, ["0000 0000 0000 0998", "0000 0000 0000 0999", "0000 0000 0000 1000", "0000 0000 0000 1001", "0000 0000 0000 1002"]),
    ],
)
def test_card_number_generator(start, end, expected):
    '''Проверка корректной работы функции'''
    assert list(card_number_generator(start, end)) == expected


def test_card_number_generator_empty_range():
    '''Исключения пустого результата'''
    assert list(card_number_generator(5, 3)) == []