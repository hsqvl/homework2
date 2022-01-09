"""Тесты для множеств"""
import pytest


@pytest.mark.sets
def test_set_join(setup_set_colors, module_fixture, session_fixture):
    """Проверка присоединения строки и её номера"""
    assert ('blue' in setup_set_colors) == 0


@pytest.mark.sets
def test_set_del_element():
    """Проверка удаления дубликатов элементов множества"""
    test_set_unique = set('aсrbnbaсrbnbaсrbnb')
    assert test_set_unique == {'b', 'n', 'с', 'a', 'r'}


@pytest.mark.sets
def test_empty_set():
    """Проверка наличия пустого множества после его создания и очистки"""
    test_set = {'one', 'two'}
    test_set.clear()
    assert test_set == set()


@pytest.mark.sets
def test_set_len(setup_set_colors):
    """Проверка того, что множество не нулевое"""
    assert len(setup_set_colors) != 0
