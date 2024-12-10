import a_Log
from a_Log import Logger
from a_Global_Per import windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno


file_name = "File Error of Produkt"


class ErrorProduct(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[3][-1]
            )
            return "Error Produkt, message: {0}".format(self.message)
        else:
            return "Error Produkt, raised"


def chek_mora(mora):
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
                    ")))Mora must contain only digits and mora can`t be < 0"
                )

        Logger.log_info(file_name, "NO errors found during status validation.")
        return True
    except ErrorProduct as e:
        Logger.log_error(file_name, "An error occurred during validation.", str(e))
        return False


def check_price(price):
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
