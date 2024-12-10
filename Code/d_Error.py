import a_Log
from a_Log import Logger
from a_Global_Per import windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno


file_name = "File Error of Produkt"


class ErrorProduct(Exception):
    """
    Exception raised for errors related to product operations.

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
        Initializes the exception with an optional error message.

        This constructor allows for the creation of an exception instance with a custom message.
        If no message is provided, the instance will be initialized without a specific message.

        Args:
            *args: Variable length argument list. If provided, the first argument is used as the error message.

        Returns:
            None
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        Returns a string representation of the ErrorProduct instance.

        If the instance has a message attribute, it displays an error message using the showerror function from the tkinter.messagebox module.
        The error message is formatted as "Error Produkt, message: {0}".

        If the instance does not have a message attribute, it returns the string "Error Produkt, raised".

        Parameters:
        self (ErrorProduct): The instance of the ErrorProduct class.

        Returns:
        str: A string representation of the ErrorProduct instance.
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[3][-1]
            )
            return "Error Produkt, message: {0}".format(self.message)
        else:
            return "Error Produkt, raised"


def chek_mora(mora):
    """
    Validates the mora input for a product.

    Parameters:
    mora (str or int): The mora of the product to be validated. It should be a non-empty string or integer,
                       containing only digits and without leading or trailing spaces.

    Returns:
    bool: True if the mora is valid (non-empty, contains only digits, and positive).
          False otherwise, with appropriate error messages logged.

    Raises:
    ErrorProduct: If the mora is not valid.
    """
    try:
        mora = str(mora)
        if len(mora) > 0:
            while " " in mora:
                mora = mora.replace(" ", "")
        if len(mora) < 1:
            raise ErrorProduct("Morad must be a positive number")
        for i in mora:
            if not i.isdigit():
                print(i)
                raise ErrorProduct(
                    "Mora must contain only digits and mora can`t be < 0"
                )

        Logger.log_info(file_name, "NO errors found during status validation.")
        return True
    except ErrorProduct as e:
        Logger.log_error(file_name, "An error occurred during validation.", str(e))
        return False


def check_price(price):
    """
    Validates the price input for a product.

    Parameters:
    price (str): The price of the product to be validated. It should be a non-empty string,
                 containing only digits and without leading or trailing spaces.

    Returns:
    bool: True if the price is valid (non-empty, contains only digits, and positive).
          False otherwise, with appropriate error messages logged.

    Raises:
    ErrorProduct: If the price is not valid.
    """
    try:
        price = str(price)
        if len(price) > 0:
            while " " in price:
                price = price.replace(" ", "")
        if len(price) < 1:
            raise ErrorProduct("Price must be a positive number")
        for i in price:
            if not i.isdigit():
                raise ErrorProduct(
                    "Price must contain only digits and price can`t be < 0"
                )
        Logger.log_info(file_name, "NO errors found during status validation.")
        return True
    except ErrorProduct as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation.")
        return False


def check_name(name):
    """
    Validates the name input for a product.

    Parameters:
    name (str): The name of the product to be validated.

    Returns:
    bool: True if the name is valid (non-empty).
          False otherwise, with appropriate error messages logged.

    Raises:
    ErrorProduct: If the name is not valid.
    """
    try:
        name = str(name)
        if len(name) < 1:
            raise ErrorProduct("Name can`t be empty")
        Logger.log_info(file_name, "NO errors found during status validation.")
        return True
    except ErrorProduct as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation.")
        return False


def check_order(order):
    """
    Validates the order input for a product.

    Parameters:
    order (str): The order quantity of the product.

    Returns:
    bool: True if the order is valid (non-empty, contains only digits, and positive).
          False otherwise, with appropriate error messages logged.

    Raises:
    ErrorProduct: If the order is not valid.
    """
    try:
        order = str(order)
        if len(order) > 0:
            while " " in order:
                order = order.replace(" ", "")
        if len(order) < 1:
            raise ErrorProduct("Order can`t be empty")
        for i in order:
            if not i.isdigit():
                raise ErrorProduct("Order must contain only digits")
        if int(order) <= 0:
            raise ErrorProduct("Order must be a positive number")
        Logger.log_info(file_name, "NO errors found during status validation.")
        return True
    except ErrorProduct as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation.")
        return False


def check_Id(id, produkts):
    """
    Validates the ID of a product to ensure it is a non-empty string of digits and exists in the provided list of products.

    Parameters:
    id (str): The ID of the product to be validated.
    produkts (list): A list of existing products. Each product should have a method get_ID() that returns its ID.

    Returns:
    bool: True if the ID is valid and exists in the list of products.
          False otherwise, with appropriate error messages logged.
    """
    try:
        id = str(id)
        if len(id) > 0:
            while " " in id:
                id = id.replace(" ", "")
        if len(id) < 1:
            raise ErrorProduct("ID can`t be empty")
        for i in id:
            if not i.isdigit():
                raise ErrorProduct("ID must contain only digits")
        flag = False
        for i in produkts:
            print(i.get_ID(), int(id))
            if i.get_ID() == int(id):
                flag = True
                break
        if not flag:
            raise ErrorProduct("ID must be in produkts")
        Logger.log_info(file_name, "NO errors found during status validation.")
        return True
    except ErrorProduct as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation.")
        return False


def check_all(name, mora, price, produkts):
    """
    Validates the input parameters for a new product.

    Parameters:
    name (str): The name of the product.
    mora (str): The mora of the product.
    price (str): The price of the product.
    produkts (list): A list of existing products.

    Returns:
    bool: True if the input parameters are valid and the product name is unique.
          False otherwise, with appropriate error messages logged.
    """
    try:
        if chek_mora(mora) and check_price(price) and check_name(name):
            for prod in produkts:
                if prod.get_name() == name:
                    raise ErrorProduct(
                        "This element (" + name + ") has already been added"
                    )
            Logger.log_info(file_name, "NO errors found during status validation.")
            return True
    except ErrorProduct as e:
        Logger.log_error(file_name, "An error occurred during validation.", str(e))
        return False
