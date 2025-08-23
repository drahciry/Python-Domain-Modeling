# Error: city isn't valid
class InvalidCityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)