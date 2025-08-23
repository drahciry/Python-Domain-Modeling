# Import custom classes
from ..exceptions.InvalidEmailError import InvalidEmailError

# Import libs
import re
from typing import List, Optional

# Class implementation
class Email:
    """
    Represents an email address with validation and domain restrictions.
    """
    def __init__(self, email: str, valid_domains: Optional[List[str]] = None):
        """
        Initialize an Email object.

        Args:
            email (str): The email address to validate and store.
            valid_domains (Optional[List[str]]): List of valid domains. Defaults to common providers.

        Raises:
            InvalidEmailError: If the email does not match the required pattern or domain.
        """
        # List of domains valid
        self.__domains = valid_domains if valid_domains is not None else [
            'gmail.com',
            'outlook.com',
            'hotmail.com'
        ]
        # Set email with validate
        self.email = email

    # ----- Properties -----

    @property
    def email(self) -> str:
        """
        Get the email address.

        Returns:
            str: The validated email address.
        """
        return self.__email
    
    @email.setter
    def email(self, email: str):
        """
        Set and validate the email address.

        Args:
            email (str): The email address to set.

        Raises:
            InvalidEmailError: If the email does not match the required pattern or domain.
        """
        # Pattern before '@'
        local_pattern = r'[a-zA-Z0-9._%+-]+'
        # Pattern after '@'. It uses join to merge all domains with '|'Friendly 'email' presentation
        # and uses re.escape to ensure that '.' will interpreted correctly
        domain_pattern = '|'.join(map(re.escape, self.__domains))
        # It merges localPattern with domainPattern before and after '@'.
        # It use anchors '^' and '$' to ensure your positions
        full_pattern = rf'^{local_pattern}@({domain_pattern})$'
        # Verify if email is a non-empty string
        if not isinstance(email, str) or not email.strip():
            # Custom class for error
            raise InvalidEmailError("email must be a non-empty string.")
        # Performs verification to validate email. If doesn't match, it raises error
        if not re.fullmatch(full_pattern, email):
            # Custom class for error
            raise InvalidEmailError("email don't match with pattern.")
        # Save email
        self.__email = email

    @property
    def username(self) -> str:
        """
        Get the username part of the email address.

        Returns:
            str: The part before the '@' symbol.
        """
        # Returns part before '@'
        return self.email.split('@')[0]
    
    @property
    def domain(self) -> str:
        """
        Get the domain part of the email address.

        Returns:
            str: The part after the '@' symbol.
        """
        # Returns part after '@'
        return self.email.split('@')[1]

    # ------ Dunder Methods ----- 

    def __str__(self) -> str:
        """Return a user-friendly string representation of the email."""
        return f'{self.email}'
    
    def __repr__(self) -> str:
        """Return the official string representation of the Email object."""
        return f'Email({self.email})'
    
    def __eq__(self, other) -> bool:
        """Compare this Email object with another Email or string."""
        # If other is an instance of Email
        if isinstance(other, Email):
            return self.email == other.email
        # If other is an instance of str (String)
        if isinstance(other, str):
            return self.email == other
        # If the previous check don't work
        return NotImplemented
    
    def __hash__(self) -> int:
        """Return the hash of the email address. """
        return hash(self.email)