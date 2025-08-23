# Error: price isn't valid   
class InvalidPriceError(Exception):
    def __init__(self, message: str):
        super().__init__(message)