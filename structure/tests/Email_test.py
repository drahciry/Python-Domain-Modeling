# Import custom classes
from ..models.Email import Email
from ..exceptions.InvalidEmailError import InvalidEmailError

# Import necessary libraries
import pytest
from typing import List, Optional

# Test function for the "happy path" scenario
@pytest.mark.parametrize(
    "email, valid_domains",
    [
        # Test 1: Valid email with default domains
        ("email.test@gmail.com", None),
        # Test 2: Valid email with custom domains
        ("email.test@customdomain.com", ["customdomain.com"]),
        # Test 3: Valid email with multiple custom domains
        ("email.test@customdomain1.com", ["customdomain1.com", "customdomain2.com"]),
    ],
)
def test_create_invalid_email_object(email: str, valid_domains: Optional[List[str]]):
    """
    Test that a valid Email object can be created successfully.
    """
    # Arrange: Create a valid email dictionary
    valid_email = {
        "email": email,
        "valid_domains": valid_domains
    }
    # Act: Create an Email object using the valid email dictionary
    email_obj = Email(**valid_email)
    # Assert: Check that the Email object is created successfully
    assert email_obj.email == email
    
# Test function for the "unhappy path" scenario
@pytest.mark.parametrize(
    "email, valid_domains, expected_exception",
    [
        # Test 1: Invalid email format
        ("invalid-email", None, InvalidEmailError),
        # Test 2: Email with domain not in default list
        ("email.test@invaliddomain.com", None, InvalidEmailError),
        # Test 3: Email with domain not in custom list
        ("email.test@customdomain3.com", ["customdomain1.com", "customdomain2.com"], InvalidEmailError),
        # Test 4: Invalid email format with custom domains
        ("invalid-email@", ["customdomain1.com"], InvalidEmailError),
        # Test 5: Empty email string
        ("", None, InvalidEmailError),
        # Test 6: None as email
        (None, None, InvalidEmailError)
    ],
)
def test_create_invalid_email_object(email: str, valid_domains: Optional[List[str]], expected_exception: Exception):
    """
    Test that an invalid Email object cannot be created.
    """
    # Arrange: Create an invalid email dictionary
    invalid_email = {
        "email": email,
        "valid_domains": valid_domains
    }
    # Act & Assert: Attempt to create an Email object and expect an exception
    with pytest.raises(expected_exception):
        Email(**invalid_email)