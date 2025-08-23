# Error: category isn't valid   
class InvalidCategoryError(Exception):
    def __init__(self, message: str):
        super().__init__(message)