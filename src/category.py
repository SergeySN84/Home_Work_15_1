from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        if not issubclass(type(product), Product):
            raise TypeError("Класс объекта должен быть наследником Product")

        if product.quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return (f"{self.name}, количество продуктов: {len(self.__products)} шт., "
                f"общее количество: {total_quantity} шт.")
