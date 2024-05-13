import decoding


class Product:
    """
    The product class of any store
    """
    def __init__(self, barcode):
        """
        Initializes a Product instance with barcode information
        :param barcode: str, a string containing the barcode information
        """
        self.__country = decoding.barcodes[barcode[:3]]
        self.__manufacturer = decoding.barcodes[barcode[3:7]]
        self.__product = decoding.barcodes[barcode[7:12]]
        self.__check_digit = barcode[-1]
        self.__price = 0

    @property
    def price(self):
        """
        Getter method for the price of the product
        :return: float, the price of the product
        """
        return self.__price

    @price.setter
    def price(self, other):
        """
        Setter method for the price of the product
        :param other: float, the new price of the product
        """
        self.__price = other

    @price.getter
    def price(self):
        """
        Getter method for the price of the product
        :return: float, the price of the product
        """
        return self.__price

    def __str__(self):
        """
        Returns a string representation of the Product instance
        :return: str, a string representation of the Product
        """
        return f'{self.__product}    {self.__country} / {self.__manufacturer} / {self.__price} /'

    def __repr__(self):
        """
        Returns a string representation of the Product instance
        :return: str, a string representation of the Product
        """
        return self.__str__()


class Cart:
    """
    Class of a shopping cart
    """
    total_cost = 0
    all_cart = []

    def __init__(self, product):
        """
        Initializes a Cart instance with a product
        :param product: Product, the product to be added to the cart
        """
        self.__product = product
        if product not in Cart.all_cart:
            Cart.all_cart.append(self)

    @staticmethod
    def counter():
        """
        Calculates the total cost of items in the cart
        """
        Cart.total_cost = 0
        for line in Cart.all_cart:
            price = str(line).split('/')[2][1:].rstrip()
            Cart.total_cost += int(price)

    @staticmethod
    def write():
        """
        Writes the cart contents to a file
        """
        with open('cart.txt', 'w') as file_cart:
            print('Product name |Country |Manufacturer |Price|', file=file_cart)
            for product in Cart.all_cart:
                print(product, file=file_cart)

    def __str__(self):
        """
        Returns a string representation of the Cart instance
        :return: str, a string representation of the Cart
        """
        return f'-{self.__product}\n'

    def __repr__(self):
        """
        Returns a string representation of the Cart instance
        :return: str, a string representation of the Cart
        """
        return self.__str__()
