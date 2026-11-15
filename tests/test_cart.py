import pytest
from shop.product import Product
from shop.cart import ShoppingCart


def test_new_cart_is_empty():
    cart = ShoppingCart()
    assert cart.is_empty() is True
    assert cart.get_item_count() == 0


def test_add_one_product():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p)
    assert cart.get_item_count() == 1
    assert cart.get_items()[p] == 1


def test_add_two_different_products():
    cart = ShoppingCart()
    p1 = Product("Keyboard", 1000)
    p2 = Product("Mouse", 500)
    cart.add_product(p1)
    cart.add_product(p2)
    assert cart.get_item_count() == 2


def test_add_same_product_increases_quantity():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p, 1)
    cart.add_product(p, 2)
    assert cart.get_items()[p] == 3


def test_get_total():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p)
    assert cart.get_total() == 1000.0


def test_get_total_with_quantity():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p, 3)
    assert cart.get_total() == 3000.0


def test_remove_product():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p)
    cart.remove_product(p)
    assert cart.is_empty() is True


def test_partial_remove():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p, 5)
    cart.remove_product(p, 2)
    assert cart.get_items()[p] == 3


def test_remove_more_than_in_cart_raises():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p, 2)
    with pytest.raises(ValueError):
        cart.remove_product(p, 5)


def test_get_item_count():
    cart = ShoppingCart()
    p1 = Product("Keyboard", 1000)
    p2 = Product("Mouse", 500)
    cart.add_product(p1, 2)
    cart.add_product(p2, 3)
    assert cart.get_item_count() == 5


def test_clear():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p)
    cart.set_coupon(10)
    cart.clear()
    assert cart.is_empty() is True
    assert cart.get_total() == 0


def test_zero_quantity_raises():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    with pytest.raises(ValueError):
        cart.add_product(p, 0)


def test_negative_quantity_raises():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    with pytest.raises(ValueError):
        cart.add_product(p, -1)


def test_coupon_10_percent():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p)
    cart.set_coupon(10)
    assert cart.get_total() == 900.0


def test_coupon_over_20_raises():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.set_coupon(25)


def test_total_with_product_discount():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000, discount_percent=10)
    cart.add_product(p)
    assert cart.get_total() == 900.0


def test_total_with_product_and_coupon_discount():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000, discount_percent=10)
    cart.add_product(p)
    cart.set_coupon(10)
    assert cart.get_total() == 810.0


def test_clear_resets_coupon():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p)
    cart.set_coupon(10)
    cart.clear()
    cart.add_product(p)
    assert cart.get_total() == 1000.0


def test_get_items_returns_copy():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p, 2)
    items = cart.get_items()
    items[p] = 100
    assert cart.get_items()[p] == 2


def test_remove_product_not_in_cart_raises():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    with pytest.raises(ValueError):
        cart.remove_product(p)


def test_partial_remove_to_zero():
    cart = ShoppingCart()
    p = Product("Keyboard", 1000)
    cart.add_product(p, 2)
    cart.remove_product(p, 2)
    assert cart.is_empty() is True
