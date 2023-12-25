from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_num: int):
        """Инициализатор дочернего класса"""
        super().__init__(name, price, quantity)
        if float(sim_num) == int(sim_num) and int(sim_num) > 0:
            self.__sim_num = sim_num
        else:
            raise ValueError("Количество сим - карт должно быть целым числом больше нуля")


    def __repr__(self):
        """Магия отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__sim_num})"


    def __str__(self):
        """Магия юзер - френдли"""
        return f'{self.name}'


    def __add__(self, other):
        """Магия сложения с проверкой"""
        if not isinstance(other, Item):
            raise TypeError("Складывать можно только объекты класса Item")
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        """Геттер числа симок"""
        return self.__sim_num

    @number_of_sim.setter
    def number_of_sim(self, num):
        """Сеттер числа симок"""
        if float(num) == int(num) and int(num) > 0:
            self.__sim_num = num
        else:
            raise ValueError("Количество сим - карт должно быть целым числом больше нуля")
