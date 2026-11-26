import pytest
from src.decorators import log


def test_success_console(capsys):
    '''Проверка корректного возращения результата без filename'''
    @log()
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    out = capsys.readouterr().out
    assert out == "add ok\n"


def test_success_file(tmp_path):
    '''Проверка на корректный результат при наличии filename'''
    file = tmp_path / "logs.txt"

    @log(filename=str(file))
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    assert file.read_text().strip() == "add ok"


def test_append_mode(tmp_path):
    """Проверка, что новые записи дописываются, а не перезаписывают файл."""
    file = tmp_path / "logs.txt"

    @log(filename=str(file))
    def f1():
        return 1

    @log(filename=str(file))
    def f2():
        return 2

    f1()
    f2()

    lines = file.read_text().strip().split("\n")
    assert lines == ["f1 ok", "f2 ok"]


def test_error_console(capsys):
    '''Проверка формата лога в консоль'''
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    out = capsys.readouterr().out
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in out


def test_error_file(tmp_path):
    '''Проверка формата лога в файл'''
    file = tmp_path / "logs.txt"

    @log(filename=str(file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    content = file.read_text().strip()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in content


def test_with_kwargs(capsys):
    '''Проверка выполнения функции с именованными аргументами'''
    @log()
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    assert greet("Alice", greeting="Hi") == "Hi, Alice!"
    out = capsys.readouterr().out
    assert out == "greet ok\n"


def test_error_with_kwargs(capsys):
    '''Проверка выполнения функции с позиционными и именованными аргументами'''
    @log()
    def process(x, y=10):
        raise ValueError("bad value")

    with pytest.raises(ValueError):
        process(5, y=20)

    out = capsys.readouterr().out
    assert "process error: ValueError. Inputs: (5,), {'y': 20}" in out