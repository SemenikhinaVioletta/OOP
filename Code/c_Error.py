from a_Log import Logger
from a_Global_Per import client_statuses, windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno

file_name = "File Error of Pro Client"


class ErrorProClient(Exception):
    """
    Exception raised for errors related to professional clients.

    This exception can be initialized with an optional error message, which can be displayed
    in an error dialog. It provides a string representation that includes the error message
    if available, or indicates that the exception was raised without a specific message.

    Args:
        *args: Variable length argument list. If provided, the first argument is used as the error message.

    Returns:
        None
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
        Returns a string representation of the ErrorProClient exception.

        If the exception has a message, it displays an error message box with the title "ERROR IN INPUT" and the provided message.
        The error message box is parented to the last window in the 'windows' list.

        Returns:
        str: A string representation of the exception, showing the error message if available, otherwise indicating that the exception was raised.
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[1][-1]
            )
            return "Error Pro Client, message: {0}".format(self.message)
        else:
            return "Error Pro Client, raised"


def chek_name(name_entry):
    """
    Validates the name of a client.

    This function checks if the provided name is valid according to the following criteria:
    - The name must contain at least 3 words.
    - Each word in the name must start with an uppercase letter.
    - The name must contain only alphabetic characters.

    Parameters:
    name_entry (tkinter.Entry): The entry widget for the client's name. The name is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the name is valid, False otherwise. Raises an ErrorProClient exception if the name is not valid.
    """
    name = str(name_entry.get())
    message = "Validation started."
    names = name.split()
    try:
        if len(names) < 3:
            message = "Name must contain at least 3 words."
            raise ErrorProClient(message)
        else:
            for i in names:
                if i[0].islower():
                    message = (
                        "Each word in the name must start with an uppercase letter."
                    )
                    raise ErrorProClient(message)
                else:
                    for j in i:
                        if not j.isalpha():
                            message = "Name must contain only alphabetic characters."
                            raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(file_name, "An error occurred during validation.", str(e))
        return False


def chek_phone(phone_entry):
    """
    Validates the phone number of a client.

    This function checks if the provided phone number is valid according to the following criteria:
    - The phone number must be exactly 11 digits long.
    - The phone number must not start with zero.
    - The phone number must contain only digits.

    Parameters:
    phone_entry (tkinter.Entry): The entry widget for the client's phone number. The phone number is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the phone number is valid, False otherwise. Raises an ErrorProClient exception if the phone number is not valid.
    """
    phone = str(phone_entry.get())
    message = "Validation started."
    try:
        if len(phone) != 11:
            message = "Phone number must be exactly 11 digits long."
            raise ErrorProClient(message)
        elif phone[0] == "0":
            message = "Phone number must not start with zero."
            raise ErrorProClient(message)
        else:
            for j in phone:
                if not j.isdigit():
                    message = "Phone number must contain only digits."
                    raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(file_name, "An error occurred during validation.", str(e))
        return False


def chek_email(email_entry):
    """
    Validates the email of a client.

    This function checks if the provided email is valid according to the following criteria:
    - The email must contain at least 5 characters.
    - The email must contain exactly one '@' symbol.
    - The email must contain exactly one '.' symbol after the '@' symbol.
    - The '.' symbol cannot be the first or last character in the email.
    - The email must not have consecutive '.' symbols or '@' symbols.

    Parameters:
    email_entry (tkinter.Entry): The entry widget for the client's email. The email is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the email is valid, False otherwise. Raises an ErrorProClient exception if the email is not valid.
    """
    email = str(email_entry.get())
    message = "Validation started."
    try:
        if len(email) < 5:
            message = (
                'Email must contain at least 5 characters, e.g., "example@domain.com".'
            )
            raise ErrorProClient(message)
        elif email.count("@") != 1:
            message = "Email must contain exactly one '@' symbol."
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
                message = (
                    "Email must contain exactly one '.' symbol after the '@' symbol."
                )
                raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(file_name, "An error occurred during validation.", str(e))
        return False


def chek_Contract(Contract_entry):
    """
    Validates the contract number of a client.

    This function checks if the provided contract number is not empty, contains only digits, and is valid.
    If the contract number is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the contract number is valid, it logs a success message and returns True.

    Parameters:
    Contract_entry (tkinter.Entry): The entry widget for the client's contract number. The contract number is obtained from the 'get' method of the tkinter.Entry object.

    Returns:
    bool: True if the contract number is valid, False otherwise. Raises an ErrorProClient exception if the contract number is not valid.
    """
    Contract = str(Contract_entry.get())
    message = "Validation started."
    Contract = Contract.split()
    try:
        if len(Contract) == 1:
            Contract = Contract[0]
            for i in Contract:
                if not i.isdigit():
                    message = "Contract must contain only digits and > 0"
                    raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(file_name, "An error occurred during validation.", str(e))
        return False


def chek_id(id, Clients):
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
        message = "No errors found during ID validation."

        if len(id) != 0:
            for j in id:
                if not j.isdigit():
                    message = "ID must contain only digits."
                    raise ErrorProClient(message)
        else:
            message = "ID cannot be empty."
            raise ErrorProClient(message)

        flag = False
        for i in Clients:
            if int(id) == i.get_ID():
                flag = True
                break
        if not flag:
            message = "Client with this ID does not exist."
            raise ErrorProClient(message)

        Logger.log_info(file_name, "No errors found during ID validation.")
        return True
    except ErrorProClient as e:
        Logger.log_error(file_name, "An error occurred during ID validation.", str(e))
        return False


def chek_status(status):
    """
    Validates the status of a client.

    This function checks if the provided status is a single digit, and if it is one of the valid status codes (1, 2, or 3).
    If the status is not valid, it raises an ErrorProClient exception with an appropriate error message.
    If the status is valid, it logs a success message and returns True.

    Parameters:
    status (int or str): The status to be validated. If it is a string, it will be converted to an integer.

    Returns:
    bool: True if the status is valid, False otherwise. Raises an ErrorProClient exception if the status is not valid.
    """
    try:
        message = "Validation started."
        status = str(status)
        if not status[0].isdigit():
            message = "Status must be a digit."
            raise ErrorProClient(message)
        status = int(status)
        if status not in [1, 2, 3]:
            message = "Unknown this status"
            raise ErrorProClient(message)
        Logger.log_info(file_name, "NO errors found during status validation.")
        return True

    except ErrorProClient as e:
        Logger.log_error(
            file_name, "An error occurred during status validation.", str(e)
        )
        return False


def add_pro_to_table(name_entry, phone_entry, email_entry, Clients, status, flag):
    """
    This function validates and checks if a new client's data is unique in the table.

    Parameters:
    name_entry (tkinter.Entry): The entry widget for the client's name.
    phone_entry (tkinter.Entry): The entry widget for the client's phone number.
    email_entry (tkinter.Entry): The entry widget for the client's email.
    mora_entry (tkinter.Entry): The entry widget for the client's mora.
    Clients (list): A list of existing client objects.
    flag (int): A flag indicating whether the client is being added (0) or updated (1).

    Returns:
    bool: True if the data is valid and unique, False otherwise.
    """
    try:
        if (
            chek_name(name_entry)
            and chek_phone(phone_entry)
            and chek_email(email_entry)
            and chek_status(status)
        ):
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            if flag == 0:
                for k in Clients:
                    if int(phone) == k.get_phone():
                        message = "This phone is already in table"
                        raise ErrorProClient(message)

                    if email == k.get_email():
                        message = "This email is already in table"
                        raise ErrorProClient(message)

            Logger.log_info(file_name, "NO errors found during status validation.")
            return True
    except ErrorProClient as e:
        Logger.log_error(file_name, "An error occurred during ID validation.", str(e))
        return False
