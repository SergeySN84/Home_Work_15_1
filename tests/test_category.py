import pytest
from src.product import Product
from src.category import Category


def test_category_str():
    product = Product("Товар", "Описание", 100, 5)
    category = Category("Категория", "Описание", [product])
    expected = ("Категория, количество продуктов: 1 шт.,"
                " общее количество: 5 шт.")
    assert str(category) == expected


def test_category_total_count():
    assert Category.total_categories == 1


def test_category_products_property():
    product1 = Product("Товар1", "Описание1", 100, 5)
    product2 = Product("Товар2", "Описание2", 200, 3)
    category = Category("Категория", "Описание", [product1, product2])
    expected = ("Товар1, 100 руб. Остаток: 5 шт."
                "\nТовар2, 200 руб. Остаток: 3 шт.")
    assert category.products == expected


def test_category_add_product_valid():
    category = Category("Категория", "Описание", [])
    product = Product("Товар", "Описание", 100, 5)
    category.add_product(product)
    assert len(category._Category__products) == 1


def test_category_add_product_invalid():
    category = Category("Категория", "Описание", [])
    with pytest.raises(ValueError):
        category.add_product("не продукт")
