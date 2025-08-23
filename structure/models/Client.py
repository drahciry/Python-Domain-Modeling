# Import custom classes
from .Email import Email
from .Address import Address
from ..exceptions.InvalidIdError import InvalidIdError
from ..exceptions.InvalidNameError import InvalidNameError
from ..exceptions.InvalidEmailError import InvalidEmailError
from ..exceptions.InvalidAddressError import InvalidAddressError

# Class implementation
class Client:
    """
    Represents a client with id, name, surname, and email.
    """
    def __init__(self, id_client: int, name: str, surname: str, email: Email, address: Address):
        """
        Initialize a Client instance with validated attributes.

        Args:
            id_client (int): Unique identifier for the client. Must be a positive integer.
            name (str): First name of the client. Must be a non-empty string.
            surname (str): Surname of the client. Must be a non-empty string.
            email (Email): Email object representing the client's email.
            address (Address): Address object representing the client's address.

        Raises:
            InvalidIdError: If id_client is not a positive integer.
            InvalidNameError: If name or surname is not a non-empty string.
            InvalidEmailError: If email is not an Email object.
            InvalidAddressError: If address is not an Address object.
        """
        self.id_client = id_client
        self.id_client_int = id_client
        self.name = name
        self.surname = surname
        self.email = email
        self.address = address
        
    # ----- Properties -----
        
    @property
    def id_client(self) -> str:
        """
        Get the client's unique identifier.

        Returns:
            int: The client's id.
        """
        return self.__id_client

    @id_client.setter
    def id_client(self, id_client: int):
        """
        Set the client's unique identifier with validation.

        Args:
            id_client (int): The new id value.

        Raises:
            InvalidIdError: If id_client is not a positive integer.
        """
        if not isinstance(id_client, int) or id_client <= 0:
            raise InvalidIdError("id_client must be a positive integer.")
        self.__id_client = f'C{id_client}'  # Format id with 'C' prefix
        
    @property
    def id_client_int(self):
        """
        Get the client's unique identifier.

        Returns:
            str: The client's id.
        """
        return self.__id_client_int
    
    @id_client_int.setter
    def id_client_int(self, id_client: int):
        """
        Set the client's unique identifier with validation.

        Args:
            id_client (int): The new id id_client.

        Raises:
            InvalidIdError: If id_client is not a positive integer.
        """
        if not isinstance(id_client, int) or id_client <= 0:
            raise InvalidIdError("id_client must be a positive integer.")
        self.__id_client_int = id_client

    @property
    def name(self) -> str:
        """
        Get the client's first name.

        Returns:
            str: The client's first name.
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Set the client's first name with validation.

        Args:
            name (str): The new name value.

        Raises:
            InvalidNameError: If name is not a non-empty string.
        """
        if not isinstance(name, str) or not name.strip():
            raise InvalidNameError("name must be a non-empty string.")
        self.__name = name.strip()

    @property
    def surname(self) -> str:
        """
        Get the client's surname.

        Returns:
            str: The client's surname.
        """
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        """
        Set the client's surname with validation.

        Args:
            surname (str): The new surname value.

        Raises:
            InvalidNameError: If surname is not a non-empty string.
        """
        if not isinstance(surname, str) or not surname.strip():
            raise InvalidNameError("surname must be a non-empty string.")
        self.__surname = surname.strip()

    @property
    def email(self) -> Email:
        """
        Get the client's email object.

        Returns:
            Email: The client's email object.
        """
        return self.__email

    @email.setter
    def email(self, email: Email):
        """
        Set the client's email with validation.

        Args:
            email (Email): The new email object.

        Raises:
            ValueError: If email is not an Email object.
        """
        if not isinstance(email, Email):
            raise InvalidEmailError("email must be an Email object.")
        self.__email = email
        
    @property
    def address(self) -> Address:
        """
        Get the client's address object.

        Returns:
            Address: The client's address object.
        """
        return self.__address
    
    @address.setter
    def address(self, address: Address):
        """
        Set the client's address with validation.

        Args:
            address (Address): The new address object.

        Raises:
            InvalidAddressError: If address is not an Address object.
        """
        if not isinstance(address, Address):
            raise InvalidAddressError("address must be an Address object.")
        self.__address = address

    # ----- Dunder Methods -----

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the client.

        Returns:
            str: String representation of the client.
        """
        return (f"Client(id={self.id_client}, name='{self.name}', surname='{self.surname}', "
                f"email={self.email}), address={self.address}")

    def __repr__(self) -> str:
        """
        Return the official string representation of the Client object.

        Returns:
            str: Official string representation of the client.
        """
        return (f"Client(id_client={self.id_client[1:]}, name='{self.name}', "
                f"surname='{self.surname}', email={repr(self.email)}), address={repr(self.address)}")

    def __eq__(self, other) -> bool:
        """
        Compare this Client object with another Client.

        Args:
            other (Any): Another Client object.

        Returns:
            bool: True if all attributes are equal, False otherwise.
        """
        if not isinstance(other, Client):
            return NotImplemented
        return (
            self.id_client == other.id_client and
            self.name == other.name and
            self.surname == other.surname and
            self.email == other.email and
            self.address == other.address
        )