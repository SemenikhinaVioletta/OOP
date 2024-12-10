import b_Class_New_Client as New
from a_Global_Per import windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
from a_Log import Logger

file_name = "File Error of New Klient"
logger = Logger(file_name, "Application started", [])


class ErrorNewClient(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[2][-1]
            )
            return "Error New klient, message: {0}".format(self.message)
        else:
            return "Error New klient, raised"


def chek_name(name):
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
                email[i:].count("") != 1
                or email[i + 1] == ""
                or i >= len(email) - 3
                or i == 0
            ):
                raise ErrorNewClient(message)
        Logger.log_info(file_name, "No errors found during validation")
        return True
    except ErrorNewClient as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation")
        return False


def add_new_to_table(name_entry, phone_entry, email_entry, klients):
    try:
        name = str(name_entry.get())
        phone = str(phone_entry.get())
        email = str(email_entry.get())
        message = "Validation started"
        if chek_name(name) and chek_phone(phone) and chek_mail(email):
            for k in klients:
                if int(phone) == k.get_phone():
                    message = "This phone is already in table"
                    raise ErrorNewClient(message)

                if email == k.get_email():
                    message = "This email is already in table"
                    raise ErrorNewClient(message)

            Logger.log_info(file_name, "No errors found during validation")
            return True
    except ErrorNewClient as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation")
        return False


def delete_from_table(id, klients):
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
        for i in klients:
            if int(id) == i.get_ID():
                flag = True
                break
        if not flag:
            message = "No client with this ID found in table"
            raise ErrorNewClient(message)

        Logger.log_info(file_name, "No errors found during ID validation")
        return True
    except ErrorNewClient as e:
        Logger.log_error(file_name, str(e), "An error occurred during ID validation")
        return False
