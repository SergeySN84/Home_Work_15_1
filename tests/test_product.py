import pytest
from unittest import mock
from io import StringIO


from src.product import Product, Smartphone, LawnGrass, BaseProduct


def test_product_is_abstract_base():

    """Проверка, что Product наследуется от
    BaseProduct и BaseProduct — абстрактный"""
    assert issubclass(Product, BaseProduct)
    assert hasattr(BaseProduct.get_description, "__isabstractmethod__")
    assert hasattr(BaseProduct.get_price, "__isabstractmethod__")


def test_product_inheritance():
    """Проверка цепочки наследования"""
    assert isinstance(Product("Товар", "Описание", 100, 5), BaseProduct)
    assert isinstance(Product("Товар", "Описание", 100, 5), Product)


def test_product_creation_logs(capfd):
    """Проверка, что при создании продукта выводится сообщение"""
    product = Product("Товар", "Описание", 100.0, 10)
    captured = capfd.readouterr()
    assert captured.out.strip() == "Product('Товар', 'Описание', 100.0, 10)"


def test_smartphone_creation_logs(capfd):
    """Проверка лога при создании смартфона"""
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 1, 95.0, "15", 256, "Черный")
    captured = capfd.readouterr()
    assert captured.out.strip() == "Product('iPhone', 'Смартфон', 80000, 1)"


def test_lawn_grass_creation_logs(capfd):
    """Проверка лога при создании газонной травы"""
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 20, "Россия", "7 дней", "Зелёный")
    captured = capfd.readouterr()
    assert captured.out.strip() == "Product('Газон', 'Зелёная трава', 500, 20)"


def test_product_attributes():
    """Проверка атрибутов продукта"""
    product = Product("Товар", "Описание", 100.0, 5)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 5


def test_product_str():
    """Проверка строкового представления"""
    product = Product("Товар", "Описание", 100.0, 5)
    assert str(product) == "Товар, 100.0 руб. Остаток: 5 шт."


def test_product_price_setter_correct(monkeypatch):
    """Проверка установки корректной цены,
    включая повышение и подтверждённое понижение"""
    product = Product("Товар", "Описание", 100.0, 5)

    # Подменяем input
    monkeypatch.setattr('builtins.input', lambda _: 'y')

    # Повышение — без вопроса
    product.price = 120.0
    assert product.price == 120.0

    # Понижение — с подтверждением
    product.price = 110.0
    assert product.price == 110.0


def test_product_price_setter_invalid(capfd):
    """Проверка установки некорректной цены"""
    product = Product("Товар", "Описание", 100.0, 5)
    product.price = -50
    captured = capfd.readouterr()
    assert "Цена введена некорректно!" in captured.out


def test_product_price_setter_decrease_confirmation(monkeypatch):
    """Проверка подтверждения понижения цены"""
    product = Product("Товар", "Описание", 100.0, 5)

    # Подменяем input на 'y'
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    with mock.patch('sys.stdout', new=StringIO()) as fake_out:
        product.price = 80.0
        assert "Цена успешно понижена." in fake_out.getvalue()

    assert product.price == 80.0


def test_product_price_setter_decrease_rejected(monkeypatch):
    """Проверка отмены понижения цены"""
    product = Product("Товар", "Описание", 100.0, 5)

    # Подменяем input на 'n'
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    with mock.patch('sys.stdout', new=StringIO()) as fake_out:
        product.price = 80.0
        assert "Цена не была изменена." in fake_out.getvalue()

    assert product.price == 100.0


def test_product_addition():
    """Проверка сложения продуктов"""
    product1 = Product("Товар1", "Описание", 100.0, 2)
    product2 = Product("Товар2", "Описание", 150.0, 3)
    total = product1 + product2
    assert total == 100*2 + 150*3  # 200 + 450 = 650
    assert total == 650


def test_product_addition_different_types():
    """Проверка сложения разных типов — должно быть TypeError"""
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 1, 95.0, "15", 256, "Черный")
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 20, "Россия", "7 дней", "Зелёный")
    with pytest.raises(TypeError):
        smartphone + grass


def test_product_count_increment():
    """Проверка счётчика product_count"""
    Product.product_count = 0  # Сброс
    p1 = Product("Товар1", "Описание", 100, 5)
    p2 = Product("Товар2", "Описание", 200, 3)
    assert Product.product_count == 2


def test_product_count_not_incremented_for_zero_quantity():
    """Счётчик не увеличивается при попытке создать товар с quantity <= 0"""
    Product.product_count = 0
    with pytest.raises(ValueError, match="Товар с нулевым"
                                         " количеством не "
                                         "может быть добавлен"):
        Product("Товар", "Описание", 100, 0)
    assert Product.product_count == 0


def test_smartphone_attributes():
    """Проверка уникальных атрибутов смартфона"""
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 1, 95.0, "15", 256, "Черный")
    assert smartphone.efficiency == 95.0
    assert smartphone.model == "15"
    assert smartphone.memory == 256
    assert smartphone.color == "Черный"


def test_lawn_grass_attributes():
    """Проверка уникальных атрибутов газонной травы"""
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 20, "Россия", "7 дней", "Зелёный")
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зелёный"


def test_implements_abstract_methods():
    """Проверка, что Product реализует абстрактные методы"""
    product = Product("Товар", "Описание", 100, 5)
    assert product.get_description() == "Описание"
    assert product.get_price() == 100


def test_smartphone_is_product():
    """Проверка, что Smartphone — это Product"""
    smartphone = Smartphone("iPhone", "Смартфон",
                            80000, 1, 95.0, "15", 256, "Черный")
    assert isinstance(smartphone, Product)
    assert isinstance(smartphone, BaseProduct)


def test_lawn_grass_is_product():
    """Проверка, что LawnGrass — это Product"""
    grass = LawnGrass("Газон", "Зелёная трава",
                      500, 20, "Россия", "7 дней", "Зелёный")
    assert isinstance(grass, Product)
    assert isinstance(grass, BaseProduct)


def test_product_create_with_zero_quantity():
    """Проверка, что при создании товара с
    quantity=0 выбрасывается ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством"
                                         " не может быть добавлен"):
        Product("Товар", "Описание", 100.0, 0)


def test_product_create_with_negative_quantity():
    """Проверка, что при создании товара с отрицательным
    quantity выбрасывается ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством"
                                         " не может быть добавлен"):
        Product("Товар", "Описание", 100.0, -5)
