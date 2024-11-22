class ErrorStatus:
    """
    A class to represent an error status with a custom message.

    Attributes
    ----------
    message : str
        The error message.

    Methods
    -------
    __init__(self, message)
        Initializes the ErrorStatus object with the given message.

    """
    def __init__(self, message):
        self.message = message
