from tkinter.messagebox import showerror, showwarning, showinfo
import Log
from Log import Logger


class ErrorNewKlient(Exception):
    file_name = "File Error of New Klient"

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            showerror(title="ERROR IN INPUT", message=self.message)
            return "Error New klient, message: {0}".format(self.message)
        else:
            return "Error New klient, raised"


def add_new_to_table(name_entry, phone_entry, email_entry):
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
            Logger("", "Goos name: " + name, "")

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
            Logger("", "Goos phone:" + phone, "")

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
            flag = 0
        else:
            Logger("", "Goos email:" + email, "")

    except ErrorNewKlient:
        Logger(file_name, str(ErrorNewKlient(message)), "")
