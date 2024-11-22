from tkinter.messagebox import showerror, showwarning, showinfo

class ErrorNewKlient(Exception):
    """
    Custom exception class to represent error statuses.

    Attributes:
    message (str): The error message associated with the error status.

    Methods:
    __init__(self, *args): Constructor to initialize the error status with an optional message.
    __str__(self) -> str: String representation of the error status.
    """

    def __init__(self, *args):
        """
        Initialize the error status with an optional message.
    
        Parameters:
        *args (tuple): Variable length argument list. The first argument is expected to be a string representing the error message.
    
        Attributes:
        message (str): The error message associated with the error status. If no message is provided, it will be set to None.
    
        Raises:
        TypeError: If the first argument is not a string.
    
        Examples:
        >>> error = ErrorNewKlient("Invalid input")
        >>> print(error.message)
        Invalid input
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        String representation of the ErrorNewKlient instance.

        If the error message is provided, it will display an error message box using tkinter's showerror function.
        The error message will be formatted as "Error New klient, message: {0}".

        If no error message is provided, it will simply return "Error New klient, raised".

        Returns:
        str: The formatted error message or a default message indicating that the error was raised.
        """
        print("calling str")
        if self.message:
            showerror(title="ERROR IN INPUT", message=self.message)
            return "Error New klient, message: {0}".format(self.message)
        else:
            return "Error New klient, raised"


def add_new_to_table(name_entry, phone_entry, email_entry):
    """
    This function validates and adds new client data to a table.

    Parameters:
    name_entry (tkinter.Entry): The entry widget for the client's name.
    phone_entry (tkinter.Entry): The entry widget for the client's phone number.
    email_entry (tkinter.Entry): The entry widget for the client's email address.

    Returns:
    None

    Raises:
    ErrorNewKlient: If any of the validation checks fail, an instance of ErrorNewKlient is raised with an appropriate error message.
    """
    print("File Error: method add_new_to_table - start checing...")
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
            flag = 0
        else:
            print("\t Goos name:", name)

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
            flag = 0
        else:
            print("\t Goos phone:", phone)

        if len(email) < 5:
            message ="Email must contain at least 5 characters or more, example: \"a@a.a.\""
            flag = 1
        elif email.count("@") != 1:
            message = "Email must contain exactly one '@' symbol."
            flag = 1
        else:
            i = 0
            for i in range(len(email)):
                if email[i] == "@":
                    break

            if email[i:].count(".") != 1 or email[i + 1] == "." or i >= len(email) - 3  or i == 0:
                message = "Email must contain exactly one '.' symbol."
                flag = 1
        if flag == 1:
            raise ErrorNewKlient(message)
            flag = 0
        else:
            print("\t Goos email:", email)

    except ErrorNewKlient:
        print("\tError:", ErrorNewKlient(message))
