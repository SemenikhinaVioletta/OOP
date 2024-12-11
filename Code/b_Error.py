import b_Class_New_Client as New
from a_Global_Per import windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
from a_Log import Logger

file_name = "File Error of New Client"


class ErrorNewClient(Exception):
    """
    Custom exception class for handling errors related to the New Client module.

    Attributes:
    message (str): The error message associated with the exception.

    Methods:
    __init__(self, *args): Constructor to initialize the error message.
    __str__(self) -> str: Returns a string representation of the ErrorNewClient object.
    """

    def __init__(self, *args):
        """
        Constructor to initialize the error message.

        Parameters:
        *args: Variable length argument list. If provided, the first argument will be used as the error message.
               If no arguments are provided, the error message will be set to None.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        Returns a string representation of the ErrorNewClient object.

        If the error message is provided, it displays an error message box using tkinter.messagebox.showerror()
        with the title "ERROR IN INPUT" and the provided message. The function then returns a string in the format
        "Error New Client, message: {0}".format(self.message).

        If no error message is provided, the function simply returns the string "Error New Client, raised".

        Returns:
        str: A string representation of the ErrorNewClient object.
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[2][-1]
            )
            return "Error New Client, message: {0}".format(self.message)
        else:
            return "Error New Client, raised"


def chek_name(name):
    """
    Validates the given name according to specific rules.

    Parameters:
    name (str): The name to be validated. It should contain at least 3 words, each starting with an uppercase letter,
                and should contain only alphabetic characters.

    Returns:
    bool: True if the name is valid and no errors occur during validation.
          False if an error occurs during validation.

    Raises:
    ErrorNewClient: If the name is not valid. The error message will provide specific details about the validation failure.
    """
    try:
        names = name.split()
        if len(names) < 3:
            message = "Name must contain at least 3 words"
            raise ErrorNewClient(message)
        else:
            for i in names:
                if i[0].islower():
                    message = (
                        "Each word in the name must start with an uppercase letter"
                    )
                    raise ErrorNewClient(message)
                else:
                    for j in i:
                        if not j.isalpha():
                            message = "Name must contain only alphabetic characters"
                            raise ErrorNewClient(message)
        Logger.log_info(file_name, "No errors found during validation")
        return True
    except ErrorNewClient as e:
        Logger.log_error(file_name, "An error occurred during validation", str(e))
        return False


def chek_phone(phone):
    """
    Validates the given phone number according to specific rules.

    Parameters:
    phone (str): The phone number to be validated. It should not contain any spaces at the beginning or end,
                 and should only contain digits.

    Returns:
    bool: True if the phone number is valid and no errors occur during validation.
          False if an error occurs during validation.

    Raises:
    ErrorNewClient: If the phone number is not valid. The error message will provide specific details about the validation failure.
    """
    try:
        if len(phone) > 0:
            while phone[0] == " ":
                phone = phone[1:]
            while phone[-1] == " ":
                phone = phone[:-1]
            while " " in phone:
                phone = phone.replace(" ", "")

        if len(phone) != 11:
            message = "Phone number must be exactly 11 digits long"
            raise ErrorNewClient(message)
        elif phone[0] == "0":
            message = "Phone number must not start with zero"
            raise ErrorNewClient(message)
        else:
            for j in phone:
                if not j.isdigit():
                    message = "Phone number must contain only digits"
                    raise ErrorNewClient(message)

        Logger.log_info(file_name, "No errors found during validation")
        return True
    except ErrorNewClient as e:
        Logger.log_error(file_name, "An error occurred during validation", str(e))
        return False


def chek_mail(email):
    """
    Validates the given email address according to specific rules.

    Parameters:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email address is valid and no errors occur during validation.
          False if an error occurs during validation.

    Raises:
    ErrorNewClient: If the email address is not valid.
    """
    try:
        if len(email) > 0:
            while " " in email:
                email = email.replace(" ", "")

        if len(email) < 5:
            message = (
                'Email must contain at least 5 characters, e.g., "example@domain.com".'
            )
            raise ErrorNewClient(message)

        elif email.count("@") != 1:
            message = "Email must contain exactly one '@' symbol"
            raise ErrorNewClient(message)

        else:
            i = 0
            for i in range(len(email)):
                if email[i] == "@":
                    break
            if (
                email[i:].count(".") != 1
                or email[i + 1] == ""
                or i >= len(email) - 3
                or i == 0
            ):
                message = 'Email must contain at least one character after "@", e.g., "example@domain.com".'
                raise ErrorNewClient(message)
        Logger.log_info(file_name, "No errors found during validation")
        return True
    except ErrorNewClient as e:
        Logger.log_error(file_name, "An error occurred during validation", str(e))
        return False


def add_new_to_table(name_entry, phone_entry, email_entry, Clients):
    """
    This function validates and adds a new client to the Clients list based on the given name, phone, and email.

    Parameters:
    name_entry (tkinter.Entry): The entry widget containing the client's name.
    phone_entry (tkinter.Entry): The entry widget containing the client's phone number.
    email_entry (tkinter.Entry): The entry widget containing the client's email.
    Clients (list): A list of client objects.

    Returns:
    bool: True if the addition is successful and no errors occur during validation.
          False if an error occurs during validation.

    Raises:
    ErrorNewClient: If the name, phone, or email is not valid or if the phone or email is already in the Clients list.
    """
    try:
        name = str(name_entry.get())
        phone = str(phone_entry.get())
        email = str(email_entry.get())
        message = "Validation started"
        if chek_name(name) and chek_phone(phone) and chek_mail(email):
            for k in Clients:
                if int(phone) == k.get_phone():
                    message = "This phone is already in table"
                    raise ErrorNewClient(message)

                if email == k.get_email():
                    message = "This email is already in table"
                    raise ErrorNewClient(message)

            Logger.log_info(file_name, "No errors found during validation")
            return True
    except ErrorNewClient as e:
        Logger.log_error(file_name, "An error occurred during validation", str(e))
        return False


def delete_from_table(id, Clients):
    """
    This function validates and deletes a client from the Clients list based on the given ID.

    Parameters:
    id (tkinter.StringVar): The ID of the client to be deleted.
    Clients (list): A list of client objects.

    Returns:
    bool: True if the deletion is successful and no errors occur during validation.
          False if an error occurs during validation.

    Raises:
    ErrorNewClient: If the ID is not valid or if no client with the given ID is found in the Clients list.
    """
    try:
        id = id.get()
        message = "Validation started"
        if len(id) != 0:
            for j in id:
                if not j.isdigit():
                    message = "ID must contain only digits"
                    raise ErrorNewClient(message)
            if int(id) < 0:
                message = "ID must be greater than or equal to 0"
                raise ErrorNewClient(message)
        else:
            message = "ID cannot be empty"
            raise ErrorNewClient(message)

        flag = False
        for i in Clients:
            if int(id) == i.get_ID():
                flag = True
                break
        if not flag:
            message = "No client with this ID found in table"
            raise ErrorNewClient(message)

        Logger.log_info(file_name, "No errors found during ID validation")
        return True
    except ErrorNewClient as e:
        Logger.log_error(file_name, "An error occurred during ID validation", str(e))
        return False
