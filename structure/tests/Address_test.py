# Import custom classes
from ..models.Address import Address
from ..exceptions.InvalidCityError import InvalidCityError
from ..exceptions.InvalidStateError import InvalidStateError

# Import necessary libraries
import pytest

# Test function for the "happy path" scenario
@pytest.mark.parametrize(
    "city, state",
    [
        # Test 1: City = Rio de Janeiro; State = RJ
        ("Rio de Janeiro", "RJ"),
        # Test 2: City = Campinas; State = SP
        ("Campinas", "SP"),
        # Test 3: City = Salvador; State = BA
        ("Salvador", "BA")
    ]
)
def test_create_valid_address_object(city: str, state: str):
    """
    Test that a valid Address object can be created successfully.
    """
    # Arrange: Create a valid address dictionary
    valid_address = {
        "city": city,
        "state": state
    }
    # Act: Create an Address object using the valid address dictionary
    address = Address(**valid_address)
    # Assert: Check that the Address object is created successfully
    assert address.city == city
    assert address.state == state
    
# Test function for the "unhappy path" scenario
@pytest.mark.parametrize(
    "city, state, expected_exception",
    [
        # Test 1: Invalid State
        ("Rio de Janeiro", "XX", InvalidStateError),
        # Test 2: Invalid City
        ("", "SP", InvalidCityError),
        # Test 3: Invalid Length State 
        ("Rio de Janeiro", "RJI", InvalidStateError),
        # Test 4: Non-string City
        ([], "RJ", InvalidCityError),
        # Test 5: Non-string State
        ("Rio de Janeiro", None, InvalidStateError),
        # Test 6: Both City and State Invalid
        ("", "", InvalidCityError)
    ]
)
def test_create_invalid_address_object(city: str, state: str, expected_exception: Exception):
    """
    Test that an invalid Address object cannot be created.
    """
    # Arrange: Create an invalid address dictionary
    invalid_address = {
        "city": city,
        "state": state
    }
    # Act & Assert: Check that creating an Address object raises the expected exception
    with pytest.raises(expected_exception):
        Address(**invalid_address)