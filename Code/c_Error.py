from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import a_Log
from a_Log import Logger
from a_Global_per import status_klient

file_name = "File Error of Pro Klient"


class ErrorProKlient(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent = False
            )  # Показываем сообщение об ошибке
            return "Error Pro klient, message: {0}".format(self.message)
        else:
            return "Error Pro klient, raised"


def chek_name(name_entry):
    name = str(name_entry.get())  # Получаем имя
    message = "Validation started."  # Сообщение о начал
    names = name.split()  # Разделяем имя на части
    try:
        if len(names) < 3:
            message = "Name must contain at least 3 words."  # Исправлено на более информативное сообщение
            raise ErrorProKlient(message)
        else:
            for i in names:
                if i[0].islower():
                    message = "Each word in the name must start with an uppercase letter."  # Исправлено на более информативное сообщение
                    raise ErrorProKlient(message)
                else:
                    for j in i:
                        if not j.isalpha():
                            message = "Name must contain only alphabetic characters."  # Исправлено на более информативное сообщение
                            raise ErrorProKlient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
        return False


def chek_phone(phone_entry):
    phone = str(phone_entry.get())
    message = "Validation started."  # Сообщение о начал
    try:
        if len(phone) != 11:
            message = "Phone number must be exactly 11 digits long."  # Исправлено на более информативное сообщение
            raise ErrorProKlient(message)
        elif phone[0] == "0":
            message = "Phone number must not start with zero."  # Исправлено на более информативное сообщение
            raise ErrorProKlient(message)
        else:
            for j in phone:
                if not j.isdigit():
                    message = "Phone number must contain only digits."  # Исправлено на более информативное сообщение
                    raise ErrorProKlient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
        return False


def chek_email(email_entry):
    email = str(email_entry.get())  # Получаем email
    message = "Validation started."  # Сообщение о начале валидации
    try:
        if len(email) < 5:
            message = 'Email must contain at least 5 characters, e.g., "example@domain.com".'  # Исправлено на более информативное сообщение
            raise ErrorProKlient(message)
        elif email.count("@") != 1:
            message = "Email must contain exactly one '@' symbol."  # Исправлено на более информативное сообщение
            raise ErrorProKlient(message)
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
                message = "Email must contain exactly one '.' symbol after the '@' symbol."  # Исправлено на более информативное сообщение
                raise ErrorProKlient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
        return False


def chek_mora(mora_entry):
    mora = str(mora_entry.get())  # Получаем email
    message = "Validation started."  # Сообщение о начале валидации
    try:
        if len(mora) != 0:
            for i in mora:
                if not i.isdigit():
                    message = "Mora must contain only digits and > 0"  # Исправлено на более информативное сообщение
                    raise ErrorProKlient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
        return False


"""def chek_kontrakt(kontrakt_entry):
    kontrakt = str(kontrakt_entry.get())
    message = "Validation started."  # Сообщение о начале валидации
    try:
        if len(kontrakt) != 0:
            for i in kontrakt:
                if not i.isdigit():
                    message = "Mora must contain only digits and > 0"  # Исправлено на более информативное сообщение
                    raise ErrorProKlient(message)
        Logger.log_info(file_name, "NO errors found during validation.")
        return True

    except ErrorProKlient as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation.")
        return False  # Логируем ошибку"""


def chek_id(id):
    try:
        id = id.get()
        message = (
            "No errors found during ID validation."  # Сообщение о начале валидации
        )

        # Проверка ID
        if len(id) != 0:
            for j in id:
                if not j.isdigit():
                    message = "ID must contain only digits."  # Исправлено на более информативное сообщение
                    raise ErrorProKlient(message)
        else:
            message = (
                "ID cannot be empty."  # Исправлено на более информативное сообщение
            )
            raise ErrorProKlient(message)

        Logger.log_info(file_name, "No errors found during ID validation.")
        return True
    except ErrorProKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during ID validation."
        )  # Логируем ошибку
        return False


# Функция для добавления нового клиента в таблицу
def add_pro_to_table(name_entry, phone_entry, email_entry, mora_entry, klients):
    try:
        if (
            not chek_name(name_entry)
            or not chek_phone(phone_entry)
            or not chek_email(email_entry)
            or not chek_mora(mora_entry)
        ):
            message = "Error in element to add"
            raise ErrorProKlient(message)
        phone = int(phone_entry.get())
        email = str(email_entry.get())
        for k in klients:
            if int(phone) == k.get_phone():
                message = "This phone is already in table"
                raise ErrorProKlient(message)
            
            if email == k.get_email():
                message = "This email is already in table"
                raise ErrorProKlient(message)

        return True
    except ErrorProKlient as e:
        if e != "Error in element to add":
            Logger.log_error(
                file_name, str(e), "An error occurred during ID validation."
            )  # Логируем ошибку
        return False
