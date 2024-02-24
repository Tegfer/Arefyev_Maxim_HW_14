from src.class_stack import Category


def test_numberofcategory():
    amber = Category("Amber", "crystallized sap", 500)
    ruby = Category("Ruby", "crystal", 50)
    assert Category.numbers_of_category == 2