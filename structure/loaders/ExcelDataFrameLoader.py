# Import custom classes
from ..exceptions.InvalidPathError import InvalidPathError

# Import necessary libraries
from typing import List
import pandas as pd
import os

# Define the ExcelDataFrameLoader class
class ExcelDataFrameLoader:
    """
    Utility class for loading Excel files into pandas DataFrames using static methods.
    """

    @staticmethod
    def __validate_file_path(file_path):
        """
        Validates the Excel file path.
        
        Args:
            file_path (str): Path to the Excel file.
        
        Raises:
            InvalidPathError: If the file path is not a string or does not end with '.xlsx'.
            FileNotFoundError: If the file does not exist at the specified path.
        """
        if not isinstance(file_path, str) or not file_path.endswith('.xlsx'):
            raise InvalidPathError("File path must be a string ending with '.xlsx'")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

    @staticmethod
    def load_data(file_path, sheet_name=0) -> pd.DataFrame:
        """
        Loads data from the specified sheet of the Excel file into a pandas DataFrame.
        
        Args:
            file_path (str): Path to the Excel file.
            sheet_name (str|int): Name or index of the sheet to load (default is the first sheet).
        
        Returns:
            DataFrame: DataFrame containing the data from the specified sheet.

        Raises:
            InvalidPathError: If occur any error, a new error will be triggered informing wich error occurs.
        """
        try:
            ExcelDataFrameLoader.__validate_file_path(file_path)
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            return df
        except Exception as e:
            raise InvalidPathError(f"An error occurred while loading the data: {e}")

    @staticmethod
    def get_sheet_names(file_path) -> List[int | str]:
        """
        Retrieves the names of all sheets in the Excel file.
        
        Args:
            file_path (str): Path to the Excel file.
        
        Returns:
            list: List of sheet names.
        
        Raises:
            InvalidPathError: If occur any error, a new error will be triggered informing wich error occurs.
        """
        try:
            ExcelDataFrameLoader.__validate_file_path(file_path)
            excel = pd.ExcelFile(file_path)
            return excel.sheet_names
        except Exception as e:
            raise InvalidPathError(f"An error occurred while retrieving sheet names: {e}")