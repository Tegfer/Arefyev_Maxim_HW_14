from src.class_stack import Category


def test_category():
    amber = Category("Jewelery", "Raw gems", 5)
    assert amber.name == "Jewelery"
    assert amber.description == "Raw gems"
    assert amber.__products == 5
