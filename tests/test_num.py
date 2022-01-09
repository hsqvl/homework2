"""Тесты для чисел"""
import pytest


@pytest.mark.num
def test_minus_num(setup_num_example, module_fixture,session_fixture):
    """Проверка вычитания целого числа их тестового"""
    assert  setup_num_example -5 == 20


@pytest.mark.num
def test_plus_num(setup_num_example):
    """Проверка сложения целого числа с тестовым"""
    assert setup_num_example + 5 ==30


@pytest.mark.num
def test_qsrt_num(setup_num_example):
    """Проверка возведения в корень"""
    assert setup_num_example ** 2 == 625


@pytest.mark.num
def test_rem_num(setup_num_example):
    """Проверка остатка от деления"""
    assert  setup_num_example % 2 == 1


@pytest.mark.num
def test_div_num(setup_num_example):
    """Проверка деления тестового числа"""
    assert setup_num_example / 5 == 5.0
