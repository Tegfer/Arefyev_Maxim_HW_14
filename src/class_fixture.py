import pytest
from src.class_stack import Category, Product


@pytest.fixture(scope='class')
def category_placeholder():
    return Category("Jewelery", "Raw gems", [Product("Amber", "crystallized sap", 500, 5),
                                             Product("Garnet", "fiery-red cristal", 2000, 9)])


@pytest.fixture(scope='class')
def testing_product():
    return Product("Amber", "crystallized sap", 500, 5)
