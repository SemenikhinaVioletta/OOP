from a_Global_per import basadate
import a_Window as Win
import sqlite3 as bd
import d_Class_Produkt as prod
from a_Log import Logger
import d_Error as Error

file_name = "File Produkt"
logger = Logger(file_name, [], "Application started")


def produkt_Table(window_produkt):
    
    # Функция для создания таблицы клиентов
    def make_Table():
        """
        The function `make_Table` creates a table with specified columns and headings, populating it with data from a list of clients and adding a vertical scrollbar.
        """
        columns = ("ID", "Name", "Cost of one copy", "Copies in stock")
        table_produkt = Win.ttk.Treeview(frame, columns=columns, show="headings")
        table_produkt.grid(row=1, column=1, sticky="nsew", rowspan=10)
        table_produkt.heading("ID", text="ID", anchor=Win.W)
        table_produkt.heading("Name", text="Name", anchor=Win.W)
        table_produkt.heading("Cost of one copy", text="Cost of one copy", anchor=Win.W)
        table_produkt.heading("Copies in stock", text="Copies in stock", anchor=Win.W)
        table_produkt.column("#1", stretch=Win.NO, width=50)
        for produkt in produkts:
            table_produkt.insert("", Win.END, values=produkt.get())
        scrollbar = Win.ttk.Scrollbar(
            frame, orient=Win.VERTICAL, command=table_produkt.yview
        )

    frame = Win.Frame(master=window_produkt, relief=Win.SUNKEN)
    frame.pack(expand=True)
    ''' add_produkt = Win.Button(frame, text="Add Client", command=add_produkt)
    add_produkt.grid(row=1, column=2, padx=10, pady=10)
    rename_produkt = Win.Button(frame, text="Rename Client", command=rename)
    rename_produkt.grid(row=2, column=2, padx=10, pady=10)
    to_Pro = Win.Button(frame, text="Make to Pro", command=do_pro)
    to_Pro.grid(row=3, column=2, padx=10, pady=10)
    Delete_element = Win.Button(frame, text="Delete", command=delete_element)
    Delete_element.grid(row=4, column=2, padx=10, pady=10)'''
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(3)),
    )
    close_table.grid(row=5, column=2, padx=10, pady=10)
    make_Table()


def make_array():
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    for line in rows:
        produkt = prod.Produkt(int(line[0]), str(line[1]), int(line[2]), int(line[3]))
        produkts.append(produkt)
    cursor.close()


def do_produkt(flag, window_produkt):
    global produkts
    produkts = []
    make_array()
    if flag == 1:
        produkt_Table(window_produkt)
    else:
        # Логирование ошибки
        Logger(
            file_name, "Error in creating add_produkt client", "Invalid flag in do_produkt"
        )
