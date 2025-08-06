import pytest

from src.product import Product, Smartphone, LawnGrass


def test_create_product():
    product = Product("Телевизор", "60 дюймов, 4K", 30000.0, 10)
    assert product.name == "Телевизор"
    assert product.description == "60 дюймов, 4K"
    assert product.price == 30000.0
    assert product.quantity == 10


def test_price_setter_correct():
    product = Product("Телевизор", "60 дюймов, 4K", 30000.0, 10)
    product.price = 25000
    assert product.price == 25000


def test_price_setter_invalid(capfd):
    product = Product("Телевизор", "60 дюймов, 4K", 30000.0, 10)
    product.price = -100
    captured = capfd.readouterr()
    assert "Цена введена некорректно!" in captured.out


def test_str_product():
    product = Product("Телевизор", "60 дюймов, 4K", 30000.0, 10)
    assert str(product) == "Телевизор, 30000.0 руб. Остаток: 10 шт."


def test_product_addition():
    product1 = Product("Телевизор", "4K", 30000.0, 2)
    product2 = Product("Телевизор", "8K", 50000.0, 3)
    total = product1 + product2
    assert total == 30000*2 + 50000*3  # 60000 + 150000 = 210000
    assert total == 210000


def test_addition_different_types():
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 5, 95.0, "15", 256, "Черный")
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 20, "Россия", "7 дней", "Зелёный")
    with pytest.raises(TypeError):
        smartphone + grass


def test_create_smartphone():
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 5, 95.0, "15", 256, "Черный")
    assert smartphone.name == "iPhone"
    assert smartphone.description == "Смартфон"
    assert smartphone.price == 80000
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.0
    assert smartphone.model == "15"
    assert smartphone.memory == 256
    assert smartphone.color == "Черный"


def test_str_smartphone():
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 5, 95.0, "15", 256, "Черный")
    assert str(smartphone) == "iPhone, 80000 руб. Остаток: 5 шт."


def test_smartphone_addition():
    smartphone1 = Smartphone("iPhone", "Смартфон",
                             80000, 5, 95.0, "15", 256, "Черный")
    smartphone2 = Smartphone("Samsung", "Флагман",
                             70000, 3, 90.0, "S23", 512, "Серый")
    total = smartphone1 + smartphone2
    assert total == 80000*5 + 70000*3  # 400000 + 210000 = 610000
    assert total == 610000


def test_create_lawn_grass():
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 20, "Россия", "7 дней", "Зелёный")
    assert grass.name == "Газон"
    assert grass.description == "Зелёная трава"
    assert grass.price == 500
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зелёный"


def test_str_lawn_grass():
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 20, "Россия", "7 дней", "Зелёный")
    assert str(grass) == "Газон, 500 руб. Остаток: 20 шт."


def test_lawn_grass_addition():
    grass1 = LawnGrass("Газон", "Зелёная трава",
                       500, 20, "Россия", "7 дней", "Зелёный")
    grass2 = LawnGrass("Газон2", "Быстрорастущая",
                       400, 30, "Германия", "10 дней", "Светло-зелёный")
    total = grass1 + grass2
    assert total == 500*20 + 400*30  # 10000 + 12000 = 22000
    assert total == 22000


def test_inheritance():
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 5, 95.0, "15", 256, "Черный")
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 20, "Россия", "7 дней", "Зелёный")
    assert isinstance(smartphone, Product)
    assert isinstance(grass, Product)
