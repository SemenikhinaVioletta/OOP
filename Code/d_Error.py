import a_Log
from a_Log import Logger
from a_Global_per import windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno


file_name = "File Error of Produkt"


class ErrorProduct(Exception):
    """
    Custom exception class for handling errors related to product input.

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
        *args: Variable length argument list. The first argument is considered as the error message.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        Return the string representation of the error message.

        If the error message is provided, display an error message box and return a formatted string.
        If no error message is provided, return a default string.

        Returns:
        str: The string representation of the error message.
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[3][-1]
            )  # Показываем сообщение об ошибке
            return "Error Produkt, message: {0}".format(self.message)
        else:
            return "Error Produkt, raised"


def chek_mora(mora):
    """
    Validates the mora value of a product.

    This function checks if the provided mora value is a valid positive number.
    It raises an ErrorProduct exception if the mora value is not a positive number or contains non-digit characters.

    Parameters:
    mora (int or str): The mora value of the product to be validated.

    Returns:
    bool: True if the mora value is valid, False otherwise.

    Raises:
    ErrorProduct: If the mora value is not a positive number or contains non-digit characters.
    """
    try:
        mora = str(mora)
        if len(mora) < 1:
            raise ErrorProduct("Morad must be a positive number")
        for i in mora:
            if not i.isdigit():
                print(i)
                raise ErrorProduct(
                    ")))Mora must contain only digits and mora can`t be < 0"
                )

        Logger.log_info(file_name, "NO errors found during status validation.")
        return True
    except ErrorProduct as e:
        Logger.log_error(file_name, "An error occurred during validation.", str(e))
        return False


def check_price(price):
    """
    Validates the price of a product.

    This function checks if the provided price is a valid positive integer.
    It raises an ErrorProduct exception if the price is not a positive number or contains non-digit characters.

    Parameters:
    price (int or str): The price of the product to be validated.

    Returns:
    bool: True if the price is valid, False otherwise.

    Raises:
    ErrorProduct: If the price is not a positive number or contains non-digit characters.
    """
    try:
        price = str(price)
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
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # ��огируем ошибку
        return False


def check_name(name):
    """
    Validates the name of a product.

    This function checks if the provided name is valid according to the defined rules.
    It raises an ErrorProduct exception if the name is empty.

    Parameters:
    name (str): The name of the product to be validated.

    Returns:
    bool: True if the name is valid, False otherwise.

    Raises:
    ErrorProduct: If the name is empty.
    """
    try:
        name = str(name)
        if len(name) < 1:
            raise ErrorProduct("Name can`t be empty")
        Logger.log_info(file_name, "NO errors found during status validation.")
        return True
    except ErrorProduct as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # ��огируем ошибку
        return False

def check_order(order):
    try:
        order = str(order)
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
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        ) 
        return False

def check_Id(id, produkts):
    """
    Validates the ID of a product against a list of existing product IDs.

    Parameters:
    id (str): The ID of the product to be validated.
    produkts (list): A list of existing product IDs.

    Returns:
    bool: True if the ID is valid and does not exist in the produkts list, False otherwise.
    Raises:
    ErrorProduct: If the ID is empty, contains non-digit characters, or does not exist in the produkts list.
    """
    try:
        id = str(id)
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
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # ��огируем ошибку
        return False


def check_all(name, mora, price, produkts):
    """
    Validates the input data for a product.

    This function checks if the provided mora, price, and name are valid according to the defined rules.
    It also checks if the name already exists in the list of products.

    Parameters:
    mora (int or str): The mora value of the product.
    price (int or str): The price value of the product.
    name (str): The name of the product.
    produkts (list): A list of existing product objects.

    Returns:
    bool: True if the input data is valid and the name does not exist in the produkts list, False otherwise.

    Raises:
    ErrorProduct: If the mora, price, or name are invalid, or if the name already exists in the produkts list.
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
