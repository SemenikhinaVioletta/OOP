import d_Error as Error
import sqlite3 as bd
from a_Log import Logger
from a_Global_Per import database, windows
from d_Produkt import produkts, make_array
from f_Class_Status_Client import contract_statuses

file_name = "File Class_Contract"
logger = Logger(file_name, [], "Application started")


class Contract:
    def __init__(self, ID, status, data_start, data_end, products, Mora):
        self.ID = ID
        self.status = 0
        self.set_status(status)
        self.data_start = data_start
        self.data_end = data_end
        self.products = []
        self.mora = Mora
        self.set_products(products)

    def set_products(self, products):
        make_array()
        products = products.split()
        for produkt in produkts:
            for id in products:
                if id == str(produkt.get_ID()):
                    self.products.append(produkt)
                    break

    def set_status(self, status):
        for stat in contract_statuses:
            if stat.get_ID() == status:
                self.status = stat
                break

    def add_product(self, produkt):
        self.products.append(produkt)

    def remove_product(self, produkt):
        self.products.remove(produkt)

    def get_ID(self):
        return int(self.ID)

    def get_status(self):
        return self.status.get_ID()
