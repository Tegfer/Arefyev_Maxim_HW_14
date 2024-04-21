from class_stack import Product


class Smartphone(Product):
    __smartphone = []

    def __init__(self, name, description, price, quantity, efficiency, model, internal_storage, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.internal_storage = internal_storage
        self.color = color

    @classmethod
    def add_product(cls, product):
        added_product = cls(product["name"], product["description"], product["price"], product["quantity"], product["efficiency"], product["model"], product["internal_storage"], product["color"])

        for i in cls.__smartphone:
            if i.name == added_product.name:
                i.quantity += added_product.quantity
                i._price = max(i._price, added_product._price)
                return i
        cls.__smartphone.append(added_product)
        return added_product


class LawnGrass(Product):
    __lawn_grass = []

    def __init__(self, name, description, price, quantity, manufacturer, germination_rate, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.germination_rate = germination_rate
        self.color = color

    @classmethod
    def add_product(cls, product):
        added_product = cls(product["name"], product["description"], product["price"], product["quantity"], product["manufacturer"], product["germination_rate"], product["color"])

        for i in cls.__lawn_grass:
            if i.name == added_product.name:
                i.quantity += added_product.quantity
                i._price = max(i._price, added_product._price)
                return i
        cls.__lawn_grass.append(added_product)
        return added_product
