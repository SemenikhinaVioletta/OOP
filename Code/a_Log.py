import logging
from tkinter import messagebox


class Logger:
    """
    A flexible logging utility for managing and recording application messages and errors.

    The Logger class provides comprehensive logging functionality with support for informational and error messages, including error dialog display.

    Attributes:
        name (str): Identifier for the logger.
        errors (list): Collection of error messages.
        message (str): Primary log message.

    Methods:
        setup_logging: Configures logging format and level.
        log_message: Processes and logs messages based on error status.
        show_error_dialog: Displays error dialog for critical messages.
        log_info: Static method for logging informational messages.
        log_error: Static method for logging error messages.
    """

    def __init__(self, name, errors, message):
        """
        Initialize a Logger object with the given name, errors, and message.

        This method sets up the logging configuration and logs the message based on the presence of errors.

        Parameters:
        - name (str): The name to be included in the log messages.
        - errors (list): A list of error messages. If empty, no error message will be logged.
        - message (str): The detailed message to be logged.

        Returns:
        - None
        """
        self.name = name
        self.errors = errors
        self.message = message
        self.setup_logging()
        self.log_message()


    def setup_logging(self):
        """
        Sets up the logging configuration for the Logger class.

        This method configures the logging module to use a specific format and log level.
        The log format includes the timestamp, log level, filename, and message.
        The log level is set to INFO.

        Parameters:
        - self (Logger): The Logger object instance.

        Returns:
        - None
        """
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
            level=logging.INFO,
        )


    def log_message(self):
        """
        Logs a message based on the presence of errors.

        This method checks if there are any errors in the `errors` attribute.
        If there are no errors, it logs the `message` attribute using the `logging.info` method.
        If there are errors, it logs the `message` attribute along with the `errors` attribute using the `logging.error` method.
        In case of errors, it also displays an error dialog using the `show_error_dialog` method.

        Parameters:
        - self (Logger): The Logger object instance.

        Returns:
        - None
        """
        if len(self.errors) == 0:
            if self.message[0] == "*":
                logging.info(f"\t{self.name} {self.message[1:]}")
            else:
                logging.info(f"{self.name}: {self.message}")
        else:
            logging.error(f"{self.name}: {self.errors}: {self.message}")
            self.show_error_dialog()


    def show_error_dialog(self):
        """
        Displays an error dialog with a title "ERROR IN INPUT" and the message from the Logger instance.

        This method uses the tkinter messagebox module to display an error dialog box.
        The dialog box has a title "ERROR IN INPUT" and displays the message from the Logger instance.
        The parent of the dialog box is set to None, meaning it will be displayed as a top-level window.

        Parameters:
        - self (Logger): The Logger object instance.

        Returns:
        - None
        """
        messagebox.showerror(title="ERROR IN INPUT", message=self.message, parent=None)


    @staticmethod
    def log_info(name: str, message: str) -> None:
        """
        Logs an informational message with the given name and message.

        This function logs an informational message using the Python logging module.
        If the message starts with "*", it is formatted differently to visually distinguish it.

        Parameters:
        - name (str): The name to be included in the log message. This could be the name of the module, class, or function where the message is being logged.
        - message (str): The detailed message to be logged. This could provide additional context or information about the event being logged.

        Returns:
        - None
        """
        if message[0] == "*":
            logging.basicConfig(
                format="\t\t\t\t%(filename)s - %(message)s",
                level=logging.INFO,
            )
            logging.info(f"\t{name} {message[1:]}")
        else:
            logging.info(f"{name}: {message}")


    @staticmethod
    def log_error(name, error, message):
        """
        Logs an error message with the given name, error, and message.

        This function logs an error message using the Python logging module.
        The message is formatted as "{name}: {error}: {message}".

        Parameters:
        - name (str): The name to be included in the log message. This could be the name of the module, class, or function where the error occurred.
        - error (str): The specific error that occurred. This could be a custom error message or an exception message.
        - message (str): The detailed message to be logged. This could provide additional context or information about the error.

        Returns:
        - None
        """
        logging.error(f"{name}: {error}: {message}")
