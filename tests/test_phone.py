import pytest
from src.item import Item
from src.phone import Phone

# Фикстуры:
@pytest.fixture


def tv():
    return Item("tv", 10000, 2)

@pytest.fixture


def phone():
    return Phone("Iphone 3000SuperMaxLastSecretSonOfSteveJobs", 1500000, 1, 2)


def test_init(phone):
    """Тест конструктора"""
    assert phone.name == "Iphone 3000SuperMaxLastSecretSonOfSteveJobs"
    assert phone.price == 1500000
    assert phone.quantity == 1
    assert phone.number_of_sim == 2


def test_init_1():
    """Тест конструктора неправильного объекта"""
    with pytest.raises(ValueError):
        Phone("First", 10, 1, 0)


def test_repr(phone):
    """Тест магии для отладки"""
    assert phone.__repr__() == "Phone('Iphone 3000SuperMaxLastSecretSonOfSteveJobs', 1500000, 1, 2)"


def test_str(phone):
    """Тест магии для пользователя"""
    assert phone.__str__() == "Iphone 3000SuperMaxLastSecretSonOfSteveJobs"


def test_add(phone, tv):
    """Тест + """
    assert phone.__add__(tv) == 3
    assert phone.__add__(1) == "Складывать можно только объекты класса Item или дочернего Phone"


def test_number_of_sim_getter(phone):
    """Тест геттера симок"""
    assert phone.number_of_sim == 2


def test_number_of_sim_setter(phone):
    """Тест сеттера симок"""
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
    with pytest.raises(ValueError):
        phone.number_of_sim = - 1
    with pytest.raises(ValueError):
        phone.number_of_sim = 8.5
    with pytest.raises(ValueError):
        phone.number_of_sim = "abcd"
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
