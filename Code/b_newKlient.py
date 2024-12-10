import a_Window as Win
import sqlite3 as bd
import b_Class_New_klient as New
import b_Error as Error
from b_Error import add_new_to_table, delete_from_table
from a_Log import Logger
from a_Global_per import windows, basadate, make_combox
from c_Error import chek_mora
import c_Class_Pro_Klient as Pro

file_name = "File newKlient"


def new_Klient_Tabel(window_new_klient):
    """
    The `new_Klient_Tabel` function in Python defines a set of sub-functions for adding, renaming, and deleting clients, as well as creating a GUI interface for managing client data in a table.

    @param window_new_klient `window_new_klient` is a parameter that represents the window or GUI element where the functions for adding, renaming, and deleting clients will be displayed and interacted with. It serves as the main window for managing client information and operations within the application.
    """

    # Функция для добавления нового клиента
    def take_this(name_entry, phone_entry, email_entry):
        """
        The function `take_this` adds a new entry to a table and creates a new client object based on the provided name, phone, and email entries.

        @param name_entry The `name_entry` parameter likely refers to an entry field where the user can input their name. This function seems to be taking the name, phone number, and email address entered by the user, adding them to a table, creating a new client object, and then entering that client into a database
        @param phone_entry The `phone_entry` parameter in the `take_this` function seems to be a variable that holds the phone number entered by the user. It is likely used as part of adding a new entry to a table or database. The function appears to check if adding a new entry to the table is successful
        @param email_entry The `email_entry` parameter in the `take_this` function is a variable that holds the email information entered by the user. It is used as one of the inputs to the `add_new_to_table` function and is also passed as a parameter to create a new `New_Klient` object
        """
        if add_new_to_table(name_entry, phone_entry, email_entry, klients):
            klient = New.New_Klient(
                klients[-1].get_ID() + 1,
                str(name_entry.get()),
                int(phone_entry.get()),
                str(email_entry.get()),
            )
            klient.enter_klient_to_bd()
            klients.clear()
            make_array()
            make_Table()

    # Функция для изменения данных существующего клиента
    def do_this(klient, name_entry, phone_entry, email_entry):
        """
        The function `do_this` adds a new entry to a table and renames a client if successful.

        @param klient It looks like the `do_this` function takes four parameters: `klient`, `name_entry`, `phone_entry`, and `email_entry`.
        @param name_entry The `name_entry` parameter seems to be a reference to an entry widget where the user can input a name. This input is then used to add a new entry to a table and also to rename a client in the `klient` object.
        @param phone_entry The `phone_entry` parameter in the `do_this` function seems to be a variable that holds the phone number entered by the user. It is likely a field or input where the user can input their phone number.
        @param email_entry The `email_entry` parameter in the `do_this` function seems to be a reference to an entry field where the user can input their email address. This parameter is likely used to retrieve the email address entered by the user and pass it to the `add_new_to_table` function for processing.
        """
        if add_new_to_table(name_entry, phone_entry, email_entry, klients):
            klient.rename_newklient(
                str(name_entry.get()),
                int(phone_entry.get()),
                str(email_entry.get()),
                klients,
            )
            klients.clear()
            make_array()
            make_Table()
    
    def make_this(klient, mora_entry, status_entry):
        """Creates a new professional client entry in the database.

        This function checks for the existence of a client based on their phone number and email address. 
        If the client does not already exist, it creates a new professional client and adds them to the database.

        Args:
            klient (Pro_Klient): The client instance containing personal information.
            mora_entry (Entry): The entry field for the client's debt amount.
            status_entry (int): The status of the client represented as an integer.

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If a client with the same phone number or email already exists.
            bd.Error: If an error occurs while interacting with the SQLite database.
        """
        basa = bd.connect(basadate)
        cur = basa.cursor()
        try:
            # Проверка существования клиента по телефону
            cur.execute(
                """SELECT EXISTS(SELECT 1 FROM Klient WHERE Phone = ?)""", (klient.get_phone(),)
            )
            info_phone = cur.fetchone()[0]  # Получаем результат запроса

            # Проверка существования клиента по электронной почте
            cur.execute(
                """SELECT EXISTS(SELECT 1 FROM Klient WHERE Mail = ?)""", (klient.get_email(),)
            )
            info_email = cur.fetchone()[0]  # Получаем результат запроса

            if info_email:
                raise Error.ErrorNewClient("There is already a client with this email")
            if info_phone:
                raise Error.ErrorNewClient("There is already a client with this phone")

            if chek_mora(mora_entry):
                mora_entry = str(mora_entry.get())
                if len(mora_entry) == 0:
                    mora_entry = "0"
                mora_entry = int(mora_entry)
                pro = Pro.Pro_Klient(0, "", mora_entry, "", 0, "", status_entry, klient)
                pro.enter_klient_to_pro_bd()
                id = Win.Entry()
                id.insert(0, str(klient.get_ID()))
                id_for_delite(id)
                make_Table()
        except Error.ErrorNewClient as e:
            Logger.log_error(file_name, str(e), "Error with already")
        except bd.Error as error:
            Logger(file_name, "Error while adding client to database", error)
        finally:
            cur.close()
            basa.close()

    # Функция для получения текста для изменения клиента
    def get_text(id, frame_for, wind):
        """
        The function `get_text` updates client information in a GUI window based on user input.

        @param id The `id` parameter in the `get_text` function seems to be used as an identifier for a client. It is likely used to search for a specific client in a list of clients (`klients`). The function then allows the user to update information (name, phone number, email) for
        @param frame_for `frame_for` is a tkinter frame where labels, entries, and buttons are being placed for user input and interaction in a graphical user interface (GUI) application.
        @param wind The `wind` parameter in the `get_text` function seems to be an instance of a window or GUI class that is used to create and manage the graphical user interface elements. It is likely used to display labels, entry fields, buttons, and handle user interactions within the window or frame specified by
        """
        if Error.delete_from_table(id, klients):
            try:
                flag = 0
                id = int(id.get())
                for klient in klients:
                    if klient.ID == id:
                        flag = 1
                        name_text = Win.Label(
                            frame_for,
                            text='Enter new name for client in format:\n"Secondname Name Surname"',
                        )
                        name_entry = Win.Entry(frame_for)
                        name_text.grid(row=2, column=1)
                        name_entry.insert(0, klient.get_name())
                        name_entry.grid(row=2, column=2, padx=5)
                        phone_text = Win.Label(
                            frame_for,
                            text='Enter new phone number for client in format:\n"88888888888"',
                        )
                        phone_entry = Win.Entry(frame_for)
                        phone_text.grid(row=3, column=1, pady=5)
                        phone_entry.insert(0, str(klient.get_phone()))
                        phone_entry.grid(row=3, column=2, pady=5, padx=5)
                        email_text = Win.Label(
                            frame_for,
                            text='Enter new email for client in format:\n"email@domain.com"',
                        )
                        email_entry = Win.Entry(frame_for)
                        email_text.grid(row=4, column=1, pady=5)
                        email_entry.insert(0, klient.get_email())
                        email_entry.grid(row=4, column=2, pady=5, padx=5)
                        save_button = Win.Button(
                            frame_for,
                            text="Save",
                            command=(
                                lambda: do_this(
                                    klient, name_entry, phone_entry, email_entry
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

    # Функция для удаления клиента
    def id_for_delite(id):
        """
        This function checks if a record with a specific ID exists in a table, prompts for confirmation before deleting it, and then removes the record from the table.

        @param id The `id` parameter in the `id_for_delite` function seems to represent the unique identifier of a client in a system. It is used to identify and delete a specific client from a table or database.
        @param window The `window` parameter in the `id_for_delite` function seems to represent a window object or a reference to the window that needs to be closed after the operation is completed. The `window.close_window(2)` method is likely used to close this window once the deletion process is finished.
        """
        if delete_from_table(id, klients):
            id = int(id.get())
            for klient in klients:
                if klient.get_ID() == id:
                    # Подтверждение удаления клиента
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the client with ID: {id}, Name: {klient.get_name()}?",
                        parent=windows[2][-1],
                    )
                    if confirm:
                        klient.delete_klient_from_bd()
                        klients.remove(klient)
                        make_Table()
                    break

    def id_for_pro(id, frame_for):
        """Retrieves and displays client information based on the provided ID.

        This function checks if a client exists in the database using the given ID. If found, it displays the client's name, phone number, and email address, and provides input fields for updating the client's debt and status.

        Args:
            id (Entry): The entry field containing the client's ID.
            frame_for (Frame): The frame in which the client information will be displayed.

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If the client with the specified ID is not found.
        """
        if Error.delete_from_table(id, klients):
            try:
                flag = 0
                id = int(id.get())
                for klient in klients:
                    if klient.ID == id:
                        flag = 1
                        name_text = Win.Label(
                            frame_for,
                            text="Name: " + klient.get_name(),
                        )
                        name_text.grid(row=2, column=1, pady=5, columnspan=2)
                        phone_text = Win.Label(
                            frame_for,
                            text="Phone: " + str(klient.get_phone()),
                        )
                        phone_text.grid(row=3, column=1, pady=5, columnspan=2)
                        email_text = Win.Label(
                            frame_for,
                            text="Email Address: " + klient.get_email(),
                        )
                        email_text.grid(row=4, column=1, pady=5, columnspan=2)

                        mora_entry = Win.Entry(frame_for)
                        mora_text = Win.Label(
                            frame_for,
                            text='Enter mora for pro klient in format:\n"0"',
                        )
                        mora_text.grid(row=5, column=1, pady=5)
                        mora_entry.grid(row=5, column=2, padx=5)

                        status_text = Win.Label(
                            frame_for,
                            text="Enter status",
                        )
                        status_entry = make_combox("Nothing selected", 6, frame_for)
                        status_text.grid(row=6, column=1, pady=5)
                        save_button = Win.Button(
                            frame_for,
                            text="Save",
                            command=lambda: make_this(
                                klient, mora_entry, status_entry.get()
                            ),
                        )
                        save_button.grid(row=7, column=1, pady=5)
                        break
                if flag == 0:
                    message = f"Client with ID = {id} not found!"
                    raise Error.ErrorNewClient(message)
            except Error.ErrorNewClient as e:
                Logger.log_error(file_name, str(e), "Error creating to pro")

    # Функция для создания окна удаления клиента
    def delete_element():
        """
        This Python function creates a window for deleting a client by entering their ID.
        """
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Delete New klient", "500x300")
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
                    "Please close other windows for work with new klient"
                )
        except Error.ErrorNewClient as e:
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    # Функция для добавления нового клиента
    def add_new():
        """
        The `add_new` function creates a window for adding a new client with fields for name, phone number, and email, along with save and back buttons.
        """
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Add New klient", "600x300")
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
                    frame_for, text='Enter email for new client in format:\n"email@domain.com"'
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
                    "Please close other windows for work with new klient"
                )
        except Error.ErrorNewClient as e:
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    # Функция для переименования клиента
    def rename():
        """
        The `rename` function creates a window for renaming a client and includes elements for entering the client"s ID and performing actions related to renaming.
        """
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Rename New klient", "600x300")
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
                    "Please close other windows for work with new klient"
                )
        except Error.ErrorNewClient as e:
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    def do_pro():
        """Opens a new window for creating a professional client.

        This function checks if there are fewer than two open windows. If so, it creates a new window where the user can enter the ID of a client to convert to a professional client, along with options to find the client or go back.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorNewClient: If there are already two or more open windows.
        """
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Make Pro klient", "600x500")
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
                    "Please close other windows for work with new klient"
                )
        except Error.ErrorNewClient as e:
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    # Функция для создания таблицы клиентов
    def make_Table():
        """
        The function `make_Table` creates a table with specified columns and headings, populating it with data from a list of clients and adding a vertical scrollbar.
        """
        columns = ("ID", "Name", "Phone", "Mail")
        table_new_klient = Win.ttk.Treeview(frame, columns=columns, show="headings")
        table_new_klient.grid(row=1, column=1, sticky="nsew", rowspan=10)
        table_new_klient.heading("ID", text="ID", anchor=Win.W)
        table_new_klient.heading("Name", text="Name", anchor=Win.W)
        table_new_klient.heading("Phone", text="Phone", anchor=Win.W)
        table_new_klient.heading("Mail", text="Mail", anchor=Win.W)
        table_new_klient.column("#1", stretch=Win.NO, width=50)
        for klient in klients:
            table_new_klient.insert("", Win.END, values=klient.get())
        scrollbar = Win.ttk.Scrollbar(
            frame, orient=Win.VERTICAL, command=table_new_klient.yview
        )

    frame = Win.Frame(master=window_new_klient, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_new_klient = Win.Button(frame, text="Add Client", command=add_new)
    add_new_klient.grid(row=1, column=2, padx=10, pady=10)
    rename_klient = Win.Button(frame, text="Rename Client", command=rename)
    rename_klient.grid(row=2, column=2, padx=10, pady=10)
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
    make_Table()


def make_array():
    """
    This function connects to the SQLite database and retrieves all records from the "Klient_new" table.
    It then creates a new "New_Klient" object for each record and appends it to the "klients" list.

    Parameters:
    None

    Returns:
    None
    """
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klient_new")
    rows = cursor.fetchall()
    for line in rows:
        klient = New.New_Klient(int(line[0]), str(line[1]), int(line[2]), str(line[3]))
        klients.append(klient)
    cursor.close()


def do_new_client(flag, window_new_klient):
    """
    This function manages the creation of a new client window based on the provided flag.
    If the flag is 1, it calls the "new_Klient_Tabel" function to create a new client window.
    If the flag is not 1, it logs an error message using the "Logger" function.

    Parameters:
    flag (int): A flag indicating the action to be performed. If flag is 1, a new client window is created.
                If flag is not 1, an error is logged.
    window_new_klient (Window): The window object for creating a new client.

    Returns:
    None
    """
    global klients
    klients = []
    make_array()
    if flag == 1:
        new_Klient_Tabel(window_new_klient)
    else:
        # Логирование ошибки
        Logger(
            file_name, "Error in creating new client", "Invalid flag in do_new_klient"
        )
