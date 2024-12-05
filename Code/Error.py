from tkinter.messagebox import showerror, showwarning, showinfo
import Log
from Log import Logger
import Class_New_klient as New

file_name = "File Error of New Klient"

# Класс для обработки ошибок нового клиента
class ErrorNewKlient(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            showerror(title="ERROR IN INPUT", message=self.message)  # Показываем сообщение об ошибке
            return "Error New klient, message: {0}".format(self.message)
        else:
            return "Error New klient, raised"

# Функция для добавления нового клиента в таблицу
def add_new_to_table(name_entry, phone_entry, email_entry):
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
            raise ErrorNewKlient(message)  # Вызываем ошибку, если есть проблемы с именем
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
            raise ErrorNewKlient(message)  # Вызываем ошибку, если есть проблемы с телефоном
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
            if email[i:].count(".") != 1 or email[i + 1] == "." or i >= len(email) - 3 or i == 0:
                message = "Email must contain exactly one '.' symbol after the '@' symbol."  # Исправлено на более информативное сообщение
                flag = 1

        if flag == 1:
            raise ErrorNewKlient(message)  # Вызываем ошибку, если есть проблемы с email
        else:
            pass

    except ErrorNewKlient as e:
        Logger.log_error(file_name, str(e), "An error occurred during validation.")  # Логируем ошибку
    finally:
        if flag == 0:
            Logger.log_info(file_name, "No errors found during validation.")  # Логируем успешную проверку
        return flag  # Возвращаем флаг

# Функция для удаления клиента из таблицы
def delete_from_table(id):
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
            message = "ID cannot be empty."  # Исправлено на более информативное сообщение
            flag = 1

        if flag == 1:
            raise ErrorNewKlient(message)  # Вызываем ошибку, если есть проблемы с ID
        else:
            pass

    except ErrorNewKlient as e:
        Logger.log_error(file_name, str(e), "An error occurred during ID validation.")  # Логируем ошибку
    finally:
        if flag == 0:
            Logger.log_info(file_name, "No errors found during ID validation.")  # Логируем успешную проверку
        return flag  # Возвращаем флаг
