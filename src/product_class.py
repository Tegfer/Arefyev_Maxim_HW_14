from class_stack import Product, AbstractProduct, MixinLog


class Smartphone(Product, AbstractProduct, MixinLog):
    __smartphone = []

    def __init__(self, name, description, price, quantity, efficiency, model, internal_storage, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.internal_storage = internal_storage
        self.color = color


class LawnGrass(Product, AbstractProduct, MixinLog):
    __lawn_grass = []

    def __init__(self, name, description, price, quantity, manufacturer, germination_rate, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.germination_rate = germination_rate
        self.color = color
