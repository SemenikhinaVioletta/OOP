import a_Window as Win
import sqlite3 as bd
import e_Error as Error
import e_Class_Contract as cont
import datetime as t
from datetime import date
from a_Log import Logger
from a_Global_Per import database, windows
from c_proClient import pro_client as clients
from d_Produkt import produkts
from d_Produkt import make_array as make_prod
from c_proClient import make_array as make_pro

file_name = "File Contract"
Date = date.today()
contracts = []
produkts_to_contract = []


def contract_Table(window_contract):

    def add_product_to_contract(product):
        try:
            make_prod()
            product = str(product).split()
            product = int(product[0])
            if Error.chek_product(product, produkts):
                for i in produkts:
                    if produkts_to_contract.count(i.get_ID()) + 1 > i.get_number():
                        message = "Not this product in magazines"
                        raise Error.ErrorContract(message)
                    if i.get_ID() == product:
                        produkts_to_contract.append(i.get_ID())
                        break
        except Error.ErrorContract as e:
            Logger.log_error(file_name, "Error in add product to contract", str(e))

    def save(client, end_data):
        try:
            for i in clients:
                if i.get_ID() == int(client.split()[0]):
                    client = i
                    break
            if Error.chek_date(Date, end_data) and len(produkts_to_contract) != 0:
                for i in clients:
                    if i.get_ID() == client.get_ID():
                        contract = cont.Contract(
                            len(contracts) + 1,
                            1,
                            Date,
                            end_data,
                            produkts_to_contract,
                            0,
                            i.get_ID(),
                        )
                        contract.set_mora()
                        contract.add_to_bd()
                frame.destroy()
                contract_Table(window_contract)
                remake_cli_prod(contract)
        except Error.ErrorContract as e:
            Logger.log_error(file_name, "Error in add contract", str(e))

    def add_new():
        try:
            if len(windows[4]) == 2:
                raise Error.ErrorContract(
                    "Please close other windows for work with pro Contract"
                )

            wind = Win.Window("Add Contract", "600x300")
            wind.make_protokol(lambda: wind.close_window(4))
            windows[4].append(wind)
            frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
            frame_for.pack(expand=True)
            text_client = Win.Label(frame_for, text="Enter Contracts:")
            text_client.grid(row=1, column=1)
            box_client = make_combobox(0, clients, 1, frame_for)
            text_product = Win.Label(frame_for, text="Enter Products:")
            text_product.grid(row=2, column=1)
            box_product = make_combobox(1, produkts, 2, frame_for)

            button_product = Win.Button(
                frame_for,
                text="add product\nto kontrakt",
                command=lambda: add_product_to_contract(box_product.get()),
            )
            button_product.grid(row=2, column=3, padx=5, pady=5)
            text_data = Win.Label(
                frame_for, text="The contract is concluded from\t" + str(Date) + "\tto:"
            )
            text_data.grid(row=3, column=1, columnspan=2, padx=5, pady=30)
            entr_data = Win.Entry(
                frame_for,
            )
            entr_data.grid(row=3, column=3)
            text_status = Win.Label(frame_for, text="Start status:\t1\tIn process")
            text_status.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

            button_save = Win.Button(
                frame_for,
                text="Save",
                command=lambda: save(str(box_client.get()), entr_data.get()),
            )
            button_save.grid(row=5, column=1, padx=10, pady=10)
            button_back = Win.Button(
                frame_for, text="Back", command=lambda: wind.close_window(4)
            )
            button_back.grid(row=5, column=2, padx=10, pady=10)

        except Error.ErrorContract as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def id_for_delite(id):
        if Error.chek_ID(id.get(), contracts):
            id = int(id.get())
            for contract in contracts:
                if contract.get_ID() == id:
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the contract with ID: {id}?",
                        parent=windows[4][-1],
                    )
                    if confirm:
                        contract.delete_contract_from_bd()
                        contracts.remove(contract)
                        frame.destroy()
                        contract_Table(window_contract)
                    break

    def delete_element():
        try:
            if len(windows[4]) < 2:
                wind = Win.Window("Delete Contract", "500x300")
                wind.make_protokol(lambda: wind.close_window(4))
                windows[4].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                Id_for_delite = Win.Label(
                    frame_for, text="Enter ID of the contract you want to delete:"
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
                raise Error.ErrorContract(
                    "Please close other windows for work with contract"
                )
        except Error.ErrorContract as e:
            Error.Logger.log_error(file_name, "Error with opend windows.", str(e))

    def end_contract(text_for_delite):
        id = int(text_for_delite.get())
        if Error.chek_ID(id, contracts):
            for contract in contracts:
                if contract.get_ID() == id:
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to end the contract with ID: {id}?",
                        parent=windows[4][-1],
                    )
                    if confirm:
                        contract.set_status(2)
                        contract.update_status()
                        frame.destroy()
                        contract_Table(window_contract)
                    break

    def end_new():
        try:
            if len(windows[4]) < 2:
                wind = Win.Window("End Contract", "500x300")
                wind.make_protokol(lambda: wind.close_window(4))
                windows[4].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                Id_for_delite = Win.Label(
                    frame_for, text="Enter ID of the contract you want to end:"
                )
                Id_for_delite.grid(row=1, column=1, padx=5, pady=5)
                text_for_delite = Win.Entry(frame_for)
                text_for_delite.grid(row=1, column=2, padx=5)
                button_for_delite = Win.Button(
                    frame_for,
                    text="End contract",
                    command=lambda: end_contract(text_for_delite),
                )
                button_for_delite.grid(row=2, column=2, padx=5)
                Id_for_delite.grid(row=1, column=1, padx=5, pady=5)
            else:
                raise Error.ErrorContract(
                    "Please close other windows for work with contract"
                )
        except Error.ErrorContract as e:
            Error.Logger.log_error(file_name, "Error with opend windows.", str(e))

    global frame
    frame = Win.Frame(master=window_contract, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_new_Contract = Win.Button(frame, text="Add Contract", command=add_new)
    add_new_Contract.grid(row=11, column=1, padx=10, pady=10)
    """
        add_new_Contract = Win.Button(frame, text="End Contract", command=end_new)
        add_new_Contract.grid(row=2, column=2, padx=10, pady=10)
        Delete_element = Win.Button(frame, text="Delete", command=delete_element)
        Delete_element.grid(row=3, column=2, padx=10, pady=10)
    """
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(4)),
    )
    close_table.grid(row=11, column=3, padx=10, pady=10)
    make_array()
    make_Table()


def remake_cli_prod(contract):
    make_pro()
    make_prod()
    make_array()
    for i in produkts:
        for prod in contract.get_produkts_to_bd().split():
            if i.get_ID() == int(prod):
                i.set_number(-1)
                i.order(i.get_number())
                i.set_zakazano(1)
        i.rename_produkt(i.get_name(), i.get_mora(), produkts)
    for cli in clients:
        if cli.get_ID() == contract.get_client_id():
            cli.add_contract(contracts[-1])
            cli.rename_client(
                cli.get_name(),
                cli.get_phone(),
                contract.get_mora(),
                cli.get_email(),
                cli.status,
                cli.get_contract_id(),
                clients,
            )
            break
    make_pro()
    make_prod()


def make_array():
    contracts.clear()
    conn = bd.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contracts")
    rows = cursor.fetchall()
    for line in rows:
        produkt = cont.Contract(
            int(line[0]),
            int(line[1]),
            str(line[2]),
            str(line[3]),
            str(line[4]).split(),
            int(line[5]),
            int(line[6]),
        )
        contracts.append(produkt)
    cursor.close()


def make_combobox(flag, array, row_index, parent_frame):
    value = []
    if flag == 0:
        for client in array:
            print(client.contract)
            if len(client.contract) != 0:
                if client.contract[-1] == 2:
                    value.append(str(client.get_ID()) + " \t" + client.get_short_name())
            else:
                value.append(str(client.get_ID()) + " \t" + client.get_short_name())
    if flag == 1:
        for product in array:
            if product.get_number() > 0:
                value.append(str(product.get_ID()) + " \t" + product.get_name())
    combobox = Win.Combobox(parent_frame, values=value, width=35, state="readonly")
    combobox.grid(row=row_index, column=2, padx=5, pady=5)
    if len(value) != 0:
        combobox.set(value[0])
    else:
        combobox.set("Sorry haven`t got good client")
    return combobox


def make_Table():
    def on_select(event):
        cur_item = table_contract.item(table_contract.focus())
        col = table_contract.identify_column(event.x)
        if col == "#0":
            cell_value = cur_item["text"]
        else:
            if len(cur_item["values"]) != 0:
                cell_value = cur_item["values"][0]
                Logger.log_info(file_name, f"You tap on contract with ID: {cell_value}")

    columns = ("ID", "Status", "Contract", "Data of end Contract", "Mora")
    table_contract = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_contract.grid(row=1, column=1, sticky="nsew", columnspan=3)
    table_contract.heading("ID", text="ID", anchor=Win.W)
    table_contract.heading("Status", text="Status", anchor=Win.W)
    table_contract.heading("Contract", text="Contract", anchor=Win.W)
    table_contract.heading(
        "Data of end Contract", text="Data of end Contract", anchor=Win.W
    )
    table_contract.heading("Mora", text="Mora", anchor=Win.W)
    table_contract.column("#1", stretch=Win.NO, width=50)
    for produkt in contracts:
        table_contract.insert("", Win.END, values=produkt.get())
    scrollbar = Win.ttk.Scrollbar(
        frame, orient=Win.VERTICAL, command=table_contract.yview
    )
    table_contract.bind("<ButtonRelease-1>", on_select)


def do_contract(flag, window_contract):
    if flag == 1:
        contract_Table(window_contract)
    else:
        Logger(
            file_name,
            "Error in creating add_contract contractct",
            "Invalid flag in do_contract",
        )
