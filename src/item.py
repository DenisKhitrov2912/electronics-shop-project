import csv
import os


class InstantiateCSVError(Exception):
    """Класс ошибки повреждения цсв"""


    def __init__(self, *args, **kwargs):
        """Конструктор ошибки"""
        self.message = args[0] if args else 'Файл items.csv поврежден'


    def __str__(self):
        """Магия str"""
        return self.message

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def _ _init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()


    def __repr__(self):
        """Магия отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        """Магия юзер - френдли"""
        return f'{self.__name}'


    def __add__(self, other):
        """Магия сложения с проверкой"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return "Складывать можно только объекты класса Item"


    @property


    def name(self):
        """Геттер имени"""
        return self.__name

    @name.setter


    def name(self, name):
        """Сеттер имени из 10 символов"""
        self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, file):
        """Метод класса для экземпляров из csv"""
        try:
            cls.all = []
            with open(os.path.join('..', file), newline = '',
                encoding = 'windows - 1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['name']
                    price = float(row['price'])
                    try:
                        quantity = int(row['quantity'])
                    except ValueError:
                        raise InstantiateCSVError
                    cls(name, price, quantity)
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл items.csv")
            raise
        except InstantiateCSVError:
            print("InstantiateCSVError: Файл items.csv поврежден")
            raise

    @staticmethod


    def string_to_number(data):
        """Строка - целое число"""
        return int(float(data))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
