from abc import ABC, abstractmethod


class Category:
    numbers_of_category = 0
    "Список товаров"
    __products = []

    def __init__(self, name, description, number_of_products):
        self.name = name
        self.description = description
        self.__products = number_of_products
        Category.numbers_of_category += 1

    def add_ware(self, wares):
        if wares not in self.__products:
            self.__products.append(wares)
        return self.__products

    @property
    def ware_list(self):
        products_list = []
        for product in self.__products:
            if product not in products_list:
                products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.number_of} шт.")
        return products_list

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.__products}"

    def __len__(self):
        return f"{self.name}, колличество продуктов: {len(self.__products)}"

    def avg_price(self):
        try:
            avg_price = round(sum([i.price for i in self.__products]) / len(self.__products), 2)
            return avg_price
        except ZeroDivisionError:
            return 0


class ZeroProductQuantity(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Количество товара не может быть менее 1"

    def __str__(self):
        return self.message


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    def add_product(cls, product):
        pass


class MixinLog:
    def __repr__(self):
        attributes = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"Создан объект {self.__class__.__name__}({', '.join(attributes)})"


class Product(AbstractProduct, MixinLog):
    numbers_of_products = 0
    __products = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        Product.numbers_of_products += 1

    @classmethod
    def add_product(cls, ware):
        prdct = cls(**ware)
        try:
            if prdct.quantity > 0:
                for i in cls.__products:
                    if i.name == prdct.name:
                        i.quantity += prdct.quantity
                        i._price = max(i._price, prdct._price)
                        return i
                cls.__products.append(prdct)
                return prdct
            raise ZeroProductQuantity()
        except ZeroProductQuantity as e:
            print(e)
        else:
            print("Товар добавлен")
        finally:
            print("Обработка товара завершена")

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
    def price(self):
        return self._price

    @property
    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self._price * self.quantity + other._price * other.quantity
        return print("Нельзя складывать товары из разных категорий")


class ZeroProductQuantity(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Количество товара не может быть менее 1"

    def __str__(self):
        return self.message
