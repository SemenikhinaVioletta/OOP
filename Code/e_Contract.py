import a_Window as Win
import sqlite3 as bd
import e_Error as Error
import e_Class_Contract as cont
from a_Log import Logger
from a_Global_Per import database, windows

file_name = "File Contract"
logger = Logger(file_name, [], "Application started")



def make_array():
    global contracts
    contracts = []
    conn = bd.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contracts")
    rows = cursor.fetchall()
    for line in rows:
        produkt = cont.Contract(int(line[0]), int(line[1]), int(line[2]), int(line[3]), str(line[4]), int(line[5]))
        contracts.append(produkt)
    cursor.close()

def make_Table():
    columns = ("ID", "Name", "Cost of one copy", "Copies in stock")
    table_produkt = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_produkt.grid(row=1, column=1, sticky="nsew", rowspan=10)
    table_produkt.heading("ID", text="ID", anchor=Win.W)
    table_produkt.heading("Name", text="Name", anchor=Win.W)
    table_produkt.heading("Cost of one copy", text="Cost of one copy", anchor=Win.W)
    table_produkt.heading("Copies in stock", text="Copies in stock", anchor=Win.W)
    table_produkt.column("#1", stretch=Win.NO, width=50)
    for produkt in contracts:
        table_produkt.insert("", Win.END, values=produkt.get())
    scrollbar = Win.ttk.Scrollbar(
        frame, orient=Win.VERTICAL, command=table_produkt.yview
    )


def do_product(flag, window_contract):
    if flag == 1:
        contract_Table(window_contract)
    else:
        Logger(
            file_name,
            "Error in creating add_contract product",
            "Invalid flag in do_contract",
        )
