# Import all model classes
from .Address import Address
from .Product import Product
from .Client import Client
from .Email import Email
from .Price import Price

# Define the __all__ variable to control what gets imported with 'from models import *'
__all__ = [
    'Address',
    'Client',
    'Email',
    'Price',
    'Product'
]