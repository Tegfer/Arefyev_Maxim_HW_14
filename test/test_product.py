from src.class_stack import Product


def test_product():
    amber = Product("Amber", "crystallized sap", 500, "5")
    assert amber.name == "Amber"
    assert amber.description == "crystallized sap"
    assert amber._price == 500
    assert amber.quantity == "5"
