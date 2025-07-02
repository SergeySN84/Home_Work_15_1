import pytest

from src.product import Product


def test_product_initialization():
    product = Product("Samsung Galaxy S23", "256GB, Серый", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23"
    assert product.description == "256GB, Серый"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str_representation():
    product = Product("Samsung Galaxy S23", "256GB, Серый", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт."


def test_product_addition():
    product1 = Product("Samsung Galaxy S23", "", 180000.0, 5)
    product2 = Product("Iphone 15", "", 210000.0, 8)
    total = product1 + product2
    expected = (180000.0 * 5) + (210000.0 * 8)
    assert total == expected


def test_product_add_invalid_type_raises_error():
    product = Product("Samsung Galaxy S23", "", 180000.0, 5)
    with pytest.raises(TypeError):
        product + "not a product"
