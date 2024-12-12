import a_Window as Win
import sqlite3 as bd
import e_Error as Error
import e_Class_Contract as cont
from a_Log import Logger
from a_Global_Per import database, windows

file_name = "File Contract"


def contract_Table(window_contract):
    
    #def add_new():
        
    
    global frame
    frame = Win.Frame(master=window_contract, relief=Win.SUNKEN)
    frame.pack(expand=True)
    """add_new_Client = Win.Button(frame, text="Add Client", command=add_new)
    add_new_Client.grid(row=1, column=2, padx=10, pady=10)
    rename_Client = Win.Button(frame, text="Rename Client", command=rename)
    rename_Client.grid(row=2, column=2, padx=10, pady=10)
    Delete_element = Win.Button(frame, text="Delete", command=delete_element)
    Delete_element.grid(row=3, column=2, padx=10, pady=10)"""
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(4)),
    )
    close_table.grid(row=4, column=2, padx=10, pady=10)
    make_array()
    make_Table()

def make_array():
    global contracts
    contracts = []
    conn = bd.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contracts")
    rows = cursor.fetchall()
    for line in rows:
        produkt = cont.Contract(int(line[0]), int(line[1]), str(line[2]), str(line[3]), str(line[4]), int(line[5]), int(line[6]))
        contracts.append(produkt)
    cursor.close()

def make_Table():
    columns = ("ID", "Status", "Client", "Data of end Contract", "Mora")
    table_contract = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_contract.grid(row=1, column=1, sticky="nsew", rowspan=10)
    table_contract.heading("ID", text="ID", anchor=Win.W)
    table_contract.heading("Status", text="Status", anchor=Win.W)
    table_contract.heading("Client", text="Client", anchor=Win.W)
    table_contract.heading("Data of end Contract", text="Data of end Contract", anchor=Win.W)
    table_contract.heading("Mora", text="Mora", anchor=Win.W)
    table_contract.column("#1", stretch=Win.NO, width=50)
    for produkt in contracts:
        table_contract.insert("", Win.END, values=produkt.get())
    scrollbar = Win.ttk.Scrollbar(
        frame, orient=Win.VERTICAL, command=table_contract.yview
    )


def do_contract(flag, window_contract):
    if flag == 1:
        contract_Table(window_contract)
    else:
        Logger(
            file_name,
            "Error in creating add_contract contractct",
            "Invalid flag in do_contract",
        )
