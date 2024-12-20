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
    This function manages the display of a product table in a given window.
    It provides options to add new products, update existing products, and delete products.

    Parameters:
    window_produkt (Window): The window object where the product table will be displayed.

    Returns:
    None
    """
    def take_this(name_entry, coast_entry, number_entry):
        """
        Processes and adds a new product to the database with validation and UI update.

        Args:
        name_entry (Entry): Input field containing the product's name.
        coast_entry (Entry): Input field containing the product's cost.
        number_entry (Entry): Input field containing the product's quantity.

        Returns:
        None
        """

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

    def add_produkt():
        """
        Creates a new window for adding a product with input fields for name, cost, and quantity.

        Raises:
        ErrorProduct: If more than one new product window is already open.

        Returns:
        None
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

    global frame
    frame = Win.Frame(master=window_produkt, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_prod = Win.Button(frame, text="Add Produkt", command=add_produkt)
    add_prod.grid(row=11, column=1, padx=10, pady=10)
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(3)),
    )
    close_table.grid(row=11, column=3, padx=10, pady=10)
    make_array()
    make_Table(window_produkt)


def make_array():
    """
    Retrieves product data from the database and populates the product list.

    This function connects to the database, executes a SQL query to select all records from the 'Produkts' table,
    fetches the query results, and creates a 'Produkt' object for each record. The 'Produkt' objects are then appended
    to the 'produkts' list.

    Parameters:
    None

    Returns:
    None
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


def make_Table(window_produkt):
    """
    Creates and configures the product table with interactive features for product management.

    This function sets up a Treeview table displaying product information, enables row selection for performing actions like renaming, ordering, or deleting products, and provides a scrollbar for navigation.

    Args:
        window_produkt (Window): The parent window for the product table.

    Returns:
        None
    """

    def id_for_delite(id, poup):
        """
        Handles the deletion process for a specific product after user confirmation.

        This function verifies the product's existence, prompts the user for deletion confirmation, and removes the product from the database and product list if confirmed.

        Args:
            id (int): The unique identifier of the product to be deleted.
            poup (Window): The parent popup window triggering the product deletion.

        Returns:
            None
        """

        if Error.check_Id(id, produkts):
            id = int(id)
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
                        poup.destroy()
                        windows[3].remove(poup)
                        produkt_Table(window_produkt)
                    break

    def make_this(produkt, get_order, poup):
        """
        Processes a product order by validating the order quantity and updating the product's stock.

        This function checks the order quantity, calculates the new stock level, updates the product's order status in the database, and refreshes the product table.

        Args:
            produkt (Produkt): The product object being ordered.
            get_order (Entry): Input field containing the order quantity.
            poup (Window): The parent popup window triggering the product order.

        Raises:
            ErrorProduct: If the order quantity is invalid.

        Returns:
            None
        """

        try:
            if Error.check_order(get_order.get()):
                get_number = produkt.get_number() + int(get_order.get())
                produkt.order(get_number)
                frame.destroy()
                produkt_Table(window_produkt)
                windows[3][-1].close_window(3)
                poup.destroy()
                windows[3].remove(poup)
        except Error.ErrorProduct:
            pass

    def get_number(ID_entry, poup):
        """
        Initiates a product ordering process by creating a window with current product stock and order input.

        This function prepares an order window for a specific product, displaying current storage quantity and allowing the user to specify the order amount while preventing multiple simultaneous windows from being opened.

        Args:
            ID_entry (int): The unique identifier of the product to be ordered.
            poup (Window): The parent popup window triggering the product order.

        Raises:
            ErrorProduct: If multiple windows are open or the product is not found.

        Returns:
            None
        """

        try:
            if len(windows[3]) < 3:
                wind = Win.Window("Jrder produkt", "600x300")
                wind.make_protokol(lambda: wind.close_window(3))
                windows[3].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                try:
                    if Error.check_Id(ID_entry, produkts):
                        flag = 0
                        id = int(ID_entry)
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
                                delete_button = Win.Button(
                                    frame_for,
                                    text="Back",
                                    command=lambda: wind.close_window(3),
                                )
                                delete_button.grid(row=5, column=2, pady=5, padx=5)

                                save_button = Win.Button(
                                    frame_for,
                                    text="Order",
                                    command=(
                                        lambda: make_this(produkt, order_entry, poup)
                                    ),
                                )
                                save_button.grid(row=5, column=1, pady=5)
                                break
                        if flag == 0:
                            message = f"Client with ID = {id} not found!"
                            raise Error.ErrorProduct(message)
                except Error.ErrorProduct as e:
                    Logger.log_error(file_name, "Error in order", str(e))
            else:
                raise Error.ErrorProduct(
                    "Please close other windows for work with new produkt"
                )
        except Error.ErrorProduct as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def do_this(produkt, name_entry, mora_entry, number_entry, poup):
        """
        Validates and processes a product's information update with user confirmation.

        This function checks the validity of new product details, prompts for user confirmation, and updates the product's information in the database if confirmed.

        Args:
            produkt (Produkt): The product object to be updated.
            name_entry (Entry): Input field containing the new product name.
            mora_entry (Entry): Input field containing the new product cost.
            number_entry (Entry): Input field containing the new product quantity.
            poup (Window): The popup window for product information update.

        Returns:
            None
        """

        if Error.check_all(
            name_entry.get(), mora_entry.get(), number_entry.get(), produkts
        ):
            confirm = Error.askyesno(
                "Confirm Rename",
                f"Are you sure you want to reneme the client: Name: {produkt.get_name()}, Mail: {str(produkt.get_mora())}, Phone: {str(produkt.get_number())}\n to Name: {str(name_entry.get())}, Mail: {str(mora_entry.get())}, Phone: {str(number_entry.get())}?",
                parent=windows[3][-1],
            )
            if confirm:
                produkt.set_number(number_entry.get())
                produkt.rename_produkt(
                    str(name_entry.get()), int(mora_entry.get()), produkts
                )
                frame.destroy()
                windows[3][-1].close_window(3)
                poup.destroy()
                windows[3].remove(poup)
                produkt_Table(window_produkt)

    def get_text(id, poup):
        """
        Initiates a product information update process by creating a window with pre-filled product details.

        This function prepares a rename window for a specific product, allowing modification of name, cost, and quantity while preventing multiple simultaneous windows from being opened.

        Args:
            id (int): The unique identifier of the product to be updated.
            poup (Window): The parent popup window triggering the product update.

        Raises:
            ErrorProduct: If multiple windows are open or the product is not found.

        Returns:
            None
        """

        try:
            if len(windows[3]) < 3:
                wind = Win.Window("Rename New produkt", "600x300")
                wind.make_protokol(lambda: wind.close_window(3))
                windows[3].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                try:
                    if Error.check_Id(id, produkts):
                        flag = 0
                        id = int(id)
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
                                            produkt,
                                            name_entry,
                                            phone_entry,
                                            number_entry,
                                            poup,
                                        )
                                    ),
                                )
                                save_button.grid(row=5, column=1, pady=5)
                                delete_button = Win.Button(
                                    frame_for,
                                    text="Back",
                                    command=lambda: wind.close_window(3),
                                )
                                delete_button.grid(row=5, column=2, pady=5, padx=5)
                                break
                        if flag == 0:
                            message = f"Client with ID = {id} not found!"
                            raise Error.ErrorProduct(message)
                except Error.ErrorProduct:
                    wind.close_window(3)

            else:
                raise Error.ErrorProduct(
                    "Please close other windows for work with new produkt"
                )
        except Error.ErrorProduct as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def on_select(event):
        """
        Handles the selection of a product in the product table and opens an action popup window.

        This function captures the selected product's ID, logs the selection, and creates a popup with options to rename, order, or delete the product while preventing multiple simultaneous windows.

        Args:
            event (Event): The selection event triggered in the product table.

        Raises:
            ErrorProduct: If multiple windows are already open.

        Returns:
            None
        """

        cur_item = table_produkt.item(table_produkt.focus())
        col = table_produkt.identify_column(event.x)
        if col == "#0":
            cell_value = cur_item["text"]
        else:
            if len(cur_item["values"]) != 0:
                cell_value = cur_item["values"][0]
                Logger.log_info(file_name, f"You tap on product with ID: {cell_value}")

                try:
                    if len(windows[3]) >= 2:
                        message = "Please close other windows for work with new Client"
                        raise Error.ErrorProduct(message)

                    def clo():
                        """
                        Closes multiple windows associated with the product management interface.

                        This function removes and destroys the last two or three windows in the windows list, effectively cleaning up the product-related window stack.

                        Returns:
                            None
                        """

                        if len(windows[3]) > 2:
                            w = windows[3][2]
                            windows[3].remove(windows[3][2])
                            w.destroy()
                        w = windows[3][1]
                        windows[3].remove(windows[3][1])
                        w.destroy()

                    popup = Win.Toplevel(windows[3][0])
                    windows[3].append(popup)
                    popup.title("Selecting actions")
                    popup.geometry("300x200")
                    popup.protocol("WM_DELETE_WINDOW", clo)
                    frame_popup = Win.Frame(master=popup, relief=Win.SUNKEN)
                    frame_popup.pack(expand=True)
                    rename_produkt = Win.Button(
                        frame_popup,
                        text="Rename Produkt",
                        command=lambda: get_text(cell_value, popup),
                    )
                    rename_produkt.grid(row=1, column=1, padx=10, pady=10)
                    rename_produkt = Win.Button(
                        frame_popup,
                        text="Order",
                        command=lambda: get_number(cell_value, popup),
                    )
                    rename_produkt.grid(row=1, column=2, padx=10, pady=10)
                    Delete_element = Win.Button(
                        frame_popup,
                        text="Delete",
                        command=lambda: id_for_delite(cell_value, popup),
                    )
                    Delete_element.grid(row=1, column=3, padx=10, pady=10)
                except Error.ErrorProduct as e:
                    Error.Logger.log_error(
                        file_name, "Error with opend windows.", str(e)
                    )

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
    """
    This function is responsible for managing the product table.
    It checks the flag value and calls the appropriate function.

    Parameters:
    flag (int): A flag indicating the action to be performed.
                 If flag is 1, the product table is displayed.
                 If flag is not 1, an error message is logged.
    window_produkt (Window): The window object where the product table will be displayed.

    Returns:
    None
    """
    if flag == 1:
        produkt_Table(window_produkt)
    else:
        Logger(
            file_name,
            "Error in creating add_produkt product",
            "Invalid flag in do_produkt",
        )
