# Import all custom loaders classes
from .ExcelDataFrameLoader import ExcelDataFrameLoader, pd

# Define the __all__ variable to control what is imported when using 'from loaders import *'
__all__ = ['ExcelDataFrameLoader', 'pd']