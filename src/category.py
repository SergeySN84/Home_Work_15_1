from src.product import Product

class Category:
    total_categories = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # Приватное поле
        Category.total_categories += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты типа Product.")
        self.__products.append(product)

    @property
    def products(self):
        return '\n'.join([str(product) for product in self.__products])

    def __str__(self):
        total_products = len(self.__products)
        total_quantity = sum(product.quantity for product in self.__products)
        return (f"{self.name}, количество продуктов: {total_products} шт.,"
                f" общее количество: {total_quantity} шт.")
