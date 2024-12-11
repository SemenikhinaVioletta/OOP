import a_Window as Win
import sqlite3 as bd
import b_Class_New_Client as New
import b_Error as Error
from b_Error import add_new_to_table, delete_from_table
from a_Log import Logger
from a_Global_Per import windows, database, create_combobox
from c_Error import chek_mora
import c_Class_Pro_Client as Pro

file_name = "File newClient"


def new_Client_Tabel(window_new_Client):
    """
    Creates a new client entry based on user-provided details and updates the database.

    This function adds the new client information to the table and creates a new client object
    with the specified name, phone number, and email. It then saves the client to the database
    and refreshes the client list and displayed table.

    Args:
        name_entry (Entry): The entry widget for the client's name.
        phone_entry (Entry): The entry widget for the client's phone number.
        email_entry (Entry): The entry widget for the client's email address.

    Returns:
        None
    """

    def take_this(name_entry, phone_entry, email_entry):
        if add_new_to_table(name_entry, phone_entry, email_entry, Clients):
            Client = New.New_Client(
                Clients[-1].get_ID() + 1,
                str(name_entry.get()),
                int(phone_entry.get()),
                str(email_entry.get()),
            )
            Client.enter_Client_to_bd()
            Clients.clear()
            frame.destroy()
            new_Client_Tabel(window_new_Client)

    def do_this(Client, name_entry, phone_entry, email_entry):
        """
        Updates a client's information with new details provided by the user.

        This function adds the new client details to the table and renames the existing client
        with the updated information. It refreshes the client list and updates the displayed table
        after the changes are made.

        Args:
            Client (Client): The client object to be updated.
            name_entry (Entry): The entry widget for the new client name.
            phone_entry (Entry): The entry widget for the new client phone number.
            email_entry (Entry): The entry widget for the new client email address.

        Returns:
            None
        """
        if add_new_to_table(name_entry, phone_entry, email_entry, Clients):
            Client.rename_newClient(
                str(name_entry.get()),
                int(phone_entry.get()),
                str(email_entry.get()),
                Clients,
            )
            Clients.clear()
            frame.destroy()
            new_Client_Tabel(window_new_Client)

    def make_this(Client, mora_entry, status_entry):
        """
        Processes the promotion of a client to a pro client and updates the database.

        This function checks for existing clients with the same phone number or email before
        promoting the specified client. If validation passes, it creates a new pro client entry
        in the database and updates the displayed client table.

        Args:
            Client (Client): The client object to be promoted.
            mora_entry (Entry): The entry widget for the mora value.
            status_entry (Combobox): The combobox for selecting the client's status.

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If a client with the same email or phone number already exists.
        """
        basa = bd.connect(database)
        cur = basa.cursor()
        try:
            cur.execute(
                """SELECT EXISTS(SELECT 1 FROM Client WHERE Phone = ?)""",
                (Client.get_phone(),),
            )
            info_phone = cur.fetchone()[0]
            cur.execute(
                """SELECT EXISTS(SELECT 1 FROM Client WHERE Mail = ?)""",
                (Client.get_email(),),
            )
            info_email = cur.fetchone()[0]
            if info_email:
                raise Error.ErrorNewClient("There is already a client with this email")
            if info_phone:
                raise Error.ErrorNewClient("There is already a client with this phone")
            if chek_mora(mora_entry):
                mora_entry = str(mora_entry.get())
                if len(mora_entry) == 0:
                    mora_entry = "0"
                mora_entry = int(mora_entry)
                pro = Pro.Pro_Client(0, "", mora_entry, "", 0, "", status_entry, Client)
                pro.enter_client_to_db()
                id = Win.Entry()
                id.insert(0, str(Client.get_ID()))
                id_for_delite(id)
                frame.destroy()
                new_Client_Tabel(window_new_Client)
        except Error.ErrorNewClient as e:
            Logger.log_error(file_name, "Error with already", str(e))
        except bd.Error as error:
            Logger(file_name, "Error while adding client to database", error)
        finally:
            cur.close()
            basa.close()

    def get_text(id, frame_for, wind):
        """
        Displays input fields for updating a client's information based on the provided ID.

        This function retrieves the client's current details and populates the input fields for
        the user to enter new values. It handles errors related to client ID validation and updates
        the client information upon confirmation.

        Args:
            id (Entry): The entry widget containing the client ID to be updated.
            frame_for (Frame): The frame where the input fields and buttons will be displayed.
            wind (Window): The window that contains the frame.

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If the client ID is not found.
        """
        try:
            if Error.delete_from_table(id, Clients):
                flag = 0
                id = int(id.get())
                for Client in Clients:
                    if Client.ID == id:
                        flag = 1
                        name_text = Win.Label(
                            frame_for,
                            text='Enter new name for client in format:\n"Secondname Name Surname"',
                        )
                        name_entry = Win.Entry(frame_for)
                        name_text.grid(row=2, column=1)
                        name_entry.insert(0, Client.get_name())
                        name_entry.grid(row=2, column=2, padx=5)
                        phone_text = Win.Label(
                            frame_for,
                            text='Enter new phone number for client in format:\n"88888888888"',
                        )
                        phone_entry = Win.Entry(frame_for)
                        phone_text.grid(row=3, column=1, pady=5)
                        phone_entry.insert(0, str(Client.get_phone()))
                        phone_entry.grid(row=3, column=2, pady=5, padx=5)
                        email_text = Win.Label(
                            frame_for,
                            text='Enter new email for client in format:\n"email@domain.com"',
                        )
                        email_entry = Win.Entry(frame_for)
                        email_text.grid(row=4, column=1, pady=5)
                        email_entry.insert(0, Client.get_email())
                        email_entry.grid(row=4, column=2, pady=5, padx=5)
                        save_button = Win.Button(
                            frame_for,
                            text="Save",
                            command=(
                                lambda: do_this(
                                    Client, name_entry, phone_entry, email_entry
                                )
                            ),
                        )
                        save_button.grid(row=5, column=1, pady=5)
                        break
                if flag == 0:
                    message = f"Client with ID = {id} not found!"
                    raise Error.ErrorNewClient(message)
        except Error.ErrorNewClient:
            wind.close_window(2)

    def id_for_delite(id):
        """
        Deletes a client from the database based on the provided ID.

        This function checks if the client ID exists in the Clients list and prompts the user for
        confirmation before deleting the client. If confirmed, it removes the client from the database
        and updates the displayed client table.

        Args:
            id (Entry): The entry widget containing the client ID to be deleted.

        Returns:
            None
        """
        if delete_from_table(id, Clients):
            id = int(id.get())
            for Client in Clients:
                if Client.get_ID() == id:
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the client with ID: {id}, Name: {Client.get_name()}?",
                        parent=windows[2][-1],
                    )
                    if confirm:
                        Client.delete_Client_from_bd()
                        Clients.remove(Client)
                        frame.destroy()
                        new_Client_Tabel(window_new_Client)
                    break

    def id_for_pro(id, frame_for):
        """
        Processes the ID of a client to promote them to a pro client.

        This function checks if the client ID exists in the Clients list and, if found, displays
        the client's details along with input fields for additional information required for promotion.
        It handles errors related to client ID validation and updates.

        Args:
            id (Entry): The entry widget containing the client ID to be processed.
            frame_for (Frame): The frame where the client details and input fields will be displayed.

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If the client ID is not found or if there is an error during processing.
        """
        if Error.delete_from_table(id, Clients):
            try:
                flag = 0
                id = int(id.get())
                for Client in Clients:
                    if Client.ID == id:
                        flag = 1
                        name_text = Win.Label(
                            frame_for,
                            text="Name: " + Client.get_name(),
                        )
                        name_text.grid(row=2, column=1, pady=5, columnspan=2)
                        phone_text = Win.Label(
                            frame_for,
                            text="Phone: " + str(Client.get_phone()),
                        )
                        phone_text.grid(row=3, column=1, pady=5, columnspan=2)
                        email_text = Win.Label(
                            frame_for,
                            text="Email Address: " + Client.get_email(),
                        )
                        email_text.grid(row=4, column=1, pady=5, columnspan=2)

                        mora_entry = Win.Entry(frame_for)
                        mora_text = Win.Label(
                            frame_for,
                            text='Enter mora for pro Client in format:\n"0"',
                        )
                        mora_text.grid(row=5, column=1, pady=5)
                        mora_entry.grid(row=5, column=2, padx=5)

                        status_text = Win.Label(
                            frame_for,
                            text="Enter status",
                        )
                        status_entry = create_combobox("Nothing selected", 6, frame_for)
                        status_text.grid(row=6, column=1, pady=5)
                        save_button = Win.Button(
                            frame_for,
                            text="Save",
                            command=lambda: make_this(
                                Client, mora_entry, status_entry.get()
                            ),
                        )
                        save_button.grid(row=7, column=1, pady=5)
                        break
                if flag == 0:
                    message = f"Client with ID = {id} not found!"
                    raise Error.ErrorNewClient(message)
            except Error.ErrorNewClient as e:
                Logger.log_error(file_name, "Error creating to pro", str(e))

    def delete_element():
        """
        Opens a new window for deleting a client.

        This function checks the number of open windows and, if appropriate, creates a new window
        for entering the ID of the client to be deleted. It provides input fields and buttons for
        user interaction, while managing errors related to window limits.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If there are too many open windows.
        """
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Delete New Client", "500x300")
                wind.make_protokol(lambda: wind.close_window(2))
                windows[2].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                Id_for_delite = Win.Label(
                    frame_for, text="Enter ID of the client you want to delete:"
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
                raise Error.ErrorNewClient(
                    "Please close other windows for work with new Client"
                )
        except Error.ErrorNewClient as e:
            Error.Logger.log_error(file_name, "Error with opend windows.", str(e))

    def add_new():
        """
        Opens a new window for adding a new client.

        This function checks the number of open windows and, if appropriate, creates a new window
        for entering the client's name, phone number, and email. It provides input fields and buttons
        for user interaction, while managing errors related to window limits.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If there are too many open windows.
        """
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Add New Client", "600x300")
                wind.make_protokol(lambda: wind.close_window(2))
                windows[2].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                name_text = Win.Label(
                    frame_for,
                    text='Enter name for new client in format:\n"Secondname Name Surname"',
                )
                name_entry = Win.Entry(frame_for)
                name_text.grid(row=1, column=1)
                name_entry.grid(row=1, column=2, padx=5)
                phone_text = Win.Label(
                    frame_for,
                    text='Enter phone number for new client in format:\n"88888888888"',
                )
                phone_entry = Win.Entry(frame_for)
                phone_text.grid(row=2, column=1, pady=5)
                phone_entry.grid(row=2, column=2, pady=5, padx=5)
                email_text = Win.Label(
                    frame_for,
                    text='Enter email for new client in format:\n"email@domain.com"',
                )
                email_entry = Win.Entry(frame_for)
                email_text.grid(row=3, column=1, pady=5)
                email_entry.grid(row=3, column=2, pady=5, padx=5)
                save_button = Win.Button(
                    frame_for,
                    text="Save",
                    command=(lambda: take_this(name_entry, phone_entry, email_entry)),
                )
                save_button.grid(row=4, column=1, pady=5)
                delete_button = Win.Button(
                    frame_for, text="Back", command=lambda: wind.close_window(2)
                )
                delete_button.grid(row=4, column=2, pady=5, padx=5)
            else:
                raise Error.ErrorNewClient(
                    "Please close other windows for work with new Client"
                )
        except Error.ErrorNewClient as e:
            Error.Logger.log_error(file_name, "Error with opend windows.", str(e))

    def rename():
        """
        Opens a new window for renaming a client.

        This function checks the number of open windows and, if appropriate, creates a new window
        for entering the ID of the client to be renamed. It provides input fields and buttons for
        user interaction, while managing errors related to window limits.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If there are too many open windows.
        """
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Rename New Client", "600x300")
                wind.make_protokol(lambda: wind.close_window(2))
                windows[2].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                ID_text = Win.Label(
                    frame_for, text="Enter ID of the client you want to rename:"
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
                    frame_for, text="Back", command=lambda: wind.close_window(2)
                )
                delete_button.grid(row=5, column=2, pady=5, padx=5)
            else:
                raise Error.ErrorNewClient(
                    "Please close other windows for work with new Client"
                )
        except Error.ErrorNewClient as e:
            Error.Logger.log_error(file_name, "Error with opend windows.", str(e))

    def do_pro():
        """
        Opens a new window for converting a client to a pro client.

        This function checks the number of open windows and, if appropriate, creates a new window
        for entering the ID of the client to be converted. It includes input fields and buttons for
        user interaction, and handles errors related to window management.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If there are too many open windows.
        """
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Make Pro Client", "600x500")
                wind.make_protokol(lambda: wind.close_window(2))
                windows[2].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                ID_text = Win.Label(
                    frame_for, text="Enter ID of the client you want to remake to pro:"
                )
                ID_entry = Win.Entry(frame_for)
                ID_find = Win.Button(
                    frame_for,
                    text="Find element",
                    command=lambda: id_for_pro(ID_entry, frame_for),
                )
                ID_find.grid(row=1, column=3, padx=5)
                ID_text.grid(row=1, column=1)
                ID_entry.grid(row=1, column=2, padx=5)
                delete_button = Win.Button(
                    frame_for, text="Back", command=lambda: wind.close_window(2)
                )
                delete_button.grid(row=7, column=2, pady=5, padx=5)
            else:
                raise Error.ErrorNewClient(
                    "Please close other windows for work with new Client"
                )
        except Error.ErrorNewClient as e:
            Error.Logger.log_error(file_name, "Error with opend windows.", str(e))

    global frame
    frame = Win.Frame(master=window_new_Client, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_new_Client = Win.Button(frame, text="Add Client", command=add_new)
    add_new_Client.grid(row=1, column=2, padx=10, pady=10)
    rename_Client = Win.Button(frame, text="Rename Client", command=rename)
    rename_Client.grid(row=2, column=2, padx=10, pady=10)
    to_Pro = Win.Button(frame, text="Make to Pro", command=do_pro)
    to_Pro.grid(row=3, column=2, padx=10, pady=10)
    Delete_element = Win.Button(frame, text="Delete", command=delete_element)
    Delete_element.grid(row=4, column=2, padx=10, pady=10)
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(2)),
    )
    close_table.grid(row=5, column=2, padx=10, pady=10)
    make_array()
    make_Table()


def make_array():
    """
    This function connects to the database, retrieves all records from the 'Client_new' table,
    and creates a new instance of the New_Client class for each record. The instances are then
    appended to the 'Clients' list.

    Parameters:
    None

    Returns:
    None
    """
    global Clients
    Clients = []
    conn = bd.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Client_new")
    rows = cursor.fetchall()
    for line in rows:
        Client = New.New_Client(int(line[0]), str(line[1]), int(line[2]), str(line[3]))
        Clients.append(Client)
    cursor.close()


def make_Table():
    """
    Creates and displays a table for new client information.

    This function initializes a Treeview widget to present client details such as ID, name, phone, and email.
    It populates the table with data from the Clients collection and adds a vertical scrollbar for navigation.

    Args:
        None

    Returns:
        None
    """
    columns = ("ID", "Name", "Phone", "Mail")
    table_new_Client = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_new_Client.grid(row=1, column=1, sticky="nsew", rowspan=10)
    table_new_Client.heading("ID", text="ID", anchor=Win.W)
    table_new_Client.heading("Name", text="Name", anchor=Win.W)
    table_new_Client.heading("Phone", text="Phone", anchor=Win.W)
    table_new_Client.heading("Mail", text="Mail", anchor=Win.W)
    table_new_Client.column("#1", stretch=Win.NO, width=50)
    for Client in Clients:
        table_new_Client.insert("", Win.END, values=Client.get())
    scrollbar = Win.ttk.Scrollbar(
        frame, orient=Win.VERTICAL, command=table_new_Client.yview
    )


def do_new_client(flag, window_new_Client):
    """
    This function creates a new client window and initializes the list of clients.

    Parameters:
    flag (int): A flag indicating whether to create a new client window. If flag is 1, create the window; otherwise, do not create the window.
    window_new_client (Window): The window object for creating a new client.

    Returns:
    None
    """
    if flag == 1:
        new_Client_Tabel(window_new_Client)
    else:
        Logger(
            file_name, "Error in creating new client", "Invalid flag in do_new_Client"
        )
