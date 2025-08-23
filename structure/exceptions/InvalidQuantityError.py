# Error: quantity isn't valid   
class InvalidQuantityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)