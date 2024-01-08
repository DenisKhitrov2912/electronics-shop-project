from src.item import Item


class MixinChangeLang:
    def __init__(self):
        """Инициализатор"""
        self.__language = 'EN'

    @property


    def language(self):
        """Геттер языка"""
        return self.__language


    def change_lang(self):
        """Меняем язык при вызове"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'




class Keyboard(Item, MixinChangeLang):
    def __init__(self, name: str, price: float, quantity: int):
        """Конструктор класса"""
        super().__init__(name, price, quantity)