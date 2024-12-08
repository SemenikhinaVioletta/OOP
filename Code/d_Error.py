from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import a_Log
from a_Log import Logger
from a_Global_per import windows

file_name = "File Error of Produkt"


class ErrorProduct(Exception):

    def __init__(self, *args):
        """
        Initializes the ErrorProdukt exception with an optional error message.

        Parameters:
        *args: Variable length argument list. If provided, the first argument is used as the error message.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        Returns a string representation of the ErrorProdukt exception, showing the error message.

        Returns:
        str: A string representation of the exception, including the error message.
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=None
            )  # Показываем сообщение об ошибке
            return "Error Produkt, message: {0}".format(self.message)
        else:
            return "Error Produkt, raised"

