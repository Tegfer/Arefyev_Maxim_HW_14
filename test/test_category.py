from src.class_stack import Category


def test_category():
    amber = Category("Amber", "crystallized sap", 500)
    assert amber.name == "Amber"
    assert amber.description == "crystallized sap"
    assert amber.__products == 500
