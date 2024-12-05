import logging
from tkinter import messagebox  # Importing messagebox for error dialogs

# The `Logger` class in Python provides logging functionality with methods to log messages and errors, as well as display error dialogs.
class Logger:
    def __init__(self, name, errors, message):
        """
        This function initializes an object with a name, errors, and message attributes, sets up logging, and logs a message.
        
        @param name The `name` parameter in the `__init__` method is used to store the name of the object being initialized. It is a common practice to provide a name or identifier for objects to distinguish them from each other.
        @param errors The `errors` parameter in the `__init__` method seems to be used to store error information related to the object being initialized. It is likely intended to hold a collection of error messages or codes that can be used for error handling or logging purposes within the class instance.
        @param message The `message` parameter in the `__init__` method of the class is used to store a message associated with the instance of the class. This message could be any information or content that you want to associate with the object being created. It seems like the `message` parameter is being used
        """
        self.name = name
        self.errors = errors
        self.message = message
        self.setup_logging()
        self.log_message()

    def setup_logging(self):
        """
        The function `setup_logging` configures the logging module in Python with a specific format and log level.
        """
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
            level=logging.INFO,
        )

    def log_message(self):
        """
        The `log_message` function logs a message with the name and errors if present, and shows an error dialog if there are errors.
        """
        if len(self.errors) == 0:
            logging.info(f"{self.name}: {self.message}")
        else:
            logging.error(f"{self.name}: {self.errors}: {self.message}")
            self.show_error_dialog()

    def show_error_dialog(self):
        """
        The function `show_error_dialog` displays an error message dialog with a specified title and message.
        """
        messagebox.showerror(title="ERROR IN INPUT", message=self.message)

    @staticmethod
    def log_info(name, message):
        """
        The `log_info` function is a static method in Python that logs an informational message with the provided name and message.
            
        @param name The `name` parameter is a string representing the name of the entity or component for which you want to log information.
        @param message The `message` parameter in the `log_info` method is a string that represents the information or message that you want to log. It could be any relevant information that you want to record in the log, such as status updates, error messages, or any other details related to the operation of your
        """
        logging.info(f"{name}: {message}")

    @staticmethod
    def log_error(name, errors, message):
        """
        The function `log_error` logs an error message with the specified name, errors, and message using the logging module in Python.
        
        @param name The `name` parameter is a string that represents the name or identifier of the error or the component where the error occurred.
        @param errors The `errors` parameter in the `log_error` function is used to specify the type or details of the error that occurred. It could be an error code, description, or any relevant information about the error that is being logged.
        @param message The `message` parameter in the `log_error` function is a string that represents the error message or description that you want to log when an error occurs. It provides additional context or information about the error that occurred.
        """
        logging.error(f"{name}: {errors}: {message}")
