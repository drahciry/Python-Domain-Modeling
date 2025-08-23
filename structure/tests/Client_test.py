# Import custom classes
from ..models.Email import Email
from ..models.Client import Client
from ..models.Address import Address
from ..exceptions.InvalidIdError import InvalidIdError
from ..exceptions.InvalidNameError import InvalidNameError
from ..exceptions.InvalidEmailError import InvalidEmailError
from ..exceptions.InvalidAddressError import InvalidAddressError

# Import necessary libraries
import pytest

# Test function for the "happy path" scenario
@pytest.mark.parametrize(
    "id_client, name, surname, email, address",
    [
        # Test 1: Valid Client Data
        (1, "John", "Doe", Email("email.test@gmail.com"), Address(city="Rio de Janeiro", state="RJ")),
        # Test 2: Valid Client Data with Different Email and Address
        (2, "Jane", "Smith", Email("email2.test@gmail.com"), Address(city="Campinas", state="SP")),
        # Test 3: Valid Client Data with Another Different Email and Address
        (3, "Alice", "Johnson", Email("email3.test@gmail.com"), Address(city="Belo Horizonte", state="MG"))
    ]
)
def test_create_valid_client_object(id_client: int, name: str, surname: str, email: Email, address: Address):
    """
    Test that a valid Client object can be created successfully.
    """
    # Arrange: Create a valid client dictionary
    valid_client = {
        "id_client": id_client,
        "name": name,
        "surname": surname,
        "email": email,
        "address": address
    }
    # Act: Create a Client object using the valid client dictionary
    client = Client(**valid_client)
    # Assert: Check that the Client object is created successfully
    assert client.id_client[1:] == str(id_client)
    assert client.id_client_int == id_client
    assert client.name == name
    assert client.surname == surname
    assert client.email == email
    assert client.address == address
    
# Test function for the "unhappy path" scenario
@pytest.mark.parametrize(
    "id_client, name, surname, email, address, expected_exception",
    [
        # Test 1: Invalid ID (Negative Number)
        (-1, "John", "Doe", Email("email.test@gmail.com"), Address(city="Rio de Janeiro", state="RJ"), InvalidIdError),
        # Test 2: Invalid Name (Empty String)
        (1, "", "Doe", Email("email.test@gmail.com"), Address(city="Campinas", state="SP"), InvalidNameError),
        # Test 3: Invalid Surname (Non-string)
        (1, "John", 123, Email("email.test@gmail.com"), Address(city="Belo Horizonte", state="MG"), InvalidNameError),
        # Test 4: Invalid Email (Not an Email Object)
        (1, "John", "Doe", "not_an_email", Address(city="Salvador", state="BA"), InvalidEmailError),
        # Test 5: Invalid Address (Not an Address Object)
        (1, "John", "Doe", Email("email.test@gmail.com"), "not_an_address", InvalidAddressError),
        # Test 6: Invalid ID (Zero)
        (0, "John", "Doe", Email("email.test@gmail.com"), Address(city="Gramado", state="RS"), InvalidIdError),
        # Test 7: Invalid Name (Non-string)
        (1, None, "Doe", Email("email.test@gmail.com"), Address(city="Fortaleza", state="CE"), InvalidNameError),
        # Test 8: Invalid Surname (Non-string)
        (1, "John", [], Email("email.test@gmail.com"), Address(city="Vila Velha", state="ES"), InvalidNameError)
    ]
)
def test_create_invalid_client_object(id_client: int, name: str, surname: str, email: Email, address: Address, expected_exception: Exception):
    """
    Test that an invalid Client object cannot be created.
    """
    # Arrange: Create an invalid client dictionary
    invalid_client = {
        "id_client": id_client,
        "name": name,
        "surname": surname,
        "email": email,
        "address": address
    }
    # Act & Assert: Attempt to create a Client object and expect an exception
    with pytest.raises(expected_exception):
        Client(**invalid_client)