import a_Log
import datetime as t
from datetime import date, datetime

from a_Log import Logger
from a_Global_Per import windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno


file_name = "File Error of Contract"
Data = date.today()


class ErrorContract(Exception):
    """
    Custom exception class for handling errors related to contract operations.

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
        *args (tuple): Variable length argument list. The first argument is considered as the error message.

        If no arguments are provided, the error message will be set to None.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        Return the string representation of the error message.

        If the error message is not None, display an error message box using tkinter.messagebox.showerror()
        and return a formatted string containing the error message.

        If the error message is None, return a generic error message.

        Returns:
        str: The string representation of the error message.
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[4][-1]
            )
            return "Error Contract, message: {0}".format(self.message)
        else:
            return "Error Contract, raised"


def chek_ID(id, contracts):
    """
    Check if the given ID exists in the list of contracts.

    Parameters:
    id (int or str): The ID to be checked.
    contracts (list): A list of contract objects. Each contract object should have a method get_ID() that returns the contract's ID.

    Returns:
    bool: True if the ID exists in the list of contracts, False otherwise. If an ErrorContract is raised, the function returns False.

    Raises:
    ErrorContract: If the ID is empty, not a number, or does not exist in the list of contracts.
    """
    try:
        id = str(id)
        if len(id) == 0:
            message = "Id cannot be empty."
            raise ErrorContract(message)

        for i in id:
            if not i.isdigit():
                message = "Id must be a number only."
                raise ErrorContract(message)
        id = int(id)

        flag = True
        for contract in contracts:
            if contract.get_ID() == id:
                flag = False
                break
        if flag:
            message = f"Contract with ID {str(id)} not found."
            raise ErrorContract(message)

        message = f"Contract with ID {str(id)} found go to contract..."
        Logger.log_info(file_name, message)
        return True
    except ErrorContract as e:
        Logger.log_error(file_name, "Error in enter Contract ID", str(e))
        return False


def chek_product(product, products):
    """
    Check if the given product exists in the list of products and has a positive quantity.

    Parameters:
    product (int or str): The ID of the product to be checked.
    products (list): A list of product objects. Each product object should have methods get_ID() and get_number() that return the product's ID and quantity, respectively.

    Returns:
    bool: True if the product exists in the list of products with a positive quantity, False otherwise. If an ErrorContract is raised, the function returns False.

    Raises:
    ErrorContract: If the product ID is empty or does not exist in the list of products.
    """
    try:
        product = str(product)
        if len(product) == 0:
            message = "Product cannot be empty."
            raise ErrorContract(message)

        flag = True
        for p in products:
            if p.get_ID() == int(product) and p.get_number() > 0:
                flag = False
                break
        if flag:
            message = f"Product {product} not found."
            raise ErrorContract(message)

        message = f"Product {product} found go to contract..."
        Logger.log_info(file_name, message)
        return True
    except ErrorContract as e:
        Logger.log_error(file_name, "Error in enter product ID", str(e))
        return False


def chek_date(date_start, date_end):
    """
    Validate and check the validity of the start and end dates for a contract.

    Parameters:
    date_start (str): The start date of the contract in the format 'YYYY-MM-DD'.
    date_end (str): The end date of the contract in the format 'YYYY-MM-DD'.

    Returns:
    bool: True if the dates are valid and the end date is after the start date, and the start date is today or later.
          False otherwise.

    Raises:
    ErrorContract: If the dates are not in the correct format, if the end date is not after the start date,
                   or if the start date is not today or later.
    ValueError: If the dates cannot be converted to a valid date.
    """
    try:
        start = str(date_start).split("-")
        end = str(date_end).split("-")
        if len(start) != 3:
            message = "Error in format start date."
            raise ErrorContract(message)
        if len(end) != 3:
            message = "Error in format end date."
            raise ErrorContract(message)
        if len(start[0]) != 4 or len(end[0]) != 4:
            message = "Error in format year."
            raise ErrorContract(message)
        if len(start[1]) != 2 or len(end[1]) != 2:
            message = "Error in format month."
            raise ErrorContract(message)
        if len(start[2]) != 2 or len(end[2]) != 2:
            message = "Error in format day."
            raise ErrorContract(message)
        for i in start:
            for j in i:
                if not j.isdigit():
                    message = "Error in start format (must be only digits)"
                    raise ErrorContract(message)
        for i in end:
            for j in i:
                if not j.isdigit():
                    message = "Error in end format (must be only digits)"
                    raise ErrorContract(message)

        date1 = date(int(start[0]), int(start[1]), int(start[2]))
        date2 = date(int(end[0]), int(end[1]), int(end[2]))
        if date2 <= date1:
            message = "End date must be after start date"
            raise ErrorContract(message)
        if date1 > Data:
            message = "Start date must be today."
            raise ErrorContract(message)
        message = "Not error in date go to contract..."
        Logger.log_info(file_name, message)
        return True
    except ErrorContract as e:
        Logger.log_error(file_name, "Error in enter Data", str(e))
        return False
    except ValueError as e:
        e = ErrorContract(str(e))
        Logger.log_error(file_name, "Error in enter Data", str(e))
        return False


