from src.class_stack import Product


def test_product():
    amber = Product("Amber", "crystallized sap", 500, 5)
    ruby = Product("Ruby", "crystal", 50, 4)
    assert Product.numbers_of_products == 2