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
    """
    Creates and manages the contract table window with options to add new contracts and close the table.

    This function sets up a frame with buttons for adding new contracts and closing the table, and initializes the contract data display by calling supporting functions.

    Args:
        window_contract (Window): The parent window for the contract table.

    Returns:
        None
    """

    def add_product_to_contract(product):
        """
        Adds a selected product to the contract's product list with inventory validation.

        This function checks product availability, ensures the requested quantity does not exceed current inventory, and appends the product ID to the contract's product list.

        Args:
            product (str): A string containing the product ID and details.

        Raises:
            ErrorContract: If the product is not available in sufficient quantity or fails validation.

        Returns:
            None
        """

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
        """
        Processes and saves a new contract with validation of client, dates, and associated products.

        This function creates a new contract by validating input parameters, setting up contract details, calculating mora, saving to the database, and updating related client and product information.

        Args:
            client (str): A string containing the client ID and details.
            end_data (str): The end date for the contract.

        Raises:
            ErrorContract: If date validation fails or no products are selected.

        Returns:
            None
        """

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
        """
        Creates a new window for adding a contract with input fields for client, products, end date, and status.

        This function manages the creation of a new contract entry window, setting up input fields and save/back buttons while preventing multiple simultaneous windows from being opened.

        Raises:
            ErrorContract: If more than one new contract window is already open.

        Returns:
            None
        """

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

    global frame
    frame = Win.Frame(master=window_contract, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_new_Contract = Win.Button(frame, text="Add Contract", command=add_new)
    add_new_Contract.grid(row=11, column=1, padx=10, pady=10)
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(4)),
    )
    close_table.grid(row=11, column=3, padx=10, pady=10)
    make_array()
    make_Table(window_contract)


def remake_cli_prod(contract):
    """
    Updates the products and clients associated with a given contract.

    This function recalculates the product quantities, updates the client's contract list,
    and renames the client and product records based on the contract's details.

    Parameters:
    contract (Contract): The contract object for which the products and clients need to be updated.

    Returns:
    None

    Side Effects:
    Modifies the product and client records in the 'produkts' and 'clients' lists.
    """
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
    """
    Retrieves and populates the contracts list with Contract objects from the database.

    This function connects to the SQLite database, executes a SELECT query to fetch all records from the Contracts table,
    and iterates through the fetched rows to create Contract objects. Each Contract object is then appended to the contracts list.

    Parameters:
    None

    Returns:
    None

    Raises:
    sqlite3.Error: If any error occurs during the database connection or query execution.
    """
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


def make_Table(window_contract):

    def id_for_delite(id):
        """
        Handles the deletion process for a specific contract after user confirmation.

        This function verifies the contract's existence, prompts the user for deletion confirmation, and removes the contract from the database and contract list if confirmed.

        Args:
            id (int): The unique identifier of the contract to be deleted.
            poup (Window): The parent popup window triggering the contract deletion.

        Returns:
            None
        """

        if Error.chek_ID(id, contracts):
            id = int(id)
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

    def end_contract(text_for_delite, poup):
        """
        Handles the process of ending a specific contract after user confirmation.

        This function verifies the contract's existence, checks its current status, prompts the user for confirmation, and updates the contract's status and end date if confirmed.

        Args:
            text_for_delite (str): The unique identifier of the contract to be ended.
            poup (Window): The parent popup window triggering the contract end action.

        Raises:
            ErrorContract: If the contract is already ended or an error occurs during the process.

        Returns:
            None
        """

        try:
            id = int(text_for_delite)
            if Error.chek_ID(id, contracts):
                for contract in contracts:
                    if contract.get_status() == 2:
                        messeage = "This already end"
                        raise Error.ErrorContract(messeage)
                    if contract.get_ID() == id:
                        confirm = Error.askyesno(
                            "Confirm Delete",
                            f"Are you sure you want to end the contract with ID: {id}?",
                            parent=windows[4][-1],
                        )
                        if confirm:
                            contract.set_status(2)
                            contract.set_data_end(Date)
                            contract.update_status()
                            frame.destroy()
                            contract_Table(window_contract)
                            poup.destroy()
                            windows[4].remove(poup)
                        break
        except Error.ErrorContract as e:
            Logger.log_error(file_name, "Error with end", str(e))

    def on_select(event):
        """
        Handles the selection of a contract in the contract table and opens an action popup window.

        This function captures the selected contract's ID, logs the selection, and creates a popup with options to end or delete the contract while preventing multiple simultaneous windows.

        Args:
            event (Event): The selection event triggered in the contract table.

        Raises:
            ErrorContract: If multiple windows are already open.

        Returns:
            None
        """

        cur_item = table_contract.item(table_contract.focus())
        col = table_contract.identify_column(event.x)
        if col == "#0":
            cell_value = cur_item["text"]
        else:
            if len(cur_item["values"]) != 0:
                cell_value = cur_item["values"][0]
                Logger.log_info(file_name, f"You tap on contract with ID: {cell_value}")
                try:
                    if len(windows[4]) >= 2:
                        message = "Please close other windows for work with new Client"
                        raise Error.ErrorContract(message)

                    def clo():
                        """
                        Closes multiple windows associated with the contract management interface.

                        This function removes and destroys the last two or three windows in the windows list, effectively cleaning up the contract-related window stack.

                        Returns:
                            None
                        """

                        if len(windows[4]) > 2:
                            w = windows[4][2]
                            windows[4].remove(windows[4][2])
                            w.destroy()
                        w = windows[4][1]
                        windows[4].remove(windows[4][1])
                        w.destroy()

                    popup = Win.Toplevel(windows[4][0])
                    windows[4].append(popup)
                    popup.title("Selecting actions")
                    popup.geometry("300x200")
                    popup.protocol("WM_DELETE_WINDOW", clo)
                    frame_popup = Win.Frame(master=popup, relief=Win.SUNKEN)
                    frame_popup.pack(expand=True)
                    add_new_Contract = Win.Button(
                        frame_popup,
                        text="End Contract",
                        command=lambda: end_contract(cell_value, popup),
                    )
                    add_new_Contract.grid(row=1, column=1, padx=10, pady=10)
                    Delete_element = Win.Button(
                        frame_popup,
                        text="Delete",
                        command=lambda: id_for_delite(cell_value),
                    )
                    Delete_element.grid(row=1, column=2, padx=10, pady=10)
                except Error.ErrorContract as e:
                    Error.Logger.log_error(
                        file_name, "Error with opend windows.", str(e)
                    )

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
    """
    Manages the contract table display or error logging based on a provided flag.

    This function determines whether to display the contract table or log an error depending on the input flag value.

    Args:
        flag (int): A control flag indicating the desired action. A value of 1 triggers table display.
        window_contract (Window): The parent window for the contract table.

    Returns:
        None

    Raises:
        Logger: Logs an error message if the flag is not 1.
    """

    if flag == 1:
        contract_Table(window_contract)
    else:
        Logger(
            file_name,
            "Error in creating add_contract contractct",
            "Invalid flag in do_contract",
        )
