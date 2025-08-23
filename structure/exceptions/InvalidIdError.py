# Error: ID isn't valid
class InvalidIdError(Exception):
    def __init__(self, message: str):
        super().__init__(message)