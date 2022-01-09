"""Тесты для словарей"""
import pytest


@pytest.mark.dictionary
def test_dictionary_sort(setup_country_dictionary, module_fixture, session_fixture):
    """Проверка сортировки ключей"""
    assert (sorted(setup_country_dictionary.keys())) == ['China', 'Norway', 'Russia']


@pytest.mark.dictionary
def test_dictionary_del_key(setup_country_dictionary):
    """Проверка удаления ключа"""
    del setup_country_dictionary['Norway']
    assert setup_country_dictionary == {'Russia': 3, 'China': 2}


@pytest.mark.dictionary
def test_dictionary_contains_element(setup_country_dictionary):
    """Проверка наличия в словаре добавленного элемента"""
    setup_country_dictionary['Poland'] = 4
    assert ('Poland' in setup_country_dictionary) == 1


@pytest.mark.dictionary
def test_dictionary_clear(setup_country_dictionary):
    """Проверка удаления всех элементов словаря"""
    setup_country_dictionary.clear()
    assert setup_country_dictionary == {}
