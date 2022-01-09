"""Тесты для строк"""
import pytest


@pytest.mark.string
def test_string_uppercase(setup_string_example, module_fixture, session_fixture):
    """Проверка изменения регистра строки"""
    assert setup_string_example.upper() == 'QWERTYQWERTY'


@pytest.mark.string
def test_string_replace(setup_string_example):
    """Проверка замены букв в строке"""
    assert setup_string_example.replace("t", "m") == 'qwermyqwermy'


@pytest.mark.string
def test_string_len(setup_string_example):
    """Проверка длины строки"""
    assert len(setup_string_example) == 12


@pytest.mark.string
def test_string_concatenation(setup_string_example):
    """Проверка конкатенации"""
    second_string = "asdfg"
    assert setup_string_example + second_string == "qwertyqwertyasdfg"
