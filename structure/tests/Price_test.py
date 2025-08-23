# Import custom classes
from ..models.Price import Price
from ..exceptions.InvalidPriceError import InvalidPriceError

# Import necessary libs
import pytest
from decimal import Decimal

# Test function for the "happy path" scenario
@pytest.mark.parametrize(
    "price",
    [
        # Test 1: Valid Price as a string
        "19.99",
        # Test 2: Valid Price as a string with more decimal places
        "100.12345",
        # Test 3: Valid Price as a string with leading and trailing spaces
        "  250.00  ",
        # Test 4: Valid Price as a string with no decimal places
        "50",
        # Test 5: Valid Price as a string with large value
        "1000000.99",
        # Test 6: Valid Price as a string with small value
        "0.01",
        # Test 7: Valid Price as a string with many decimal places
        "12345.6789012345",
        # Test 8: Valid Price as a string with leading zeros
        "000123.45"
    ]
)
def test_create_valid_price_object(price: str):
    """
    Test that a valid Price object can be created successfully.
    """
    # Arrange: Create a valid price dictionary
    valid_price = {
        "price": price
    }
    # Act: Create a Price object using the valid price dictionary
    price_obj = Price(**valid_price)
    # Assert: Check that the Price object is created successfully
    assert isinstance(price_obj.price, Decimal)
    assert price_obj.price == Decimal(price.strip())
    
# Test function for the "unhappy path" scenario
@pytest.mark.parametrize(
    "price, expected_exception",
    [
        # Test 1: Invalid Price (Negative Number)
        ("-19.99", InvalidPriceError),
        # Test 2: Invalid Price (Zero)
        ("0", InvalidPriceError),
        # Test 3: Invalid Price (Non-numeric String)
        ("abc", InvalidPriceError),
        # Test 4: Invalid Price (Empty String)
        ("", InvalidPriceError),
        # Test 5: Invalid Price (Whitespace String)
        ("   ", InvalidPriceError),
        # Test 6: Invalid Price (None)
        (None, InvalidPriceError),
        # Test 7: Invalid Price (Special Characters)
        ("$100.00", InvalidPriceError),
        # Test 8: Invalid Price (Multiple Decimal Points)
        ("100.00.00", InvalidPriceError),
        # Test 9: Invalid Price (Alphabetic Characters Mixed with Numbers)
        ("123abc", InvalidPriceError),
        # Test 10: Invalid Price (Just a Decimal Point)
        (".", InvalidPriceError),
    ]
)
def test_create_invalid_price_object(price, expected_exception):
    """
    Test that creating a Price object with invalid input raises the expected exception.
    """
    # Arrange: Create an invalid price dictionary
    invalid_price = {
        "price": price
    }
    # Act & Assert: Attempt to create a Price object and check for the expected exception
    with pytest.raises(expected_exception):
        Price(**invalid_price)