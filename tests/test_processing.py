import pytest
from datetime import datetime

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 1, "state": "PENDING", "date": "2020-01-15T10:00:00"},
    ]


class TestFilterByState:
    def test_filter_executed(self, transactions): #проверка работы функции
        result = filter_by_state(transactions, state="EXECUTED")
        assert all(item["state"] == "EXECUTED" for item in result)
        assert {item["id"] for item in result} == {41428829, 939719570}

    def test_missing_state_in_items(self, transactions): #проверка на отсутствие ключа
        data = [{"id": 1}, {"id": 2, "state": "EXECUTED"}]
        result = filter_by_state(data, state="EXECUTED")
        assert result == [{"id": 2, "state": "EXECUTED"}]

    def test_empty_list(self): #проверка на пустой список
        assert filter_by_state([], state="EXECUTED") == []


class TestSortByDate:
    def test_sort_descending_default(self, transactions): #проверка работы функции
        result = sort_by_date(transactions)
        dates = [item["date"] for item in result]
        assert dates[0] == "2020-01-15T10:00:00"
        assert dates[1] == "2019-07-03T18:35:29.512364"
        assert dates[-1] == "2018-06-30T02:08:58.425572"

    def test_equal_dates_keep_order(self): #проверка стабильности сортировки
        data = [
            {"id": 1, "date": "2024-01-01"},
            {"id": 2, "date": "2024-01-01"},
            {"id": 3, "date": "2024-01-01"},
        ]
        assert [item["id"] for item in sort_by_date(data)] == [1, 2, 3]
        assert [item["id"] for item in sort_by_date(data, False)] == [1, 2, 3]

    def test_empty_list(self): #проверка на пустой список
        assert sort_by_date([]) == []

    def test_bad_string_raises(self): #проверка на ввод не даты
        with pytest.raises(ValueError):
            sort_by_date([{"id": 1, "date": "не дата"}])

    @pytest.mark.parametrize(
        "date_str",
        [
            "2024-01-01",                      # только дата
            "2024-01-01 12:30:45",             # дата и время через пробел
            "2024-01-01T12:30:45",             # ISO без микросекунд
            "2024-01-01T12:30:45.123456",      # ISO с микросекундами
        ],
    )
    def test_supported_date_formats(self, date_str): #проверка на поддержание всех форматов
        data = [{"id": 1, "date": date_str}, {"id": 2, "date": "2024-06-01"}]
        assert [item["id"] for item in sort_by_date(data)] == [2, 1]