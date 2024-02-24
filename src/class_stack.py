class Category:
    numbers_of_category = 0

    def __init__(self, name, description, ware):
        self.name = name
        self.description = description
        self.ware = ware
        Category.numbers_of_category += 1


class Product:
    numbers_of_products = 0

    def __init__(self, name, description, price, number_of):
        self.name = name
        self.description = description
        self.price = price
        self.number_of = number_of
        Product.numbers_of_products += 1
