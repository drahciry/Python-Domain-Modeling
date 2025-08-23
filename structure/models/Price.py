# Import custom classes
from ..exceptions.InvalidPriceError import InvalidPriceError

# Import libs
from decimal import Decimal, InvalidOperation

# Class implementation
class Price:
    """Class to represent and validate a price value."""
    def __init__(self, price: str):
        """
        Constructor method.

        Args:
            price (str): Price as a string for processing.
        Raises:
            InvalidPriceError: If the input is not a valid, positive decimal string.
            InvalidOperation: if string passed is not a decimal number
        """
        self.price = price

    # ----- Properties -----
    
    @property
    def price(self):
        """
        Get the current price value.

        Returns:
            Decimal: The validated price value.
        """
        return self.__price
    
    @price.setter
    def price(self, price: str):
        """
        Set or update the price value after validation.

        Args:
            price (str): Price as a string.

        Raises:
            InvalidPriceError: If the input is not a valid, positive decimal string.
            InvalidOperation: if string passed is not a decimal number
        """
        # Check if input is valid
        if not isinstance(price, str) or not price.strip():
            raise InvalidPriceError('Invalid price input (empty or null string).')
        # Check if input is numeric
        try:
            value = Decimal(price)
        except InvalidOperation:
            raise InvalidPriceError('Value is not a valid decimal number.')
        # Check if input is positive
        if value <= 0:
            raise InvalidPriceError('Value must be a positive decimal number.')
        self.__price = value
        
    # ----- Dunder Methods -----
        
    def __str__(self):
        """Return the string representation of the price."""
        return f"{self.__price:.2f}"

    def __repr__(self):
        """Return the official string representation of the Price object."""
        return f"Price('{str(self.__price)}')"

    def __eq__(self, other):
        """Check if two Price objects are equal."""
        if isinstance(other, Price):
            return self.__price == other.__price
        if isinstance(other, str) and other.strip():
            return str(self.__price) == other
        return NotImplemented

    def __lt__(self, other):
        """Check if this Price is less than another."""
        if isinstance(other, Price):
            return self.__price < other.__price
        return NotImplemented

    def __le__(self, other):
        """Check if this Price is less than or equal to another."""
        if isinstance(other, Price):
            return self.__price <= other.__price
        return NotImplemented

    def __gt__(self, other):
        """Check if this Price is greater than another."""
        if isinstance(other, Price):
            return self.__price > other.__price
        return NotImplemented

    def __ge__(self, other):
        """Check if this Price is greater than or equal to another."""
        if isinstance(other, Price):
            return self.__price >= other.__price
        return NotImplemented

    def __add__(self, other):
        """Add two Price objects."""
        if isinstance(other, Price):
            return Price(str(self.__price + other.__price))
        return NotImplemented

    def __sub__(self, other):
        """Subtract one Price from another."""
        if isinstance(other, Price):
            result = self.__price - other.__price
            if result <= 0:
                raise InvalidPriceError('Resulting price must be positive.')
            return Price(str(result))
        return NotImplemented