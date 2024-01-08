from src.keyboard import Keyboard
import pytest


@pytest.fixture


def kb():
    """Фикстура экземпляра класса клавиатуры"""
    return Keyboard("Sample", 1000, 1)


def test_init(kb):
    """Тест конструктора"""
    assert kb.name == "Sample"
    assert kb.price == 1000
    assert kb.quantity == 1


def test_init_mixin(kb):
    """Тест конструктора миксина"""
    assert kb.language == "EN"


def test_language(kb):
    """Тест геттера языка"""
    assert kb.language == "EN"


def test_change_lang(kb):
    """Тест смены языка"""
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    with pytest.raises(AttributeError):
        kb.language = "ES"

