from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import Log
from Log import Logger
import Class_New_klient as New

file_name = "File Error of New Klient"


# Класс для обработки ошибок нового клиента
# The `ErrorNewKlient` class in Python defines a custom exception with an error message attribute that is displayed when the exception is raised.
class ErrorNewKlient(Exception):
    def __init__(self, *args):
        """
        This Python function initializes an object with a message attribute based on the provided arguments.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """
        The function returns an error message if one is provided, otherwise it indicates that an error was raised.
        
        @return The `__str__` method is returning a string based on the condition of whether `self.message` is truthy or falsy. If `self.message` is truthy, it will display an error message using `showerror` and return a formatted string indicating an error with the message. If `self.message` is falsy, it will simply return a string indicating an error was raised
        """
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message
            )  # Показываем сообщение об ошибке
            return "Error New klient, message: {0}".format(self.message)
        else:
            return "Error New klient, raised"


# Функция для добавления нового клиента в таблицу
def add_new_to_table(name_entry, phone_entry, email_entry):
    """
    The function `add_new_to_table` validates and adds a new client to a table, checking for errors in the name, phone number, and email address entries.
    
    @param name_entry The `name_entry`, `phone_entry`, and `email_entry` parameters are likely tkinter Entry widgets or similar GUI input fields where users can enter their name, phone number, and email address respectively. These widgets are used to retrieve the user input as strings for validation in the `add_new_to_table
    @param phone_entry The `phone_entry` parameter in the `add_new_to_table` function is likely a GUI entry field where the user can input their phone number. The function retrieves the phone number entered by the user and performs validation checks on it to ensure it meets certain criteria, such as being exactly 11 digits
    @param email_entry The `email_entry` parameter in the `add_new_to_table` function is used to get the email input from the user interface. It is expected to be a widget or element that allows the user to enter their email address. The function then validates this email input based on certain criteria such as length
    
    @return The function `add_new_to_table` returns the `flag` variable, which indicates whether there were any errors during the validation process. If `flag` is 0, it means no errors were found during validation. If `flag` is 1, it means there were validation errors.
    """
    flag = 0  # Флаг для отслеживания ошибок
    try:
        name = str(name_entry.get())  # Получаем имя
        phone = str(phone_entry.get())  # Получаем телефон
        email = str(email_entry.get())  # Получаем email
        message = "Validation started."  # Сообщение о начале валидации
        names = name.split()  # Разделяем имя на части

        # Проверка имени
        if len(names) < 3:
            message = "Name must contain at least 3 words."  # Исправлено на более информативное сообщение
            flag = 1
        else:
            for i in names:
                if i[0].islower():
                    message = "Each word in the name must start with an uppercase letter."  # Исправлено на более информативное сообщение
                    flag = 1
                else:
                    for j in i:
                        if not j.isalpha():
                            message = "Name must contain only alphabetic characters."  # Исправлено на более информативное сообщение
                            flag = 1
                            break
                if flag == 1:
                    break

        if flag == 1:
            raise ErrorNewKlient(
                message
            )  # Вызываем ошибку, если есть проблемы с именем
        else:
            pass

        # Проверка телефона
        if len(phone) != 11:
            message = "Phone number must be exactly 11 digits long."  # Исправлено на более информативное сообщение
            flag = 1
        elif phone[0] == "0":
            message = "Phone number must not start with zero."  # Исправлено на более информативное сообщение
            flag = 1
        else:
            for j in phone:
                if not j.isdigit():
                    message = "Phone number must contain only digits."  # Исправлено на более информативное сообщение
                    flag = 1
                    break

        if flag == 1:
            raise ErrorNewKlient(
                message
            )  # Вызываем ошибку, если есть проблемы с телефоном
        else:
            pass

        # Проверка email
        if len(email) < 5:
            message = 'Email must contain at least 5 characters, e.g., "example@domain.com".'  # Исправлено на более информативное сообщение
            flag = 1
        elif email.count("@") != 1:
            message = "Email must contain exactly one '@' symbol."  # Исправлено на более информативное сообщение
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
                message = "Email must contain exactly one '.' symbol after the '@' symbol."  # Исправлено на более информативное сообщение
                flag = 1

        if flag == 1:
            raise ErrorNewKlient(message)  # Вызываем ошибку, если есть проблемы с email
        else:
            pass

    except ErrorNewKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during validation."
        )  # Логируем ошибку
    finally:
        if flag == 0:
            Logger.log_info(
                file_name, "No errors found during validation."
            )  # Логируем успешную проверку
        return flag  # Возвращаем флаг


# Функция для удаления клиента из таблицы
def delete_from_table(id):
    """
    The function `delete_from_table` validates an ID input and logs any errors or successful validation.
    
    @param id The `delete_from_table` function takes an `id` parameter, which is used to identify the entry that needs to be deleted from a table. The function performs validation on the `id` to ensure it meets certain criteria before proceeding with the deletion operation.
    
    @return The function `delete_from_table` returns the `flag` variable, which is used to track errors during the validation process. If no errors are found during the ID validation, the flag will be 0, indicating success. If there are errors, the flag will be set to 1.
    """
    flag = 0  # Флаг для отслеживания ошибок
    try:
        id = id.get()  # Получаем ID
        flag = 0
        message = "Validation started."  # Сообщение о начале валидации

        # Проверка ID
        if len(id) != 0:
            for j in id:
                if not j.isdigit():
                    message = "ID must contain only digits."  # Исправлено на более информативное сообщение
                    flag = 1
                    break
            if flag == 0:
                if int(id) < 0:
                    message = "ID must be greater than or equal to 0."  # Исправлено на более информативное сообщение
                    flag = 1
        else:
            message = (
                "ID cannot be empty."  # Исправлено на более информативное сообщение
            )
            flag = 1

        if flag == 1:
            raise ErrorNewKlient(message)  # Вызываем ошибку, если есть проблемы с ID
        else:
            pass

    except ErrorNewKlient as e:
        Logger.log_error(
            file_name, str(e), "An error occurred during ID validation."
        )  # Логируем ошибку
    finally:
        if flag == 0:
            Logger.log_info(
                file_name, "No errors found during ID validation."
            )  # Логируем успешную проверку
        return flag  # Возвращаем флаг
