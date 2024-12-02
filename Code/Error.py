from tkinter.messagebox import showerror, showwarning, showinfo
import Log
from Log import Logger
import Class_New_klient as New

file_name = "File Error of New Klient"


class ErrorNewKlient(Exception):
    """
    Custom exception class for handling errors related to new client input.

    Attributes:
    message (str): The error message to be displayed.

    Methods:
    __init__(self, *args): Constructor to initialize the error message.
    __str__(self) -> str: String representation of the error message.
    """

    def __init__(self, *args):
        """
        Initialize the error message.

        Parameters:
        *args (tuple): Variable length argument list. If provided, the first argument is used as the error message.

        Returns:
        None
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        Return the string representation of the error message.

        Parameters:
        None

        Returns:
        str: The error message with a prefix indicating the error type.
        """
        if self.message:
            showerror(title="ERROR IN INPUT", message=self.message)
            return "Error New klient, message: {0}".format(self.message)
        else:
            return "Error New klient, raised"


# --------------------------------------------------------------------------------------------------------------------------------
# Метод для проверки вводимых значений


def add_new_to_table(name_entry, phone_entry, email_entry, klients):
    """
    This function validates and adds new client information to the 'klients' list.

    Parameters:
    name_entry (tkinter.Entry): The entry widget for the client's name.
    phone_entry (tkinter.Entry): The entry widget for the client's phone number.
    email_entry (tkinter.Entry): The entry widget for the client's email address.
    klients (list): The list of existing client objects.

    Returns:
    None

    Raises:
    ErrorNewKlient: If any of the input values fail validation, an ErrorNewKlient exception is raised.
    """
    Logger(
        file_name, "", "Method add_new_to_table - cheking information for new klient..."
    )
    try:
        name = str(name_entry.get())
        phone = str(phone_entry.get())
        email = str(email_entry.get())
        flag = 0
        message = "In this all god."

        names = name.split()
        if len(names) < 3:
            message = "Name must contain at least 3 characters."
            flag = 1
        else:
            for i in names:
                if i[0].islower():
                    message = "Name must be in title case."
                    flag = 1
                else:
                    for j in i:
                        if not j.isalpha():
                            message = "Name must contain only letters."
                            flag = 1
                            break
                if flag == 1:
                    break
        if flag == 1:
            raise ErrorNewKlient(message)
        else:
            Logger("\t", "", "Goos name: " + name)

        if len(phone) != 11:
            message = "Phone must be 11 digits length."
            flag = 1
        elif phone[0] == "0":
            message = "Phone mast be start about not null"
            flag = 1
        else:
            for j in phone:
                if not j.isdigit():
                    message = "Phone must contain only digits."
                    flag = 1
                    break
        if flag == 1:
            raise ErrorNewKlient(message)
        else:
            Logger("\t", "", "Goos phone: " + phone)

        if len(email) < 5:
            message = (
                'Email must contain at least 5 characters or more, example: "a@a.a."'
            )
            flag = 1
        elif email.count("@") != 1:
            message = "Email must contain exactly one '@' symbol."
            flag = 1
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
                message = "Email must contain exactly one '.' symbol."
                flag = 1
        if flag == 1:
            raise ErrorNewKlient(message)
        else:
            Logger("\t", "", "Goos email: " + email)
        if flag == 0:
            klient = New.New_Klient(len(klients) + 1, str(name), int(phone), str(email))
            klients.append(klient)
            klient.enter_klient_to_bd()
    except ErrorNewKlient:
        Logger(file_name, "Error enter", str(ErrorNewKlient(message)))


# --------------------------------------------------------------------------------------------------------------------------------
