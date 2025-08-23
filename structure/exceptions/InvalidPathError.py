# Error: path isn't valid
class InvalidPathError(Exception):
    def __init__(self, message: str):
        super().__init__(message)