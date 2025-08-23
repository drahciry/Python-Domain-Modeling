# Error: name isn't valid   
class InvalidNameError(Exception):
    def __init__(self, message: str):
        super().__init__(message)