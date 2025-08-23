# Import custom classes
from .Price import Price
from ..exceptions.InvalidIdError import InvalidIdError
from ..exceptions.InvalidNameError import InvalidNameError
from ..exceptions.InvalidPriceError import InvalidPriceError
from ..exceptions.InvalidCategoryError import InvalidCategoryError
from ..exceptions.InvalidQuantityError import InvalidQuantityError

# Class implementation
class Product:
    """
    Class to represent a product with id, name, category, price, and quantity.
    """

    def __init__(self, id_product: int, name: str, category: str, price: Price, quantity: int):
        """
        Initialize a Product instance with validated attributes.

        Args:
            id_product (int): Unique identifier for the product. Must be a positive integer.
            name (str): Name of the product. Must be a non-empty string.
            category (str): Category of the product. Must be a non-empty string.
            price (Price): Price object representing the product's price.
            quantity (int): Quantity of the product in stock. Must be a non-negative integer.

        Raises:
            InvalidIdError: If value is not a positive integer.
            InvalidNameError: If value is not a non-empty string.
            InvalidCategoryError: If category value is not a non-empty string.
            InvalidPriceError: If value is not a Price object.
            InvalidQuantityError: If value is not a non-negative integer.
        """
        self.id_product = id_product
        self.id_product_int = id_product
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    # ----- Properties -----

    @property
    def id_product(self) -> str:
        """
        Get the product's unique identifier.

        Returns:
            str: The product's id.
        """
        return self.__id_product

    @id_product.setter
    def id_product(self, id_product: int):
        """
        Set the product's unique identifier with validation.

        Args:
            id_product (int): The new id id_product.

        Raises:
            InvalidIdError: If id_product is not a positive integer.
        """
        if not isinstance(id_product, int) or id_product <= 0:
            raise InvalidIdError("id_product must be a positive integer.")
        self.__id_product = f'P{id_product}' # Format id with 'P' prefix 
        
    @property
    def id_product_int(self):
        """
        Get the product's unique identifier.

        Returns:
            str: The product's id.
        """
        return self.__id_product_int
    
    @id_product_int.setter
    def id_product_int(self, id_product: int):
        """
        Set the product's unique identifier with validation.

        Args:
            id_product (int): The new id id_product.

        Raises:
            InvalidIdError: If id_product is not a positive integer.
        """
        if not isinstance(id_product, int) or id_product <= 0:
            raise InvalidIdError("id_product must be a positive integer.")
        self.__id_product_int = id_product

    @property
    def name(self) -> str:
        """
        Get the product's name.

        Returns:
            str: The product's name.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Set the product's name with validation.

        Args:
            name (str): The new name value.

        Raises:
            InvalidNameError: If name is not a non-empty string.
        """
        if not isinstance(name, str) or not name.strip():
            raise InvalidNameError("name must be a non-empty string.")
        self.__name = name.strip()

    @property
    def category(self) -> str:
        """
        Get the product's category.

        Returns:
            str: The product's category.
        """
        return self.__category

    @category.setter
    def category(self, category: str):
        """
        Set the product's category with validation.

        Args:
            category (str): The new category value.

        Raises:
            InvalidCategoryError: If category is not a non-empty string.
        """
        if not isinstance(category, str) or not category.strip():
            raise InvalidCategoryError("category must be a non-empty string.")
        self.__category = category.strip()

    @property
    def price(self) -> Price:
        """
        Get the product's price.

        Returns:
            Price: The product's price object.
        """
        return self.__price

    @price.setter
    def price(self, price: Price):
        """
        Set the product's price with validation.

        Args:
            price (Price): The new price object.

        Raises:
            InvalidPriceError: If price is not a Price object.
        """
        if not isinstance(price, Price):
            raise InvalidPriceError("price must be a Price object.")
        self.__price = price

    @property
    def quantity(self) -> int:
        """
        Get the product's quantity in stock.

        Returns:
            int: The product's quantity.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """
        Set the product's quantity with validation.

        Args:
            quantity (int): The new quantity value.

        Raises:
            InvalidQuantityError: If quantity is not a non-negative integer.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise InvalidQuantityError("quantity must be a non-negative integer.")
        self.__quantity = quantity
        
    # ----- Dunder Methods -----

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the product.

        Returns:
            str: String representation of the product.
        """
        return (f"Product(id={self.id_product}, name='{self.name}', category='{self.category}', "
                f"price={self.price}, quantity={self.quantity})")

    def __repr__(self) -> str:
        """
        Return the official string representation of the Product object.

        Returns:
            str: Official string representation of the product.
        """
        return (f"Product(id_product={self.id_product}, name='{self.name}', "
                f"category='{self.category}', price={repr(self.price)}, quantity={self.quantity})")
        
    def __eq__(self, other) -> bool:
        """
        Check if two Product instances are equal.

        Args:
            other (Product): Another Product instance to compare.

        Returns:
            bool: True if all attributes are equal, False otherwise.
        """
        if not isinstance(other, Product):
            return NotImplemented
        return (
            self.id_product == other.id_product and
            self.name == other.name and
            self.category == other.category and
            self.price == other.price and
            self.quantity == other.quantity
        )