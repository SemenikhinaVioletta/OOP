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
    """
    Initializes the product management interface.

    This function creates a user interface for managing products, allowing users to add, rename,
    delete, and order products. It sets up the necessary buttons and their associated actions,
    as well as displaying the current product table.

    Args:
        window_produkt (Window): The parent window for the product management interface.

    Returns:
        None
    """

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
                int(number_entry.get()), 0
            )
            produkt.enter_produkt_to_bd()
            produkts.append(produkt)
            frame.destroy()
            produkt_Table(window_produkt)

    def make_this(produkt, get_order):
        """
        Processes an order for a product based on the user input.

        This function validates the order quantity and, if valid, updates the product's stock
        quantity accordingly. It refreshes the product list and updates the displayed product
        table to reflect the changes made.

        Args:
            produkt (Product): The product object for which the order is being processed.
            get_order (Entry): The entry widget containing the quantity of the product to order.

        Returns:
            None

        Raises:
            Error.ErrorProduct: If the order quantity is invalid.
        """
        try:
            if Error.check_order(get_order.get()):
                get_number = produkt.get_number() + int(get_order.get())
                produkt.order(get_number)
                frame.destroy()
                produkt_Table(window_produkt)
        except Error.ErrorProduct:
            pass

    def do_this(produkt, name_entry, mora_entry, number_entry):
        """
        Updates the details of a product based on user-provided input.

        This function validates the provided product information and, if valid, updates the product's
        details in the database. It then refreshes the product list and updates the displayed product
        table to reflect the changes made.

        Args:
            produkt (Product): The product object to be updated.
            name_entry (Entry): The entry widget for the product's name.
            mora_entry (Entry): The entry widget for the product's cost.
            number_entry (Entry): The entry widget for the product's quantity in stock.

        Returns:
            None

        Raises:
            Error: If the product details are invalid or cannot be updated.
        """
        if Error.check_all(
            name_entry.get(), mora_entry.get(), number_entry.get(), produkts
        ):
            produkt.rename_produkt(
                str(name_entry.get()),
                int(mora_entry.get()),
                int(number_entry.get()),
                produkts, 0
            )
            frame.destroy()
            produkt_Table(window_produkt)

    def get_text(id, frame_for, wind):
        """
        Retrieves and displays the details of a product based on the provided ID.

        This function validates the product ID and, if found, populates the input fields with the
        product's current details, allowing the user to update the information. It raises an error
        if the product ID is not found and handles the closing of the window in case of an error.

        Args:
            id (Entry): The entry widget containing the product ID to be retrieved.
            frame_for (Frame): The frame where the product details and input fields will be displayed.
            wind (Window): The window that contains the frame.

        Returns:
            None

        Raises:
            Error.ErrorProduct: If the product ID is not found in the list of products.
        """
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
        """
        Opens a new window for adding a product.

        This function checks the number of open windows and, if appropriate, creates a new window
        for entering the details of a new product, including name, cost, and quantity in stock.
        It provides input fields and buttons for user interaction, while managing errors related
        to window limits.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorProduct: If there are too many open windows.
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
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def id_for_delite(id):
        """
        Deletes a product based on the provided ID after user confirmation.

        This function checks if the product ID exists in the list of products and prompts the user
        for confirmation before deleting the product. If confirmed, it removes the product from the
        database and updates the displayed product table.

        Args:
            id (Entry): The entry widget containing the product ID to be deleted.

        Returns:
            None

        Raises:
            Error.ErrorProduct: If the product ID is not valid.
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
                        frame.destroy()
                        produkt_Table(window_produkt)
                    break

    def delete_element():
        """
        Opens a new window for deleting a product.

        This function checks the number of open windows and, if appropriate, creates a new window
        for entering the ID of the product to be deleted. It provides input fields and buttons for
        user interaction, while managing errors related to window limits.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorProduct: If there are too many open windows.
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
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def get_number(ID_entry, frame_for, wind):
        """
        Retrieves and displays the details of a product based on the provided ID.

        This function validates the product ID and, if found, displays the product's current
        stock number and allows the user to enter a new cost for the product. It raises an error
        if the product ID is not found and handles the closing of the window in case of an error.

        Args:
            ID_entry (Entry): The entry widget containing the product ID to be retrieved.
            frame_for (Frame): The frame where the product details and input fields will be displayed.
            wind (Window): The window that contains the frame.

        Returns:
            None

        Raises:
            Error.ErrorProduct: If the product ID is not found in the list of products.
        """
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
        """
        Opens a new window for renaming a product.

        This function checks the number of open windows and, if appropriate, creates a new window
        for entering the ID of the product to be renamed. It provides input fields and buttons for
        user interaction, while managing errors related to window limits.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorProduct: If there are too many open windows.
        """
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
        """
        Opens a new window for ordering a product.

        This function checks the number of open windows and, if appropriate, creates a new window
        for entering the ID of the product to be ordered. It provides input fields and buttons for
        user interaction, while managing errors related to window limits.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorProduct: If there are too many open windows.
        """
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
    make_array()
    make_Table()


def make_array():
    """
    This function retrieves all product data from the database and creates a list of Produkt objects.

    Parameters:
    None

    Returns:
    None

    Side Effects:
    - Populates the global list 'produkts' with Produkt objects.
    - Closes the database cursor.
    """
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
    """
    Creates and displays a table for product information.

    This function initializes a Treeview widget to present product details such as ID, name,
    cost per copy, and the number of copies in stock. It populates the table with data from
    the list of products and adds a vertical scrollbar for navigation.

    Args:
        None

    Returns:
    None
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


def do_product(flag, window_produkt):
    """
    This function manages the creation of a product management table within a given window.

    Parameters:
    flag (int): A flag indicating the action to be performed. If flag is 1, the function will create a product management table. If flag is not 1, an error will be logged.
    window_produkt (Window): The parent window in which the product management table will be created.

    Returns:
    None
    """
    if flag == 1:
        produkt_Table(window_produkt)
    else:
        # Логирование ошибки
        Logger(
            file_name,
            "Error in creating add_produkt product",
            "Invalid flag in do_produkt",
        )
