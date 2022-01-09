"""Тесты для списков"""
import pytest


@pytest.mark.list
def test_list_count(setup_months_list, module_fixture, session_fixture):
    """Проверка количества элементов в списке"""
    assert setup_months_list.count('March') == 2


@pytest.mark.list
def test_list_append(setup_num_list):
    """Проверка наличия добавленных элементов в конец списка"""
    setup_num_list.append(6)
    setup_num_list.append(7)
    setup_num_list.append(8)
    assert setup_num_list == [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.list
def test_list_index(setup_months_list):
    """Проверка индекса элемента"""
    assert setup_months_list.index('February') == 1


@pytest.mark.list
def test_list_clear(setup_num_list):
    """Проверка списка на пустоту после заполенеия и очистки"""
    setup_num_list.clear()
    assert setup_num_list == []


@pytest.mark.list
def test_list_remove(setup_months_list):
    """Проверка списка после удаления элемента"""
    setup_months_list.remove('January')
    assert setup_months_list == ['February', 'March', 'April', 'March']
