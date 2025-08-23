# Import custom classes
from ..exceptions.InvalidCityError import InvalidCityError
from ..exceptions.InvalidStateError import InvalidStateError

# Class implementation
class Address:
    """
    Represents an address with city and state attributes.
    """

    def __init__(self, city: str, state: str):
        """
        Initializes an Address instance.

        Args:
            city (str): The name of the city.
            state (str): The name of the state.
        Raises:
            InvalidCityError: If city is not a non-empty string.
            InvalidStateError: If state is not a valid Brazilian state abbreviation or not a non-empty string.
        """
        self.__all_states = {
            'AC': 'Acre', 
            'AL': 'Alagoas',
            'AP': 'Amapá',
            'AM': 'Amazonas',
            'BA': 'Bahia',
            'CE': 'Ceará',
            'ES': 'Espiríto Santo',
            'GO': 'Goiás',
            'MA': 'Maranhão',
            'MT': 'Mato Grosso',
            'MS': 'Mato Grosso do Sul',
            'MG': 'Minas Gerais',
            'PA': 'Pará',
            'PB': 'Paraíba',
            'PR': 'Paraná',
            'PE': 'Pernambuco',
            'PI': 'Piauí',
            'RJ': 'Rio de Janeiro',
            'RN': 'Rio Grande do Norte',
            'RS': 'Rio Grande do Sul',
            'RO': 'Rondônia',
            'RR': 'Roraima',
            'SC': 'Santa Catarina',
            'SP': 'São Paulo',
            'SE': 'Sergipe',
            'TO': 'Tocantins'
        }
        self.city = city
        self.state = state

    # ----- Properties -----

    @property
    def city(self) -> str:
        """
        Gets the city name.

        Returns:
            str: The city name.
        """
        return self.__city

    @city.setter
    def city(self, city: str):
        """
        Sets the city name.

        Args:
            city (str): The new city name.

        Raises:
            InvalidCityError: If city is not a non-empty string.
        """
        if not isinstance(city, str) or not city.strip():
            raise InvalidCityError('City must be a non-empty string.')
        self.__city = city

    @property
    def state(self) -> str:
        """
        Gets the state name.

        Returns:
            str: The state name.
        """
        return self.__state

    @state.setter
    def state(self, state: str):
        """
        Sets the state name.

        Args:
            state (str): The new state name.

        Raises:
            InvalidStateError: If state is not a valid Brazilian state abbreviation.
            InvalidStateError: If state is not a non-empty string.
        """
        if not isinstance(state, str) or not state.strip():
            raise InvalidStateError('State must be a non-empty string.')
        if state.upper() not in self.__all_states.keys():
            raise InvalidStateError('State must be a valid Brazilian state abbreviation.')
        self.__state = state.upper()

    # ----- Dunder Methods -----

    def __str__(self):
        """
        Returns a string representation of the Address.

        Returns:
            str: The address in 'city, state' format.
        """
        return f"{self.city}, {self.state}"

    def __repr__(self):
        """
        Returns an unambiguous string representation of the Address.

        Returns:
            str: The representation of the Address object.
        """
        return f"Address(city='{self.city}', state='{self.state}')"

    def __eq__(self, other):
        """
        Checks equality with another Address object.

        Args:
            other (Address): Another Address instance.

        Returns:
            bool: True if both city and state are equal, False otherwise.
        """
        if not isinstance(other, Address):
            return False
        return self.city == other.city and self.state == other.state