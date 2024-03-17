class Category:
    numbers_of_category = 0
    "Список товаров"
    __ware_list = []

    def __init__(self, name, description, wares):
        self.name = name
        self.description = description
        self.wares = wares
        Category.numbers_of_category += 1

    def add_ware(self, wares):
        if wares not in self.wares:
            self.wares.append(wares)
        return self.wares

    @property
    def ware_list(self):
        products_list = []
        for product in self.wares:
            if product not in products_list:
                products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.number_of} шт.")
        return products_list

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.wares}"

    def __len__(self):
        return f"{self.name}, колличество продуктов: {len(Product.self.quantity)}"


class Product:
    numbers_of_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        Product.numbers_of_products += 1

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price >= self._price:
                self._price = new_price
                print("Успешно")
            elif new_price < self._price and input("Вы хотите понизить цену? y/n") == 'y':
                self._price = new_price
                print("Цена понижена")
            else:
                print("Отмена")
        else:
            print("Введена некорректная цена")

    @property
    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self._price * self.quantity + other._price * other.quantity