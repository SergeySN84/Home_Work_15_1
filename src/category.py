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
            raise TypeError("Можно добавлять только объекты "
                            "класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return (f"{self.name}, количество продуктов:"
                f" {len(self.__products)} шт., "
                f"общее количество: {total_quantity} шт.")

    def middle_price(self):
        try:

            total_price = sum(product.price for product in self.__products)
            count = len(self.__products)
            return total_price / count
        except ZeroDivisionError:
            return 0
