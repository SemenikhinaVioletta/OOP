import a_Window as Win
import sqlite3 as bd
import d_Class_Produkt as prod
import d_Error as Error
from a_Log import Logger
from a_Global_per import basadate, windows

file_name = "File Produkt"
logger = Logger(file_name, [], "Application started")


def produkt_Table(window_produkt):

    # Функция для добавления нового клиента
    def take_this(name_entry, coast_entry, number_entry):
        """
        Creates a product management table within a given window.

        This function initializes a user interface for managing products, allowing users to add, rename, delete, and view product details. It provides various functionalities through nested functions to handle product operations and updates the displayed table accordingly.

        Args:
            window_produkt (Window): The parent window in which the product management table will be created.

        Examples:
            produkt_Table(main_window)
        """
        if Error.check_all(
            name_entry.get(), coast_entry.get(), number_entry.get(), produkts
        ):
            produkt = prod.Produkt(
                produkts[-1].get_ID() + 1,
                str(name_entry.get()),
                int(coast_entry.get()),
                int(number_entry.get()),
            )
            produkt.enter_produkt_to_bd()
            produkts.append(produkt)
            make_Table()

    def make_this(produkt, get_order):
        try:
            if Error.check_order(get_order.get()):
                get_number = produkt.get_number() + int(get_order.get())
                produkt.order(get_number)
                produkts.clear()
                make_array()
                make_Table()
        except Error.ErrorProduct:
            pass

    # Функция для изменения данных существующего клиента
    def do_this(produkt, name_entry, mora_entry, number_entry):
        """
        Updates the details of an existing product based on user input.

        This function renames a product and updates its associated information, such as cost and quantity, using the provided entries. It ensures that all necessary checks are performed before making the updates and refreshes the product list and table display afterward.

        Args:
            produkt (Produkt): The product instance to be updated.
            name_entry (Entry): The entry field for the new name of the product.
            mora_entry (Entry): The entry field for the new cost of the product.
            number_entry (Entry): The entry field for the new quantity of the product.

        Returns:
            None

        Raises:
            Error: If any validation checks fail.

        Examples:
            do_this(existing_product, name_entry, cost_entry, quantity_entry)
        """
        if Error.check_all(
            name_entry.get(), mora_entry.get(), number_entry.get(), produkts
        ):
            produkt.rename_Produkts(
                str(name_entry.get()),
                int(mora_entry.get()),
                int(number_entry.get()),
                produkts,
            )
            produkts.clear()
            make_array()
            make_Table()

    # Функция для получения текста для изменения клиента
    def get_text(id, frame_for, wind):
        """
        Retrieves and displays the current details of a product for editing.

        This function checks if a product with the specified ID exists and, if found, populates the input fields with the product's current details for the user to edit. It also sets up a save button to apply the changes once the user has made their edits.

        Args:
            id (Entry): The entry field containing the ID of the product to be edited.
            frame_for (Frame): The frame in which the input fields and buttons are displayed.
            wind (Window): The window that contains the frame and is used for closing the editing interface.

        Returns:
            None

        Raises:
            Error.ErrorProduct: If the product with the specified ID is not found.

        Examples:
            get_text(id_entry, frame, window)
        """
        if Error.check_Id(id.get(), produkts):
            try:
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
                        phone_entry.insert(0, str(produkt.get_phone()))
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

    # Функция для добавления нового клиента
    def add_produkt():
        """
        Opens a window for adding a new product to the inventory.

        This function creates a user interface that allows users to input the name, cost, and quantity of a new product. It includes validation to ensure that no more than one add product window is open at a time and handles any errors that may arise during this process.

        Returns:
            None

        Raises:
            Error.ErrorProduct: If there are already too many open windows for adding products.

        Examples:
            add_produkt()
        """
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
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    # Функция для удаления клиента
    def id_for_delite(id):
        """
        Deletes a product from the inventory based on the provided ID.

        This function checks if a product with the specified ID exists and prompts the user for confirmation before deleting it. If confirmed, the product is removed from the database and the displayed product table is updated accordingly.

        Args:
            id (Entry): The entry field containing the ID of the product to be deleted.

        Returns:
            None

        Raises:
            Error: If the specified ID does not correspond to any existing product.

        Examples:
            id_for_delite(id_entry)
        """
        if Error.check_Id(id.get(), produkts):
            id = int(id.get())
            for produkt in produkts:
                if produkt.get_ID() == id:
                    # Подтверждение удаления клиента
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the product with ID: {id}, Name: {produkt.get_name()}?",
                        parent=windows[3][-1],
                    )
                    if confirm:
                        produkt.delete_produkt_from_bd()
                        produkts.remove(produkt)
                        make_Table()
                    break

    # Функция для создания окна удаления клиента
    def delete_element():
        """
        Opens a window for deleting a product from the inventory.

        This function provides a user interface that allows users to enter the ID of a product they wish to delete. It ensures that only one delete window is open at a time and handles any errors related to window management.

        Returns:
            None

        Raises:
            Error.ErrorProduct: If there are already too many open windows for deleting products.

        Examples:
            delete_element()
        """
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
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    def get_number(ID_entry, frame_for, wind):
        if Error.check_Id(ID_entry.get(), produkts):
            try:
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
                            text="Enter new cost of produkt",
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

    # Функция для переименования клиента
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
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

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
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    # Функция для создания таблицы клиентов
    def make_Table():
        """
        Creates and displays a table of products in the user interface.

        This function initializes a tree view table that presents product details, including ID, name, cost, and quantity in stock. It populates the table with data from the product list and adds a scrollbar for navigation.

        Returns:
            None

        Examples:
            make_Table()
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
    add_prod = Win.Button(frame, text="Add Produkt", command=add_produkt)
    add_prod.grid(row=1, column=2, padx=10, pady=10)
    rename_produkt = Win.Button(frame, text="Rename Produkt", command=rename)
    rename_produkt.grid(row=2, column=2, padx=10, pady=10)
    rename_produkt = Win.Button(frame, text="Order", command=order)
    rename_produkt.grid(row=3, column=2, padx=10, pady=10)
    Delete_element = Win.Button(frame, text="Delete", command=delete_element)
    Delete_element.grid(row=4, column=2, padx=10, pady=10)
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(3)),
    )
    close_table.grid(row=5, column=2, padx=10, pady=10)
    make_Table()


def make_array():
    """
    Fetches product data from the database and creates instances of the Produkt class.

    This function establishes a connection to the SQLite database, executes a SQL query to select all records from the 'Produkts' table, and iterates through the fetched rows. For each row, it creates a new instance of the Produkt class using the data from the row and appends it to the 'produkts' list. Finally, it closes the database cursor.

    Parameters:
    None

    Returns:
    None
    """
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produkts")
    rows = cursor.fetchall()
    for line in rows:
        produkt = prod.Produkt(int(line[0]), str(line[1]), int(line[2]), int(line[3]))
        produkts.append(produkt)
    cursor.close()


def do_product(flag, window_produkt):
    """
    This function initializes the product management interface based on the provided flag.

    Parameters:
    flag (int): A flag indicating the desired action. If flag is 1, the function will create a product table in the provided window. If flag is not 1, an error will be logged.
    window_produkt (Window): The window in which the product management interface will be displayed.

    Returns:
    None
    """
    global produkts
    produkts = []
    make_array()
    if flag == 1:
        produkt_Table(window_produkt)
    else:
        # Логирование ошибки
        Logger(
            file_name,
            "Error in creating add_produkt product",
            "Invalid flag in do_produkt",
        )
