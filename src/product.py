from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class LogCreationMixin:

    pass


class Product(LogCreationMixin, BaseProduct):
    product_count = 0
    category_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity


        print(f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})")

        if self.quantity > 0:
            Product.product_count += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректно!")
        elif value < self._price:
            choice = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if choice.lower() == 'y':
                self._price = value
                print("Цена успешно понижена.")
            else:
                print("Цена не была изменена.")
        else:
            self._price = value

    def get_description(self):
        return self.description

    def get_price(self):
        return self._price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
