import pytest
from src.category import Category
from src.product import Product


def test_category_initialization():
    product = Product("Samsung Galaxy S23", "", 180000.0, 5)
    category = Category("Смартфоны", "Описание категории", [product])

    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category._Category__products) == 1


def test_category_str_representation():
    product = Product("Samsung Galaxy S23", "", 180000.0, 5)
    category = Category("Смартфоны", "Описание", [product])
    assert str(category) == "Смартфоны, количество продуктов: 1 шт."


def test_category_products_property():
    product1 = Product("Samsung Galaxy S23", "", 180000.0, 5)
    product2 = Product("Iphone 15", "", 210000.0, 8)
    category = Category("Смартфоны", "Описание", [product1, product2])

    expected_output = (
        "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )
    assert category.products == expected_output


def test_add_product():
    product = Product("Samsung Galaxy S23", "", 180000.0, 5)
    category = Category("Смартфоны", "Описание", [])
    category.add_product(product)
    assert len(category._Category__products) == 1


def test_add_invalid_product_raises_error():
    category = Category("Смартфоны", "Описание", [])
    with pytest.raises(ValueError):
        category.add_product("not a product")
