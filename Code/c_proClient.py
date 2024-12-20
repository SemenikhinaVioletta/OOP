import c_Class_Pro_Client as Pro
import c_Error as Error
import a_Window as Win
import sqlite3 as bd
from a_Log import Logger
from a_Global_Per import database, windows, create_combobox


pro_client = []


file_name = "File proClient"


def pro_client_Table(window_new_Client):
    """
    Manages the creation and display of the professional client table in the given window.

    Parameters:
    window_new_Client (Window): The window object where the professional client table will be displayed.

    Returns:
    None
    """

    def take_this(name_entry, phone_entry, email_entry, status_entry):
        """
        Processes and adds a new professional client to the database with validation and UI update.

        Args:
        name_entry (Entry): Input field containing the client's name.
        phone_entry (Entry): Input field containing the client's phone number.
        email_entry (Entry): Input field containing the client's email address.
        status_entry (str): Input field containing the client's professional status.

        Returns:
        None
        """

        if Error.add_pro_to_table(
            name_entry,
            phone_entry,
            email_entry,
            pro_client,
            status_entry,
            0,
        ):
            name = str(name_entry.get())
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            status = int(status_entry)
            Client = Pro.Pro_Client(
                pro_client[-1].get_ID() + 1, name, 0, "", phone, email, status, None
            )

            Client.enter_client_to_db()
            pro_client.append(Client)
            frame.destroy()
            pro_client_Table(window_new_Client)

    def add_new():
        """
        Creates a new window for adding a professional client with input fields for name, phone, email, and status.

        This function manages the creation of a new professional client entry window, setting up input fields and save/back buttons while preventing multiple simultaneous windows from being opened.

        Raises:
        ErrorProClient: If more than one new professional client window is already open.

        Returns:
        None
        """

        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Add pro Client", "600x300")
                wind.make_protokol(lambda: wind.close_window(1))
                windows[1].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                name_text = Win.Label(
                    frame_for,
                    text='Enter name for pro Client in format:\n"Secondname Name Surname"',
                )
                name_entry = Win.Entry(frame_for)
                name_text.grid(row=1, column=1)
                name_entry.grid(row=1, column=2, padx=5)
                phone_text = Win.Label(
                    frame_for,
                    text='Enter phone number for pro Client in format:\n"88888888888"',
                )
                phone_entry = Win.Entry(frame_for)
                phone_text.grid(row=2, column=1, pady=5)
                phone_entry.grid(row=2, column=2, pady=5, padx=5)
                email_text = Win.Label(
                    frame_for,
                    text='Enter email for pro Client in format:\n"email@domain.com"',
                )
                email_entry = Win.Entry(frame_for)
                email_text.grid(row=3, column=1, pady=5)
                email_entry.grid(row=3, column=2, pady=5, padx=5)

                status_text = Win.Label(
                    frame_for,
                    text="Enter status",
                )
                status_entry = create_combobox("Nothing selected", 5, frame_for)
                status_text.grid(row=5, column=1, pady=5)

                save_button = Win.Button(
                    frame_for,
                    text="Save",
                    command=(
                        lambda: take_this(
                            name_entry,
                            phone_entry,
                            email_entry,
                            status_entry.get(),
                        )
                    ),
                )
                save_button.grid(row=6, column=1, pady=5)
                delete_button = Win.Button(
                    frame_for, text="Back", command=lambda: wind.close_window(1)
                )
                delete_button.grid(row=6, column=2, pady=5, padx=5)
            else:
                raise Error.ErrorProClient(
                    "Please close other windows for work with pro Client"
                )
        except Error.ErrorProClient as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    global frame
    frame = Win.Frame(master=window_new_Client, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_new_Client = Win.Button(frame, text="Add Client", command=add_new)
    add_new_Client.grid(row=11, column=1, padx=10, pady=10)
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(1)),
    )
    close_table.grid(row=11, column=3, padx=10, pady=10)
    make_array()
    make_Table(window_new_Client)


def make_array():
    """
    Retrieves and populates the pro_client list with Pro_Client objects from the database.

    This function connects to the SQLite database, executes a SELECT query to fetch all records from the 'Client' table,
    and iterates through the fetched rows to create Pro_Client objects. Each Pro_Client object is then appended to the
    pro_client list.

    Parameters:
    None

    Returns:
    None
    """
    pro_client.clear()
    conn = bd.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Client")
    rows = cursor.fetchall()
    for line in rows:
        Client = Pro.Pro_Client(
            int(line[0]),
            str(line[1]),
            int(line[3]),
            str(line[4]),
            int(line[5]),
            str(line[6]),
            int(line[7]),
            None,
        )
        pro_client.append(Client)
    cursor.close()


def make_Table(window_new_Client):
    """
    Creates and configures the professional client table with interactive features for client management.

    This function sets up a Treeview table displaying professional client information, enables row selection for performing actions like renaming or deleting clients, and provides a scrollbar for navigation.

    Args:
        window_new_Client (Window): The parent window for the professional client table.

    Returns:
        None
    """

    def do_this(Client, name_entry, phone_entry, email_entry, status_entry, poup):
        """
        Validates and processes a professional client's information update with user confirmation.

        This function checks the validity of new client details, prompts for user confirmation, and updates the professional client's information in the database if confirmed.

        Args:
            Client (ProClient): The professional client object to be updated.
            name_entry (Entry): Input field containing the new client name.
            phone_entry (Entry): Input field containing the new client phone number.
            email_entry (Entry): Input field containing the new client email.
            status_entry (str): The new professional status for the client.
            poup (Window): The popup window for client information update.

        Returns:
            None
        """

        if Error.add_pro_to_table(
            name_entry,
            phone_entry,
            email_entry,
            pro_client,
            status_entry,
            1,
        ):
            confirm = Error.askyesno(
                "Confirm Rename",
                f"Are you sure you want to reneme the client: Name: {Client.get_name()}, Mail: {str(Client.get_email())}, Phone: {str(Client.get_phone())}\n to Name: {str(name_entry.get())}, Mail: {str(email_entry.get())}, Phone: {str(phone_entry.get())}?",
                parent=windows[1][-1],
            )
            if confirm:
                name = str(name_entry.get())
                phone = int(phone_entry.get())
                email = str(email_entry.get())
                status = int(status_entry)
                Client.rename_client(
                    name,
                    phone,
                    Client.get_mora(),
                    email,
                    status,
                    Client.get_contract_id(),
                    pro_client,
                )
                frame.destroy()
                windows[1][-1].close_window(1)
                poup.destroy()
                windows[1].remove(poup)
                pro_client_Table(window_new_Client)

    def get_text(id, poup):
        """
        Initiates a professional client information update process by creating a window with pre-filled client details.

        This function prepares a rename window for a specific professional client, allowing modification of name, phone, email, and status while preventing multiple simultaneous windows from being opened.

        Args:
            id (int): The unique identifier of the professional client to be updated.
            poup (Window): The parent popup window triggering the client update.

        Raises:
            ErrorProClient: If multiple windows are open or the client is not found.

        Returns:
            None
        """

        try:
            if len(windows[1]) < 3:
                wind = Win.Window("Rename pro Client", "700x400")
                wind.make_protokol(lambda: wind.close_window(1))
                windows[1].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                if Error.chek_id(id, pro_client):
                    try:
                        flag = 0
                        id = int(id)
                        for Client in pro_client:
                            if Client.ID == id:
                                flag = 1
                                name_text = Win.Label(
                                    frame_for,
                                    text='Enter pro name for Client in format:\n"Secondname Name Surname"',
                                )
                                name_entry = Win.Entry(frame_for)
                                name_text.grid(row=2, column=1)
                                name_entry.insert(0, Client.get_name())
                                name_entry.grid(row=2, column=2, padx=5)
                                phone_text = Win.Label(
                                    frame_for,
                                    text='Enter pro phone number for Client in format:\n"88888888888"',
                                )
                                phone_entry = Win.Entry(frame_for)
                                phone_text.grid(row=3, column=1, pady=5)
                                phone_entry.insert(0, str(Client.get_phone()))
                                phone_entry.grid(row=3, column=2, pady=5, padx=5)
                                email_text = Win.Label(
                                    frame_for,
                                    text='Enter pro email for Client in format:\n"email@domain.com"',
                                )
                                email_entry = Win.Entry(frame_for)
                                email_text.grid(row=4, column=1, pady=5)
                                email_entry.insert(0, Client.get_email())
                                email_entry.grid(row=4, column=2, pady=5, padx=5)

                                status_text = Win.Label(
                                    frame_for,
                                    text="Enter status",
                                )
                                status_entry = create_combobox(
                                    Client.get_status(), 5, frame_for
                                )
                                status_text.grid(row=5, column=1, pady=5)

                                save_button = Win.Button(
                                    frame_for,
                                    text="Save",
                                    command=(
                                        lambda: do_this(
                                            Client,
                                            name_entry,
                                            phone_entry,
                                            email_entry,
                                            status_entry.get(),
                                            poup,
                                        )
                                    ),
                                )
                                delete_button = Win.Button(
                                    frame_for,
                                    text="Back",
                                    command=lambda: wind.close_window(1),
                                )
                                delete_button.grid(row=6, column=2, pady=5, padx=5)
                                save_button.grid(row=6, column=1, pady=5)
                                break
                        if flag == 0:
                            message = f"Client with ID = {id} not found!"
                            raise Error.ErrorProClient(message)
                    except Error.ErrorProClient as e:
                        Logger.log_error(file_name, "A Error into ID.", str(e))
            else:
                raise Error.ErrorProClient(
                    "Please close other windows for work with pro Client"
                )
        except Error.ErrorProClient as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def id_for_delite(id, poup):
        """
        Handles the deletion process for a specific professional client after user confirmation.

        This function verifies the client's existence, prompts the user for deletion confirmation, and removes the professional client from the database and client list if confirmed.

        Args:
            id (int): The unique identifier of the professional client to be deleted.
            poup (Window): The parent popup window triggering the client deletion.

        Returns:
            None
        """

        if Error.chek_id(id, pro_client):
            id = int(id)
            for Client in pro_client:
                if Client.get_ID() == id:
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the Client with ID: {id}, Name: {Client.get_name()}?",
                        parent=windows[1][-1],
                    )
                    if confirm:
                        Client.delete_client_from_db()
                        pro_client.remove(Client)
                        frame.destroy()
                        pro_client_Table(window_new_Client)
                        poup.destroy()
                        windows[1].remove(poup)
                    break

    def on_select(event):
        """
        Handles the selection of a professional client in the client table and opens an action popup window.

        This function captures the selected professional client's ID, logs the selection, and creates a popup with options to rename or delete the client while preventing multiple simultaneous windows.

        Args:
            event (Event): The selection event triggered in the professional client table.

        Raises:
            ErrorProClient: If multiple windows are already open.

        Returns:
            None
        """

        cur_item = table_pro_Client.item(table_pro_Client.focus())
        col = table_pro_Client.identify_column(event.x)
        if col == "#0":
            cell_value = cur_item["text"]
        else:
            if len(cur_item["values"]) != 0:
                cell_value = cur_item["values"][0]
                Logger.log_info(
                    file_name, f"You tap on pro client with ID: {cell_value}"
                )
                try:
                    if len(windows[1]) >= 2:
                        message = "Please close other windows for work with new Client"
                        raise Error.ErrorProClient(message)

                    def clo():
                        if len(windows[1]) > 2:
                            w = windows[1][2]
                            windows[1].remove(windows[1][2])
                            w.destroy()
                        w = windows[1][1]
                        windows[1].remove(windows[1][1])
                        w.destroy()

                    popup = Win.Toplevel(windows[1][0])
                    windows[1].append(popup)
                    popup.title("Selecting actions")
                    popup.geometry("300x200")
                    popup.protocol("WM_DELETE_WINDOW", clo)
                    frame_popup = Win.Frame(master=popup, relief=Win.SUNKEN)
                    frame_popup.pack(expand=True)
                    rename_Client = Win.Button(
                        frame_popup,
                        text="Rename Client",
                        command=lambda: get_text(cell_value, popup),
                    )
                    rename_Client.grid(row=1, column=1, padx=10, pady=10)
                    Delete_element = Win.Button(
                        frame_popup,
                        text="Delete",
                        command=lambda: id_for_delite(cell_value, popup),
                    )
                    Delete_element.grid(row=1, column=2, padx=10, pady=10)
                except Error.ErrorProClient as e:
                    Error.Logger.log_error(
                        file_name, "Error with opend windows.", str(e)
                    )

    columns = ("ID", "Name", "Mora", "Phone", "Mail", "Status")
    table_pro_Client = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_pro_Client.grid(row=1, column=1, sticky="nsew", columnspan=3)
    table_pro_Client.heading("ID", text="ID", anchor=Win.W)
    table_pro_Client.heading("Name", text="Name", anchor=Win.W)
    table_pro_Client.heading("Mora", text="Mora", anchor=Win.W)
    table_pro_Client.heading("Phone", text="Phone", anchor=Win.W)
    table_pro_Client.heading("Mail", text="Mail", anchor=Win.W)
    table_pro_Client.heading("Status", text="Status", anchor=Win.W)
    table_pro_Client.column("#1", stretch=Win.NO, width=50)
    for Client in pro_client:
        table_pro_Client.insert("", Win.END, values=Client.get())
    scrollbar = Win.ttk.Scrollbar(
        frame, orient=Win.VERTICAL, command=table_pro_Client.yview
    )
    table_pro_Client.bind("<ButtonRelease-1>", on_select)


def do_pro_client(flag, window_pro_client):
    """
    This function manages the creation and display of the pro client table.

    Parameters:
    flag (int): A flag indicating the action to be performed.
                 If flag is 1, the pro client table is created and displayed.
                 If flag is not 1, an error message is logged.
    window_pro_client (Window): The window object where the pro client table will be displayed.

    Returns:
    None
    """
    make_array()
    if flag == 1:
        pro_client_Table(window_pro_client)
    else:
        Logger(
            file_name, "Error in creating pro Client", "Invalid flag in do_new_Client"
        )
