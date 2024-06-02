from src.class_fixture import testing_product
from  src.class_stack import Product


def test_productadd(test_product):
    new_product = testing_product.add_product({"name": "Emerald", "description": "Green crystal", 'price': 2000, "quantity": 15})
    testing_product.add_product({"name": "Emerald ", "description": "Green crystal", "price": 1600, "quantity": 30})
    assert new_product.name == "Emerald"
    assert new_product.description == "Green crystal"
    assert new_product.price == 1600.0
    assert new_product.quantity == 45
    assert test_product.add_product(
        {"name": "Emerald", "description": "Green crystal", "price": 1600.0, "quantity": -30}) is None
