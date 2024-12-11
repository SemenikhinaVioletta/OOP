import d_Error as Error
import sqlite3 as bd
from a_Log import Logger
from a_Global_Per import database, windows

file_name = "File Class_Contract"
logger = Logger(file_name, [], "Application started")

class Contract:
    def __init__(self, ID, status, data_start, data_end, products, Mora):
        