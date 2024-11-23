class ErrorStatus(Exception):
    """
    Custom exception class to represent error statuses.

    Attributes:
    message (str): The error message associated with the error status.

    Methods:
    __init__(self, *args): Constructor to initialize the error status with an optional message.
    __str__(self) -> str: String representation of the error status.
    """

    def __init__(self, *args):
        """
        Initialize the error status with an optional message.

        Parameters:
        *args (tuple): Variable length argument list. If provided, the first argument is considered as the error message.

        Returns:
        None
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        Return a string representation of the error status.

        Returns:
        str: A string representation of the error status, including the error message if provided.
        """
        print("calling str")
        if self.message:
            return "Error status, message: {0}".format(self.message)
        else:
            return "Error status, raised"
        else:
            return "Error status, raised"
