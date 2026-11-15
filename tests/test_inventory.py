import pytest
from shop.product import Product
from shop.inventory import Inventory


def test_add_new_product():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 5)
    assert inv.get_quantity(p) == 5


def test_add_same_product_increases():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 3)
    inv.add_product(p, 2)
    assert inv.get_quantity(p) == 5


def test_get_quantity():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 7)
    assert inv.get_quantity(p) == 7


def test_is_available_true():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 5)
    assert inv.is_available(p, 3) is True


def test_is_available_false():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 2)
    assert inv.is_available(p, 5) is False


def test_remove_product():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 5)
    inv.remove_product(p, 2)
    assert inv.get_quantity(p) == 3


def test_remove_more_than_stock_raises():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 2)
    with pytest.raises(ValueError):
        inv.remove_product(p, 5)


def test_product_not_in_stock_quantity_zero():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    assert inv.get_quantity(p) == 0


def test_add_zero_quantity_raises():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    with pytest.raises(ValueError):
        inv.add_product(p, 0)


def test_remove_negative_quantity_raises():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 5)
    with pytest.raises(ValueError):
        inv.remove_product(p, -1)


def test_custom_low_stock_limit():
    inv = Inventory(low_stock_limit=5)
    assert inv.low_stock_limit == 5


def test_negative_low_stock_limit_raises():
    with pytest.raises(ValueError):
        Inventory(low_stock_limit=-1)


def test_get_low_stock_products():
    inv = Inventory(low_stock_limit=3)
    p1 = Product("Keyboard", 1000)
    p2 = Product("Mouse", 500)
    inv.add_product(p1, 2)
    inv.add_product(p2, 10)
    low = inv.get_low_stock_products()
    assert p1 in low
    assert p2 not in low


def test_product_equal_to_limit_is_low():
    inv = Inventory(low_stock_limit=3)
    p = Product("Keyboard", 1000)
    inv.add_product(p, 3)
    assert p in inv.get_low_stock_products()


def test_product_above_limit_not_low():
    inv = Inventory(low_stock_limit=3)
    p = Product("Keyboard", 1000)
    inv.add_product(p, 4)
    assert p not in inv.get_low_stock_products()


def test_remove_last_unit_leaves_zero():
    inv = Inventory()
    p = Product("Keyboard", 1000)
    inv.add_product(p, 1)
    inv.remove_product(p, 1)
    assert inv.get_quantity(p) == 0
