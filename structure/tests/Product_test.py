# Import custom classes
from ..models.Price import Price
from ..models.Product import Product
from ..exceptions.InvalidIdError import InvalidIdError
from ..exceptions.InvalidNameError import InvalidNameError
from ..exceptions.InvalidPriceError import InvalidPriceError
from ..exceptions.InvalidCategoryError import InvalidCategoryError
from ..exceptions.InvalidQuantityError import InvalidQuantityError

# Import necessary libs
import pytest

# Test function for the "happy path" scenario
@pytest.mark.parametrize(
    "id_product, name, category, price, quantity",
    [
        # Test 1: Valid Product
        (1, "Mouse Gamer Hive P1 Pichau", "Informática", Price("217.90"), 97),
        # Test 2: Valid Product with big ID
        (87643590, "Teclado Mecânico Gamer Mancer Ghoul MK2 Switch Brown", "Informática", Price("154.90"), 223),
        # Test 3: Valid Product with much quantity
        (7, "Mousepad Pichau Stellar Ultra Speed 500x400x3mm", "Informática", Price("209.68"), 12438)
    ]
)
def test_create_valid_product_object(id_product: int, name: str, category: str, price: Price, quantity: int):
    """
    Test that a valid Product object can be created successfully.
    """
    # Arrange: Create a valid product dictionary
    valid_product = {
        "id_product": id_product,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    # Act: Create a Product object using the valid product dictionary
    product_obj = Product(**valid_product)
    # Assert: Check that the Product object is created sucessfully
    assert product_obj.id_product[1:] == str(id_product)
    assert product_obj.id_product_int == id_product
    assert product_obj.name == name
    assert product_obj.category == category
    assert product_obj.price == price
    assert product_obj.quantity == quantity
    
# Test fuction for the "unhappy path" scenario
@pytest.mark.parametrize(
    "id_product, name, category, price, quantity, expected_exception",
    [
        # Test 1: Invalid ID (Negative Number)
        (-1, "Mouse Gamer Hive P1 Pichau", "Informática", Price("217.90"), 97, InvalidIdError),
        # Test 2: Invalid Name (Empty String)
        (1, "", "Informática", Price("217.90"), 97, InvalidNameError),
        # Test 3: Invalid Category (Empty String)
        (1, "Mouse Gamer Hive P1 Pichau", "", Price("217.90"), 97, InvalidCategoryError),
        # Test 4: Invalid Price (Not a Price Object)
        (1, "Mouse Gamer Hive P1 Pichau", "Informática", "217.90", 97, InvalidPriceError),
        # Test 5: Invalid Quantity (Negative Number)
        (1, "Mouse Gamer Hive P1 Pichau", "Informática", Price("217.90"), -97, InvalidQuantityError),
        # Test 6: Invalid ID (Zero)
        (0, "Mouse Gamer Hive P1 Pichau", "Informática", Price("217.90"), 97, InvalidIdError),
        # Test 7: Invalid Name (Non-string)
        (1, 12345, "Informática", Price("217.90"), 97, InvalidNameError),
        # Test 8: Invalid Category (Non-string)
        (1, "Mouse Gamer Hive P1 Pichau", 12345, Price("217.90"), 97, InvalidCategoryError),
        # Test 9: Invalid Quantity (Non-integer)
        (1, "Mouse Gamer Hive P1 Pichau", "Informática", Price("217.90"), "97", InvalidQuantityError)
    ]
)
def test_create_invalid_product_object(id_product: int, name: str, category: str, price: Price, quantity: int, expected_exception: Exception):
    """
    Test that an invalid Product object cannot be created.
    """
    # Arrange: Create an invalid product dictionary
    invalid_product = {
        "id_product": id_product,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    # Act & Assert: Attempt to create a Product object and expect an exception
    with pytest.raises(expected_exception):
        Product(**invalid_product)