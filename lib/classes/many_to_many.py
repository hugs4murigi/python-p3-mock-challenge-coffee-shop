class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) < 3:
            raise ValueError("Name length must be greater or equal to 3 characters")
        self.__name = name
        self.__orders = []
        self.__customers = set()

    @property
    def name(self):
        return self.__name

    def orders(self):
        return self.__orders

    def customers(self):
        return list(self.__customers)

    def num_orders(self):
        return len(self.__orders)

    def average_price(self):
        if not self.__orders:
            return 0
        total_price = sum(order.price for order in self.__orders)
        return total_price / len(self.__orders)

    def add_order(self, order):
        self.__orders.append(order)
        self.__customers.add(order.customer)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters, inclusive")
        self.__name = name
        self.__orders = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters, inclusive")
        self.__name = value

    def orders(self):
        return self.__orders

    def coffees(self):
        return list(set(order.coffee for order in self.__orders))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self.__orders.append(order)
        coffee.add_order(order)
        return order


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be of type Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be of type Coffee")
        if not isinstance(price, float):
            raise TypeError("Price must be of type float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be a number between 1.0 and 10.0, inclusive")
        self.__customer = customer
        self.__coffee = coffee
        self.__price = price
        self.all.append(self)

    @property
    def price(self):
        return self.__price

    @property
    def customer(self):
        return self.__customer

    @property
    def coffee(self):
        return self.__coffee