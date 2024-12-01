import logging


class Logger:
    """
    A class to handle logging messages with different levels.

    Attributes
    ----------
    name : str
        The name of the logger.
    errors : str
        The error message to be logged.
    message : str
        The main message to be logged.

    Methods
    -------
    __init__(self, name, errors, message)
        Initializes the Logger object and logs the messages based on the presence of errors.
    """

    def __init__(self, name, errors, message):
        """
        Initializes the Logger object and logs the messages based on the presence of errors.

        Parameters
        ----------
        name : str
            The name of the logger.
        errors : str
            The error message to be logged.
        message : str
            The main message to be logged.

        Returns
        -------
        None
        """
        file_name = "Logs_data"
        if len(errors) == 0:
            logging.basicConfig(
                format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
                level=logging.INFO,
            )
            logging.info(f"{name}: {message}")

            logging.basicConfig(
                format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
                level=logging.INFO,
            )
        else:
            logging.basicConfig(
                format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
                level=logging.INFO,
            )
            logging.error(f"{name}: {errors}: {message}")
