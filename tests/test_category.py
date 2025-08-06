import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


def test_category_str():
    """Проверка строкового представления категории"""
    product = Product("Товар", "Описание", 100, 5)
    category = Category("Категория", "Описание", [product])
    expected = ("Категория, количество продуктов: 1 шт.,"
                " общее количество: 5 шт.")
    assert str(category) == expected


def test_category_products_property():
    """Проверка свойства products — вывод всех товаров по одному на строку"""
    product1 = Product("Товар1", "Описание1", 100, 5)
    product2 = Product("Товар2", "Описание2", 200, 3)
    category = Category("Категория", "Описание", [product1, product2])
    expected = ("Товар1, 100 руб. Остаток: 5 шт."
                "\nТовар2, 200 руб. Остаток: 3 шт.")
    assert category.products == expected


def test_category_add_product_valid():
    """Проверка добавления валидного продукта"""
    category = Category("Категория", "Описание", [])
    product = Product("Товар", "Описание", 100, 5)
    category.add_product(product)
    # Проверяем через name mangling
    assert len(category._Category__products) == 1
    assert category._Category__products[0] is product


def test_category_add_product_invalid_non_product():
    """Проверка добавления НЕ продукта — должен быть ValueError"""
    category = Category("Категория", "Описание", [])
    with pytest.raises(ValueError,
                       match="Товар с нулевым "
                             "количеством не может быть добавлен"):
        category.add_product("не продукт")


def test_category_add_product_zero_quantity():
    """Проверка добавления продукта с нулевым количеством"""
    product = Product("Товар", "Описание", 100, 0)
    category = Category("Категория", "Описание", [])
    with pytest.raises(ValueError,
                       match="Товар с нулевым "
                             "количеством не может быть добавлен"):
        category.add_product(product)


def test_category_add_product_negative_quantity():
    """Проверка добавления продукта с отрицательным количеством"""
    product = Product("Товар", "Описание", 100, -5)
    category = Category("Категория", "Описание", [])
    with pytest.raises(ValueError,
                       match="Товар с нулевым "
                             "количеством не может быть добавлен"):
        category.add_product(product)


def test_category_total_products_counter():
    """Проверка счётчика product_count"""
    Category.product_count = 0  # Сброс для теста
    category = Category("Категория", "Описание", [])
    product1 = Product("Товар1", "Описание", 100, 5)
    product2 = Product("Товар2", "Описание", 200, 3)
    category.add_product(product1)
    category.add_product(product2)
    assert Category.product_count == 2


def test_category_total_categories_counter():
    """Проверка счётчика total_categories"""
    initial_count = Category.total_categories
    Category("Категория 1", "Описание")
    Category("Категория 2", "Описание")
    assert Category.total_categories == initial_count + 2


def test_category_init_with_products():
    """Проверка, что продукты из списка в конструкторе добавляются корректно"""
    product1 = Product("Товар1", "Описание", 100, 5)
    product2 = Product("Товар2", "Описание", 200, 3)
    category = Category("Категория", "Описание", [product1, product2])
    assert len(category._Category__products) == 2
    assert product1 in category._Category__products
    assert product2 in category._Category__products


def test_category_products_empty():
    """Проверка вывода для пустой категории"""
    category = Category("Категория", "Описание", [])
    assert category.products == ""


def test_category_str_empty():
    """Проверка __str__ для пустой категории"""
    category = Category("Категория", "Описание", [])
    assert str(category) == ("Категория, количество продуктов:"
                             " 0 шт., общее количество: 0 шт.")


def test_category_inheritance_support():
    """Проверка, что можно добавлять наследников Product"""
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 5, 95.0, "15", 256, "Черный")
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 10, "Россия", "7 дней", "Зелёный")
    category = Category("Категория", "Описание", [])
    category.add_product(smartphone)
    category.add_product(grass)
    assert len(category._Category__products) == 2
    assert smartphone in category._Category__products
    assert grass in category._Category__products


def test_category_products_order():
    """Проверка порядка продуктов в свойстве products"""
    product1 = Product("A", "Описание", 100, 1)
    product2 = Product("B", "Описание", 100, 1)
    category = Category("Категория", "Описание", [product1, product2])
    expected = "A, 100 руб. Остаток: 1 шт.\nB, 100 руб. Остаток: 1 шт."
    assert category.products == expected
