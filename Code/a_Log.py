import logging
from tkinter import messagebox


class Logger:
    def __init__(self, name, errors, message):
        """
        Initialize a Logger object.

        Parameters:
        - name (str): The name of the logger.
        - errors (list): A list of errors to be logged.
        - message (str): The message to be logged.

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
        Initialize the logging configuration.

        This method sets up the basic configuration for logging using the logging module.
        It specifies the log format and the log level.

        Parameters:
        - None

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

        If no errors are present, logs an INFO message with the format:
        "{self.name}: {self.message}"

        If errors are present, logs an ERROR message with the format:
        "{self.name}: {self.errors}: {self.message}"
        and shows an error dialog using the show_error_dialog method.

        Parameters:
        - self (Logger): The Logger object instance.

        Returns:
        - None
        """
        if len(self.errors) == 0:
            logging.info(f"{self.name}: {self.message}")
        else:
            logging.error(f"{self.name}: {self.errors}: {self.message}")
            self.show_error_dialog()


    def show_error_dialog(self):
        """
        Displays an error dialog with a specified title, message, and parent window.

        This method uses the tkinter messagebox module to show an error dialog box.
        The dialog box displays the error message and has a title "ERROR IN INPUT".
        The parent window of the dialog box is set to None.

        Parameters:
        - self (Logger): The Logger object instance.

        Returns:
        - None
        """
        messagebox.showerror(title="ERROR IN INPUT", message=self.message, parent=None)


    @staticmethod
    def log_info(name, message):
        """
        Logs an informational message with the given name and message.

        This function logs an informational message using the Python logging module.
        The message is formatted as "{name}: {message}".

        Parameters:
        - name (str): The name to be included in the log message.
        - message (str): The message to be logged.

        Returns:
        - None
        """
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

