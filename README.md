# Core Models: A Python Domain-Driven Library

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A foundational Python library designed to provide a set of robust, validated, and type-safe domain models for a typical sales or e-commerce system. This project emphasizes clean code, object-oriented principles, and solid software engineering practices.

## Key Features

This library was built with a focus on creating reliable and maintainable code. The key features include:

* **🛡️ Robust Data Validation:** Uses property setters to ensure that objects never enter an invalid state. Business rules (e.g., a `Price` cannot be negative, an `Email` must have a valid format) are enforced at the object's boundary.
* **🚨 Custom Exception Handling:** Provides a hierarchy of specific, custom exceptions (e.g., `InvalidEmailError`, `InvalidPriceError`, `InvalidIdError`) for clear and precise error handling by client code.
* **📦 Object-Oriented Design:** Follows the Single Responsibility Principle by separating concerns into distinct classes (`Client`, `Product`, `Price`, `Address`). It also uses composition to build complex objects from simpler ones (e.g., a `Client` has an `Email` object).
* **✨ Rich Object Model:** Implements essential dunder methods (`__str__`, `__repr__`, `__eq__`, and comparison methods for `Price`) to ensure objects are easy to debug, print, and compare.
* **📑 Data Loading Utility:** Includes a reusable `ExcelDataFrameLoader` class to handle the extraction of data from Excel files into pandas DataFrames, with built-in path validation and error handling.
* **✍️ Type Safety:** Fully type-hinted for improved readability, developer experience with auto-completion, and static analysis.

## Project Structure

The project is organized into a clear package structure to promote separation of concerns and maintainability:

```
Python-Domain-Modeling/
├── .gitignore
├── README.md
├── requirements.txt
└── structure/
    ├── __init__.py
    ├── main.py
    ├── data/
    |   ├── processed/
    |   └── raw/
    |       └── sales_relatory.xlsx
    ├── exceptions/  # Custom exception classes
    |   ├── __init__.py
    |   ├── InvalidAddressError.py
    |   ├── InvalidCategoryError.py
    |   ├── InvalidCityError.py
    |   ├── InvalidEmailError.py
    |   ├── InvalidIdError.py
    |   ├── InvalidNameError.py
    |   ├── InvalidPriceError.py
    |   ├── InvalidQuantityError.py
    |   └── InvalidStateError.py
    ├── loaders/     # Data loading classes
    |   ├── __init__.py
    |   └── ExcelDataFrameLoader.py
    ├── models/      # Core domain model classes
    |   ├── __init__.py
    |   ├── Address.py
    |   ├── Client.py
    |   ├── Email.py
    |   ├── Price.py
    |   └── Product.py
    └── tests/       # Unit tests
        ├── __init__.py
        ├── Client_test.py
        ├── Email_test.py
        ├── Price_test.py
        ├── Product_test.py
        └── Address_test.py
```

## Usage Example

Here is a quick example of how to use the library's components to load data and work with the domain models.

### 1. Loading Data from an Excel File

The `ExcelDataFrameLoader` provides a simple interface to load spreadsheets into a pandas DataFrame.

```python
from structure.loaders.ExcelDataFrameLoader import ExcelDataFrameLoader

# Instantiate the loader
loader = ExcelDataFrameLoader()

# Load the data
try:
    products_df = loader.load_data('path/to/your/spreadsheat.xlsx')
    print("Spreadsheets loaded successfully!")
    print(products_df.head())
except Exception as e:
    print(f"Failed to load data: {e}")
```

### 2. Working with Models and Validation

The model classes ensure that you are always working with valid data.

```python
from structure.models.Price import Price
from structure.models.Product import Product
from structure.exceptions.InvalidPriceError import InvalidPriceError

try:
    # Creating a valid Price object
    product_price = Price("199.90")
    print(f"Valid price created: {product_price}")

    # Creating a valid Product object
    my_product = Product(
        id_product=101,
        name="Wireless Keyboard",
        category="Electronics",
        price=product_price,
        quantity=50
    )
    print(f"Valid product created: {my_product}")

    # Example of invalid data triggering a custom exception
    invalid_price = Price("-10.00")

except InvalidPriceError as e:
    print(f"\nCaught an expected error: {e}")
```

## Testing

This project uses `pytest` for unit testing to ensure all models and validations work as expected. To run the tests, navigate to the root directory (`Python-Domain-Modeling/`) and execute:

```bash
pytest
```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page for this repository.

---
**Richard Gonçalves** - [Linkedin](https://linkedin.com/in/drahciry)  
