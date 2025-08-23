# Error: email doesn't match with pattern/regex
class InvalidEmailError(Exception):
    def __init__(self, message: str):
        super().__init__(message)