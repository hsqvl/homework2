"""Данные для использования в тестах"""
import pytest


@pytest.fixture
def setup_months_list():
    """Список с месяцами"""
    return ['January', 'February', 'March', 'April', 'March']


@pytest.fixture
def setup_num_list():
    """Список с цифрами"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def setup_country_dictionary():
    """Список со словарем стран"""
    return {'Norway': 1, 'Russia': 3, 'China': 2}


@pytest.fixture
def setup_set_colors():
    """Список со множеством цветов"""
    return {'green', 'orange', 'green', 'yellow', 'orange', 'black'}


@pytest.fixture
def setup_string_example():
    """Тестовая строка"""
    return 'qwertyqwerty'


@pytest.fixture
def setup_tuple_example():
    """Тестовый кортеж"""
    return 'one', 'two', 'three', 'four', 'five'


@pytest.fixture
def setup_tuple_num_example():
    """Тестовый кортеж числа"""
    return 1.1, 0.5, 45.5, 33.33, 9.12, 3.14, 2.73


@pytest.fixture
def setup_num_example():
    """Тестовое число"""
    return 25


@pytest.fixture(scope="module")
def module_fixture(request):
    """ Вывод сообщения о начале и конце работы модуля"""
    print(f"\n Start {request.scope} ")

    def fin():
        print(f"\n Finalize {request.scope} ")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    """ Вывод сообщения о начале и конце работы сесcии"""
    print(f"\n Start  {request.scope} ")

    def fin():
        print(f"\n Finalize {request.scope} ")

    request.addfinalizer(fin)
