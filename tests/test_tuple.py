"""Тесты для кортежей"""
import pytest


@pytest.mark.tuple
def test_len_tuple(setup_tuple_example, module_fixture, session_fixture):
    """Проверка количества значений кортежа"""
    assert len(setup_tuple_example) == 5


@pytest.mark.tuple
def test_index_tuple(setup_tuple_example):
    """Проверка вызова индекса кортежа"""
    assert setup_tuple_example.index('four') == 3


@pytest.mark.tuple
def test_list_tuple(setup_tuple_example):
    """Конвертация кортежа в список"""
    assert list(setup_tuple_example) == ['one', 'two', 'three', 'four', 'five']


@pytest.mark.tuple
def test_join_tuple(setup_tuple_example):
    """Конвертация кортежа в строку"""
    assert ''.join(setup_tuple_example) == 'onetwothreefourfive'


@pytest.mark.tuple
def test_slice_tuple(setup_tuple_num_example):
    """Слайс кортежа с 0 по 5 с шагом 2"""
    assert setup_tuple_num_example[0:5:2] == (1.1, 45.5, 9.12)


@pytest.mark.tuple
def test_sort_tuple(setup_tuple_num_example):
    """Сортировка кортежа"""
    assert sorted(setup_tuple_num_example) == [0.5, 1.1, 2.73, 3.14, 9.12, 33.33, 45.5]
