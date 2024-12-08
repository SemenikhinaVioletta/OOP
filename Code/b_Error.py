from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import a_Log
from a_Log import Logger
import b_Class_New_klient as New
from a_Global_per import windows

file_name = "File Error of New Klient"


# Класс для обработки ошибок нового клиента
# The `ErrorNewKlient` class in Python defines a custom exception with an error message attribute that is displayed when the exception is raised.
class ErrorNewKlient(Exception):
    """Custom exception for handling errors related to new clients.

    This class extends the built-in Exception class to provide a specific error type for issues encountered when creating or managing new clients. It allows for the inclusion of a custom error message and provides a string representation of the error.

    Args:
        *args: Variable length argument list that can include a custom error message.

    Returns:
        None
    """

    def __init__(self, *args):
        """
        This Python function initializes an object with a message attribute based on the provided arguments.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        The function returns an error message if one is provided, otherwise it indicates that an error was raised.

        @return The `__str__` method is returning a string based on the condition of whether `self.message` is truthy or falsy. If `self.message` is truthy, it will display an error message using `showerror` and return a formatted string indicating an error with the message. If `self.message` is falsy, it will simply return a string indicating an error was raised
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=None
            )  # Показываем сообщение об ошибке
            return "Error New klient, message: {0}".format(self.message)
        else:
            return "Error New klient, raised"


# Функция для добавления нового клиента в таблицу
def add_new_to_table(name_entry, phone_entry, email_entry, klients):
    """
    This function validates and adds a new client to a table.

    Parameters:
    name_entry (tkinter.Entry): The entry widget for the client's name.
    phone_entry (tkinter.Entry): The entry widget for the client's phone number.
    email_entry (tkinter.Entry): The entry widget for the client's email address.

    Returns:
    bool: True if the validation is successful and the client is added to the table, False otherwise.
    """
    try:
        name = str(name_entry.get())  # Get the name
        phone = str(phone_entry.get())  # Get the phone number
        email = str(email_entry.get())  # Get the email address
        message = "Validation started."  # Message indicating the start of validation
        names = name.split()  # Split the name into individual words

        # Validate the name
        if len(names) < 3:
            message = "Name must contain at least 3 words."
            raise ErrorNewKlient(message)
        else:
            for i in names:
                if i[0].islower():
                    message = (
                        "Each word in the name must start with an uppercase letter."
                    )
                    raise ErrorNewKlient(message)
                else:
                    for j in i:
                        if not j.isalpha():
                            message = "Name must contain only alphabetic characters."
                            raise ErrorNewKlient(message)
        # Validate the phone number
        if len(phone) != 11:
            message = "Phone number must be exactly 11 digits long."
            raise ErrorNewKlient(
                message
            )  # Raise an error if there are issues with the phone number

        elif phone[0] == "0":
            message = "Phone number must not start with zero."
            raise ErrorNewKlient(
                message
            )  # Raise an error if there are issues with the phone number

        else:
            for j in phone:
                if not j.isdigit():
                    message = "Phone number must contain only digits."
                    raise ErrorNewKlient(
                        message
                    )  # Raise an error if there are issues with the phone number
        # Validate the email address
        if len(email) < 5:
            message = (
                'Email must contain at least 5 characters, e.g., "example@domain.com".'
            )
            raise ErrorNewKlient(
                message
            )  # Raise an error if there are issues with the email address

        elif email.count("@") != 1:
            message = "Email must contain exactly one '@' symbol."
            raise ErrorNewKlient(
                message
            )  # Raise an error if there are issues with the email address

        else:
            i = 0
            for i in range(len(email)):
                if email[i] == "@":
                    break
            if (
                email[i:].count(".") != 1
                or email[i + 1] == "."
                or i >= len(email) - 3
                or i == 0
            ):
                raise ErrorNewKlient(
                    message
                )  # Raise an error if there are issues with the email address

        for k in klients:
            if int(phone) == k.get_phone():
                message = "This phone is already in table"
                raise ErrorNewKlient(message)

            if email == k.get_email():
                message = "This email is already in table"
                raise ErrorNewKlient(message)

        Logger.log_info(
            file_name, "No errors found during validation."
        )  # Log successful validation
        return True
    except ErrorNewKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Log the error
        return False


# Функция для удаления клиента из таблицы
def delete_from_table(id):
    """
    This function validates and deletes a client from a table based on the provided ID.

    Parameters:
    id (tkinter.StringVar): The string variable containing the ID of the client to be deleted.

    Returns:
    bool: True if the validation is successful and the client is deleted from the table, False otherwise.
    Raises:
    ErrorNewKlient: If the ID is not valid, an exception is raised with an appropriate error message.
    """
    try:
        id = id.get()  # Получаем ID
        message = "Validation started."  # Сообщение о начале валидации

        # Проверка ID
        if len(id) != 0:
            for j in id:
                if not j.isdigit():
                    message = "ID must contain only digits."  # Исправлено на более информативное сообщение
                    raise ErrorNewKlient(message)
            if int(id) < 0:
                message = "ID must be greater than or equal to 0."  # Исправлено на более информативное сообщение
                raise ErrorNewKlient(message)
        else:
            message = (
                "ID cannot be empty."  # Исправлено на более информативное сообщение
            )
            raise ErrorNewKlient(message)
        Logger.log_info(
            file_name, "No errors found during ID validation."
        )  # Логируем успешную проверку
        return True
    except ErrorNewKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during ID validation."
        )  # Логируем ошибку
        return False
