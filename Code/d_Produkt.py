import a_Window as Win
import sqlite3 as bd
import d_Class_Produkt as prod
import d_Error as Error
from a_Log import Logger
from a_Global_Per import database, windows

file_name = "File Produkt"
produkts = []
logger = Logger(file_name, [], "Application started")


def produkt_Table(window_produkt):

    def take_this(name_entry, coast_entry, number_entry):
        if Error.check_all(
            name_entry.get(), coast_entry.get(), number_entry.get(), produkts
        ):
            produkt = prod.Produkt(
                produkts[-1].get_ID() + 1,
                str(name_entry.get()),
                int(coast_entry.get()),
                int(number_entry.get()),
                0,
            )
            produkt.enter_produkt_to_bd()
            produkts.append(produkt)
            frame.destroy()
            produkt_Table(window_produkt)

    def make_this(produkt, get_order):
        try:
            if Error.check_order(get_order.get()):
                get_number = produkt.get_number() + int(get_order.get())
                produkt.order(get_number)
                frame.destroy()
                produkt_Table(window_produkt)
        except Error.ErrorProduct:
            pass

    def do_this(produkt, name_entry, mora_entry, number_entry):
        if Error.check_all(
            name_entry.get(), mora_entry.get(), number_entry.get(), produkts
        ):
            produkt.set_number(number_entry.get())
            produkt.rename_produkt(
                str(name_entry.get()), int(mora_entry.get()), produkts
            )
            frame.destroy()
            produkt_Table(window_produkt)

    def get_text(id, frame_for, wind):
        try:
            if Error.check_Id(id.get(), produkts):
                flag = 0
                id = int(id.get())
                for produkt in produkts:
                    if produkt.ID == id:
                        flag = 1
                        name_text = Win.Label(
                            frame_for,
                            text="Enter new name for produkt",
                        )
                        name_entry = Win.Entry(frame_for)
                        name_text.grid(row=2, column=1)
                        name_entry.insert(0, produkt.get_name())
                        name_entry.grid(row=2, column=2, padx=5)
                        phone_text = Win.Label(
                            frame_for,
                            text="Enter new cost of produkt",
                        )
                        phone_entry = Win.Entry(frame_for)
                        phone_text.grid(row=3, column=1, pady=5)
                        phone_entry.insert(0, str(produkt.get_mora()))
                        phone_entry.grid(row=3, column=2, pady=5, padx=5)
                        number_text = Win.Label(
                            frame_for,
                            text="Enter new numbers of produkts in sclad",
                        )
                        number_entry = Win.Entry(frame_for)
                        number_text.grid(row=4, column=1, pady=5)
                        number_entry.insert(0, produkt.get_number())
                        number_entry.grid(row=4, column=2, pady=5, padx=5)
                        save_button = Win.Button(
                            frame_for,
                            text="Save",
                            command=(
                                lambda: do_this(
                                    produkt, name_entry, phone_entry, number_entry
                                )
                            ),
                        )
                        save_button.grid(row=5, column=1, pady=5)
                        break
                if flag == 0:
                    message = f"Client with ID = {id} not found!"
                    raise Error.ErrorProduct(message)
        except Error.ErrorProduct:
            wind.close_window(3)

    def add_produkt():
        try:
            if len(windows[3]) < 2:
                wind = Win.Window("Add Produkt", "600x300")
                wind.make_protokol(lambda: wind.close_window(3))
                windows[3].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                name_text = Win.Label(
                    frame_for,
                    text="Enter name of produkt",
                )
                name_entry = Win.Entry(frame_for)
                name_text.grid(row=1, column=1)
                name_entry.grid(row=1, column=2, padx=5)
                mora_text = Win.Label(
                    frame_for,
                    text="Enter cost or product",
                )
                mora_entry = Win.Entry(frame_for)
                mora_text.grid(row=2, column=1, pady=5)
                mora_entry.grid(row=2, column=2, pady=5, padx=5)
                numbers_text = Win.Label(
                    frame_for, text="Enter the quantity of the product in stock"
                )
                numbers_entry = Win.Entry(frame_for)
                numbers_text.grid(row=3, column=1, pady=5)
                numbers_entry.grid(row=3, column=2, pady=5, padx=5)
                save_button = Win.Button(
                    frame_for,
                    text="Save",
                    command=(lambda: take_this(name_entry, mora_entry, numbers_entry)),
                )
                save_button.grid(row=4, column=1, pady=5)
                delete_button = Win.Button(
                    frame_for, text="Back", command=lambda: wind.close_window(3)
                )
                delete_button.grid(row=4, column=2, pady=5, padx=5)
            else:
                raise Error.ErrorProduct(
                    "Please close other windows for work with new produkt"
                )
        except Error.ErrorProduct as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def id_for_delite(id):
        if Error.check_Id(id.get(), produkts):
            id = int(id.get())
            for produkt in produkts:
                if produkt.get_ID() == id:
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the product with ID: {id}, Name: {produkt.get_name()}?",
                        parent=windows[3][-1],
                    )
                    if confirm:
                        produkt.delete_produkt_from_bd()
                        produkts.remove(produkt)
                        frame.destroy()
                        produkt_Table(window_produkt)
                    break

    def delete_element():
        try:
            if len(windows[3]) < 2:
                wind = Win.Window("Delete  produkt", "500x300")
                wind.make_protokol(lambda: wind.close_window(3))
                windows[3].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                Id_for_delite = Win.Label(
                    frame_for, text="Enter ID of the product you want to delete:"
                )
                Id_for_delite.grid(row=1, column=1, padx=5, pady=5)
                text_for_delite = Win.Entry(frame_for)
                text_for_delite.grid(row=1, column=2, padx=5)
                button_for_delite = Win.Button(
                    frame_for,
                    text="Delete",
                    command=lambda: id_for_delite(text_for_delite),
                )
                button_for_delite.grid(row=2, column=2, padx=5)
                Id_for_delite.grid(row=1, column=1, padx=5, pady=5)
            else:
                raise Error.ErrorProduct(
                    "Please close other windows for work with new produkt"
                )
        except Error.ErrorProduct as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def get_number(ID_entry, frame_for, wind):
        try:
            if Error.check_Id(ID_entry.get(), produkts):
                flag = 0
                id = int(ID_entry.get())
                for produkt in produkts:
                    if produkt.ID == id:
                        flag = 1
                        number_text = Win.Label(
                            frame_for,
                            text="Produсt in storage:",
                        )
                        number_entry = Win.Label(
                            frame_for, text=str(produkt.get_number())
                        )
                        number_text.grid(row=2, column=1)
                        number_entry.grid(row=2, column=2, padx=5)
                        order_text = Win.Label(
                            frame_for,
                            text="Enter how mach you want order produkt",
                        )
                        order_entry = Win.Entry(frame_for)
                        order_text.grid(row=3, column=1, pady=5)
                        order_entry.grid(row=3, column=2, pady=5, padx=5)

                        save_button = Win.Button(
                            frame_for,
                            text="Order",
                            command=(lambda: make_this(produkt, order_entry)),
                        )
                        save_button.grid(row=5, column=1, pady=5)
                        break
                if flag == 0:
                    message = f"Client with ID = {id} not found!"
                    raise Error.ErrorProduct(message)
        except Error.ErrorProduct:
            wind.close_window(3)

    def rename():
        try:
            if len(windows[3]) < 2:
                wind = Win.Window("Rename New produkt", "600x300")
                wind.make_protokol(lambda: wind.close_window(3))
                windows[3].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                ID_text = Win.Label(
                    frame_for, text="Enter ID of the product you want to rename:"
                )
                ID_entry = Win.Entry(frame_for)
                ID_find = Win.Button(
                    frame_for,
                    text="Find element",
                    command=lambda: get_text(ID_entry, frame_for, wind),
                )
                ID_find.grid(row=1, column=3, padx=5)
                ID_text.grid(row=1, column=1)
                ID_entry.grid(row=1, column=2, padx=5)
                delete_button = Win.Button(
                    frame_for, text="Back", command=lambda: wind.close_window(3)
                )
                delete_button.grid(row=5, column=2, pady=5, padx=5)
            else:
                raise Error.ErrorProduct(
                    "Please close other windows for work with new produkt"
                )
        except Error.ErrorProduct as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def order():
        try:
            if len(windows[3]) < 2:
                wind = Win.Window("Jrder produkt", "600x300")
                wind.make_protokol(lambda: wind.close_window(3))
                windows[3].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                ID_text = Win.Label(
                    frame_for, text="Enter ID of the product you want to order:"
                )
                ID_entry = Win.Entry(frame_for)
                ID_find = Win.Button(
                    frame_for,
                    text="Find element",
                    command=lambda: get_number(ID_entry, frame_for, wind),
                )
                ID_find.grid(row=1, column=3, padx=5)
                ID_text.grid(row=1, column=1)
                ID_entry.grid(row=1, column=2, padx=5)
                delete_button = Win.Button(
                    frame_for, text="Back", command=lambda: wind.close_window(3)
                )
                delete_button.grid(row=5, column=2, pady=5, padx=5)
            else:
                raise Error.ErrorProduct(
                    "Please close other windows for work with new produkt"
                )
        except Error.ErrorProduct as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    global frame
    frame = Win.Frame(master=window_produkt, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_prod = Win.Button(frame, text="Add Produkt", command=add_produkt)
    add_prod.grid(row=11, column=1, padx=10, pady=10)
    """
        rename_produkt = Win.Button(frame, text="Rename Produkt", command=rename)
        rename_produkt.grid(row=2, column=2, padx=10, pady=10)
        rename_produkt = Win.Button(frame, text="Order", command=order)
        rename_produkt.grid(row=3, column=2, padx=10, pady=10)
        Delete_element = Win.Button(frame, text="Delete", command=delete_element)
        Delete_element.grid(row=4, column=2, padx=10, pady=10)
    """
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(3)),
    )
    close_table.grid(row=11, column=3, padx=10, pady=10)
    make_array()
    make_Table()


def make_array():
    produkts.clear()
    conn = bd.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produkts")
    rows = cursor.fetchall()
    for line in rows:
        produkt = prod.Produkt(
            int(line[0]), str(line[1]), int(line[2]), int(line[3]), int(line[4])
        )
        produkts.append(produkt)
    cursor.close()


def make_Table():
    def on_select(event):
        cur_item = table_produkt.item(table_produkt.focus())
        col = table_produkt.identify_column(event.x)
        if col == "#0":
            cell_value = cur_item["text"]
        else:
            if len(cur_item["values"]) != 0:
                cell_value = cur_item["values"][0]
                Logger.log_info(file_name, f"You tap on product with ID: {cell_value}")

    columns = ("ID", "Name", "Cost of one copy", "Copies in stock")
    table_produkt = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_produkt.grid(row=1, column=1, sticky="nsew", columnspan=3)
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
    table_produkt.bind("<ButtonRelease-1>", on_select)


def do_product(flag, window_produkt):
    if flag == 1:
        produkt_Table(window_produkt)
    else:
        Logger(
            file_name,
            "Error in creating add_produkt product",
            "Invalid flag in do_produkt",
        )
