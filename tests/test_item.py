"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture


def tv():
    return Item("tv", 10000, 2)

@pytest.fixture


def phone():
    return Phone("Iphone 3000SuperMaxLastSecretSonOfSteveJobs", 1500000, 1, 2)


def test_item_initialization(tv):
    """Тест конструктора"""
    assert tv.name == "tv"
    assert tv.price == 10000
    assert tv.quantity == 2


def test_calculate_total_price(tv):
    """Тест сложения скидки и цены"""
    tv.apply_discount()
    assert tv.calculate_total_price() == 20000.0


def test_apply_discount(tv):
    """Невозвратная функция"""
    assert tv.apply_discount() is None


def test_name_property(tv):
    """Переименование"""
    tv.name = "colortv"
    assert tv.name == "colortv"


def test_name_setter(tv):
    """Сокращение переименования"""
    tv.name = "colortelevision"
    assert tv.name == "colortelev"


def test_instantiate_from_csv():
    """Достаем из csv объекты класса"""
    Item.instantiate_from_csv('src/items.csv')

    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].price == 1000
    assert Item.all[4].quantity == 5


def test_string_to_number_static():
    """Преобразование строки в целое число"""
    assert Item.string_to_number("5.76") == 5


def test_repr(tv):
    """Тест магии repr"""
    assert tv.__repr__() == "Item('tv', 10000, 2)"


def test_str(tv):
    """Тест магии str"""
    assert tv.__str__() == 'tv'


def test_add(tv, phone):
    """Тест магии add"""
    assert tv.__add__(phone) == 3
    assert tv.__add__(1) == "Складывать можно только объекты класса Item"
