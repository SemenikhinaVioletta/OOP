import logging
from tkinter import messagebox  # Importing messagebox for error dialogs

class Logger:
    def __init__(self, name, errors, message):
        self.name = name
        self.errors = errors
        self.message = message
        self.setup_logging()
        self.log_message()

    def setup_logging(self):
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
            level=logging.INFO,
        )

    def log_message(self):
        if len(self.errors) == 0:
            logging.info(f"{self.name}: {self.message}")
        else:
            logging.error(f"{self.name}: {self.errors}: {self.message}")
            self.show_error_dialog()

    def show_error_dialog(self):
        messagebox.showerror(title="ERROR IN INPUT", message=self.message)

    @staticmethod
    def log_info(name, message):
        logging.info(f"{name}: {message}")

    @staticmethod
    def log_error(name, errors, message):
        logging.error(f"{name}: {errors}: {message}")
