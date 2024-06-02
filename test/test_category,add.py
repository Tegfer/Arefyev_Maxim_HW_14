from src.class_fixture import category_placeholder


def test_categoryadd(category_placeholder):
    assert category_placeholder.name == "Jewelery"
    assert category_placeholder.description == "Raw gems"
    assert category_placeholder.quantity_unique_products == 2

    assert category_placeholder.get_products == ["Amber", "crystallized sap", 500, 5,
                                               "Garnet", "fiery-red cristal", 2000, 9]
    assert len(category_placeholder) == 10
    assert str(category_placeholder) == 'Jewelery, количество продуктов: 14 шт.'
