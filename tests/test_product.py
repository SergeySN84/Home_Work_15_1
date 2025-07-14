import pytest

from src.product import Product


def test_product_str():
    product = Product("Товар", "Описание", 100, 5)
    assert str(product) == "Товар, 100 руб. Остаток: 5 шт."


def test_product_add():
    product1 = Product("Товар1", "Описание1", 100, 2)
    product2 = Product("Товар2", "Описание2", 200, 3)
    assert product1 + product2 == 100*2 + 200*3


def test_product_add_invalid_type():
    product = Product("Товар", "Описание", 100, 5)
    with pytest.raises(TypeError):
        product + "не продукт"
