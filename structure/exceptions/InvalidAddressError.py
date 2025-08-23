# Error: address isn't valid
class InvalidAddressError(Exception):
    def __init__(self, message):
        super().__init__(message)