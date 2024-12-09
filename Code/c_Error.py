from a_Log import Logger
from a_Global_per import status_klient, windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno

file_name = "File Error of Pro Klient"


class ErrorProClient(Exception):
    """
    Custom exception class for handling errors in the Pro Klient application.

    Attributes:
    message (str): The error message associated with the exception.

    Methods:
    __init__(self, *args): Constructor that initializes the error message.
    __str__(self) -> str: String representation of the exception, showing the error message.
    """

    def __init__(self, *args):
        """
        Initializes the ErrorProClient exception with an optional error message.

        Parameters:
        *args: Variable length argument list. If provided, the first argument is used as the error message.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        Returns a string representation of the ErrorProClient exception, showing the error message.

        Returns:
        str: A string representation of the exception, including the error message.
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[1][-1]
            )  # Показываем сообщение об ошибке
            return "Error Pro klient, message: {0}".format(self.message)
        else:
            return "Error Pro klient, raised"


def chek_name(name_entry):
    """
    Validates the name of a client.

    This function checks if the provided name is at least 3 words long, each word starts with an uppercase letter,
    and contains only alphabetic characters. If the name is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the name is valid, it logs a success message and returns True.

    Parameters:
    name_entry (tkinter.Entry): The entry widget for the client's name. The name is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the name is valid, False otherwise. Raises an ErrorProClient exception if the name is not valid.
    """
    name = str(name_entry.get())  # Получаем имя
    message = "Validation started."  # Сообщение о начал
    names = name.split()  # Разделяем имя на части
    try:
        if len(names) < 3:
            message = "Name must contain at least 3 words."  # Исправлено на более информативное сообщение
            raise ErrorProClient(message)
        else:
            for i in names:
                if i[0].islower():
                    message = "Each word in the name must start with an uppercase letter."  # Исправлено на более информативное сообщение
                    raise ErrorProClient(message)
                else:
                    for j in i:
                        if not j.isalpha():
                            message = "Name must contain only alphabetic characters."  # Исправлено на более информативное сообщение
                            raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
        return False


def chek_phone(phone_entry):
    """
    Validates the phone number of a client.

    This function checks if the provided phone number is exactly 11 digits long, does not start with zero,
    and contains only digits. If the phone number is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the phone number is valid, it logs a success message and returns True.

    Parameters:
    phone_entry (tkinter.Entry): The entry widget for the client's phone number. The phone number is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the phone number is valid, False otherwise. Raises an ErrorProClient exception if the phone number is not valid.
    """
    phone = str(phone_entry.get())
    message = "Validation started."  # Сообщение о начал
    try:
        if len(phone) != 11:
            message = "Phone number must be exactly 11 digits long."  # Исправлено на более информативное сообщение
            raise ErrorProClient(message)
        elif phone[0] == "0":
            message = "Phone number must not start with zero."  # Исправлено на более информативное сообщение
            raise ErrorProClient(message)
        else:
            for j in phone:
                if not j.isdigit():
                    message = "Phone number must contain only digits."  # Исправлено на более информативное сообщение
                    raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
        return False


def chek_email(email_entry):
    """
    Validates the email of a client.

    This function checks if the provided email is not empty, contains at least 5 characters, exactly one '@' symbol,
    exactly one '.' symbol after the '@' symbol, and does not start or end with a '.' or '@' symbol.
    If the email is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the email is valid, it logs a success message and returns True.

    Parameters:
    email_entry (tkinter.Entry): The entry widget for the client's email. The email is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the email is valid, False otherwise. Raises an ErrorProClient exception if the email is not valid.
    """
    email = str(email_entry.get())  # Получаем email
    message = "Validation started."  # Сообщение о начале валидации
    try:
        if len(email) < 5:
            message = 'Email must contain at least 5 characters, e.g., "example@domain.com".'  # Исправлено на более информативное сообщение
            raise ErrorProClient(message)
        elif email.count("@") != 1:
            message = "Email must contain exactly one '@' symbol."  # Исправлено на более информативное сообщение
            raise ErrorProClient(message)
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
                message = "Email must contain exactly one '.' symbol after the '@' symbol."  # Исправлено на более информативное сообщение
                raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
        return False


def chek_mora(mora_entry):
    """
    Validates the mora of a client.

    This function checks if the provided mora is not empty, contains only digits, and is greater than 0.
    If the mora is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the mora is valid, it logs a success message and returns True.

    Parameters:
    mora_entry (tkinter.Entry): The entry widget for the client's mora. The mora is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the mora is valid, False otherwise. Raises an ErrorProClient exception if the mora is not valid.
    """
    mora = str(mora_entry.get())  # Получаем email
    message = "Validation started."  # Сообщение о начале валидации
    try:
        if len(mora) != 0:
            for i in mora:
                if not i.isdigit():
                    message = "Mora must contain only digits and > 0"  # Исправлено на более информативное сообщение
                    raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
        return False


def chek_kontrakt(kontrakt_entry):
    """
    Validates the contract number of a client.

    This function checks if the provided contract number is not empty, contains only digits, and is greater than 0.
    If the contract number is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the contract number is valid, it logs a success message and returns True.

    Parameters:
    kontrakt_entry (tkinter.Entry): The entry widget for the client's contract number. The contract number is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the contract number is valid, False otherwise. Raises an ErrorProClient exception if the contract number is not valid.
    """
    kontrakt = str(kontrakt_entry.get())
    message = "Validation started."  # Сообщение о начале валидации
    kontrakt = kontrakt.split()
    try:
        if len(kontrakt) == 1:
            kontrakt = kontrakt[0]
            for i in kontrakt:
                if not i.isdigit():
                    message = "kontrakt must contain only digits and > 0"  # Исправлено на более информативное сообщение
                    raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation.")
        return False  # Логируем ошибку


def chek_id(id):
    """
    Validates the ID of a client.

    This function checks if the provided ID is not empty and contains only digits.
    If the ID is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the ID is valid, it logs a success message and returns True.

    Parameters:
    id (tkinter.StringVar): The ID to be validated. The ID is obtained from the 'get' method of the tkinter.StringVar object.

    Returns:
    bool: True if the ID is valid, False otherwise. Raises an ErrorProClient exception if the ID is not valid.
    """
    try:
        id = id.get()
        message = (
            "No errors found during ID validation."  # Сообщение о начале валидации
        )

        # Проверка ID
        if len(id) != 0:
            for j in id:
                if not j.isdigit():
                    message = "ID must contain only digits."  # Исправлено на более информативное сообщение
                    raise ErrorProClient(message)
        else:
            message = (
                "ID cannot be empty."  # Исправлено на более информативное сообщение
            )
            raise ErrorProClient(message)

        Logger.log_info(file_name, "No errors found during ID validation.")
        return True
    except ErrorProClient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during ID validation."
        )  # Логируем ошибку
        return False


def chek_status(status):
    """
    Validates the status of a client.

    This function checks if the provided status is one of the valid options (1, 2, or 3).
    If the status is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the status is valid, it logs a success message and returns True.

    Parameters:
    status (int): The status to be validated.

    Returns:
    bool: True if the status is valid, False otherwise. Raises an ErrorProClient exception if the status is not valid.
    """
    try:
        message = "Validation started."  # Сообщение о начале валидации
        if status != 1 or status != 2 or status != 3:
            message = "Unknown this status"
            raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during status validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during status validation."
        )
        return False


# Функция для добавления нового клиента в таблицу
def add_pro_to_table(name_entry, phone_entry, email_entry, mora_entry, klients, flag):
    """
    This function validates and checks if a new client's data is unique in the table.

    Parameters:
    name_entry (tkinter.Entry): The entry widget for the client's name.
    phone_entry (tkinter.Entry): The entry widget for the client's phone number.
    email_entry (tkinter.Entry): The entry widget for the client's email.
    mora_entry (tkinter.Entry): The entry widget for the client's mora.
    klients (list): A list of existing client objects.
    flag (int): A flag indicating whether the client is being added (0) or updated (1).

    Returns:
    bool: True if the data is valid and unique, False otherwise.
    """
    try:
        if (
            chek_name(name_entry)
            or chek_phone(phone_entry)
            or chek_email(email_entry)
            or chek_mora(mora_entry)
        ):
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            if flag == 0:
                for k in klients:
                    if int(phone) == k.get_phone():
                        message = "This phone is already in table"
                        raise ErrorProClient(message)

                    if email == k.get_email():
                        message = "This email is already in table"
                        raise ErrorProClient(message)

            Logger.log_info(file_name, "NO errors found during status validation.")
            return True
    except ErrorProClient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during ID validation."
        )  # Логируем ошибку
        return False
