# Import all custom exception classes
from exceptions import *

# Import all custom models classes
from models import *

# Import all custom loaders classes
from loaders import *

# Import all necessary libraries
import os

# ----- Starts logical -----

# Get the absolute path of the current file
script_dir = os.path.dirname(__file__)

# File path where worksheet are
file_path = os.path.join(script_dir, 'spreadsheets', 'sales_relatory.xlsx')

# Main function
def main():
    # Loader all sheets
    try:
        df_clients = ExcelDataFrameLoader().load_data(file_path, 'Clients')
        df_products = ExcelDataFrameLoader().load_data(file_path, 'Products')
        df_sales = ExcelDataFrameLoader().load_data(file_path, 'Sales')
    except Exception as e:
        print(f'There was an error for open the worksheet: {e}')

# Execute main function
if __name__ == '__main__':
    # Call the main function
    main()