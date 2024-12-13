import a_Log
import datetime as t
from datetime import date, datetime

from a_Log import Logger
from a_Global_Per import windows
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno


file_name = "File Error of Contract"
Data = date.today()


class ErrorContract(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[4][-1]
            )
            return "Error Contract, message: {0}".format(self.message)
        else:
            return "Error Contract, raised"


def chek_ID(id, contracts):
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
                    message = "Error in start format (mast be only digits)"
                    raise ErrorContract(message)
        for i in end:
            for j in i:
                if not j.isdigit():
                    message = "Error in end format (mast be only digits)"
                    raise ErrorContract(message)
                
        date1 = date(int(start[0]), int(start[1]), int(start[2]))
        date2 = date(int(end[0]), int(end[1]), int(end[2]))
        if date2 <= date1:
            message = "End date must be after start date"
            raise ErrorContract(message)
        if date_start > Data:
            message = "Start date must be today."
            raise ErrorContract(message)
        message = "Not error in date go to contract..."
        Logger.log_info(file_name, message)
        return True
    except ErrorContract as e:
        Logger.log_error(file_name, "Error in enter Data", str(e))
        return False

