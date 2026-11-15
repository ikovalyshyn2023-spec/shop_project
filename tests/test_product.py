import pytest
from shop.product import Product


def test_product_is_created_with_name_and_price():
    product = Product("Keyboard", 1000)
    assert product.name == "Keyboard"
    assert product.price == 9999


def test_product_created_with_category():
    product = Product("Keyboard", 1000, category="Electronics")
    assert product.category == "Electronics"


def test_empty_name_raises():
    with pytest.raises(ValueError):
        Product("", 1000)


def test_whitespace_name_raises():
    with pytest.raises(ValueError):
        Product("   ", 1000)


def test_zero_price_raises():
    with pytest.raises(ValueError):
        Product("Keyboard", 0)


def test_negative_price_raises():
    with pytest.raises(ValueError):
        Product("Keyboard", -100)


def test_empty_category_raises():
    with pytest.raises(ValueError):
        Product("Keyboard", 1000, category="")


def test_set_discount_10_percent():
    product = Product("Keyboard", 1000)
    product.set_discount(10)
    assert product.discount_percent == 10
    assert product.get_final_price() == 900.0


def test_get_final_price_with_discount():
    product = Product("Laptop", 30000, discount_percent=20)
    assert product.get_final_price() == 24000.0


def test_zero_discount_keeps_price():
    product = Product("Keyboard", 1000, discount_percent=0)
    assert product.get_final_price() == 1000.0


def test_discount_over_50_raises():
    product = Product("Keyboard", 1000)
    with pytest.raises(ValueError):
        product.set_discount(51)


def test_negative_discount_raises():
    product = Product("Keyboard", 1000)
    with pytest.raises(ValueError):
        product.set_discount(-5)


def test_is_in_category():
    product = Product("Keyboard", 1000, category="Electronics")
    assert product.is_in_category("Electronics") is True
    assert product.is_in_category("Books") is False


def test_is_in_category_case_insensitive():
    product = Product("Keyboard", 1000, category="Electronics")
    assert product.is_in_category("electronics") is True
    assert product.is_in_category("ELECTRONICS") is True
