import c_Class_Pro_Klient as Pro
from a_Global_per import basadate, windows, make_combox
import c_Error as Error
import a_Window as Win
import sqlite3 as bd
from a_Log import Logger


file_name = "File proKlient"


def pro_Klient_Tabel(window_new_klient):
    """Creates a user interface for managing professional clients.

    This function sets up a window that allows users to add, rename, and delete professional clients. It includes input fields for client details and displays a table of existing clients.

    Args:
        window_new_klient (Window): The parent window for the client management interface.

    Returns:
        None
    """

    # Функция для добавления нового клиента
    def take_this(name_entry, phone_entry, email_entry, mora_entry, status_entry):
        """
        The function `take_this` adds a new entry to a table with provided information.

        @param name_entry The `name_entry` parameter seems to be a reference to an entry field where the user can input a name. This function appears to be taking various input fields related to a client (such as name, phone number, email, mora, and status) and creating a new client object with that
        @param phone_entry The `phone_entry` parameter in the `take_this` function seems to be a field where the user enters a phone number. It is being used to extract the phone number input from the user interface element and then convert it to an integer using `int(phone_entry.get())`. This integer value is
        @param email_entry The `email_entry` parameter in the `take_this` function seems to be a reference to an entry widget where the user can input their email address. This function appears to be part of a larger program that involves adding a professional client to a table or database. The `email_entry` parameter is
        @param mora_entry It seems like the `mora_entry` parameter is used to get input for the amount owed by a client. This value is being retrieved as a string and then converted to an integer later in the code. If the input is empty, it is set to "0" before conversion.
        @param status_entry The `status_entry` parameter in the `take_this` function appears to be an integer value representing the status of a client. It is used in the function to create a new `Pro_Klient` object with the provided information and then add it to a list of clients (`pro_klient`). The
        """
        if Error.add_pro_to_table(
            name_entry, phone_entry, email_entry, mora_entry, pro_klient, 0
        ):
            name = str(name_entry.get())
            mora = str(mora_entry.get())
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            status = int(status_entry)
            if len(mora) == 0:
                mora = "0"
            mora = int(mora)
            klient = Pro.Pro_Klient(
                pro_klient[-1].get_ID() + 1, name, mora, "", phone, email, status, None
            )

            klient.enter_klient_to_pro_bd()
            pro_klient.append(klient)
            make_Table()

    # Функция для изменения данных существующего клиента
    def do_this(klient, name_entry, phone_entry, email_entry, mora_entry, status_entry):
        """
        The function `do_this` updates a client's information in a table based on user input.

        @param klient It looks like the `do_this` function is taking several input parameters. Here is a breakdown of what each parameter represents:
        @param name_entry The `name_entry`, `phone_entry`, `email_entry`, `mora_entry`, `status_entry`, and `klient` parameters are likely input fields or values that are being passed to the `do_this` function.
        @param phone_entry The `phone_entry` parameter seems to be used to get the phone number input from the user interface. It is likely an entry widget or field where the user can enter their phone number. In the provided code snippet, the phone number is retrieved using `phone_entry.get()` and then converted to an
        @param email_entry The `email_entry` parameter in the `do_this` function seems to be a field where the user can input an email address. This email address is then retrieved as a string using `str(email_entry.get())` in the function.
        @param mora_entry It seems like the `mora_entry` parameter is used to get the value entered by the user for some kind of debt or outstanding amount. The value is then converted to a string using `str(mora_entry.get())`. This value is likely related to financial information or outstanding payments associated with the
        @param status_entry It seems like the `status_entry` parameter is used to update the status of a client in the `klient` object. The `status_entry` parameter is expected to be an integer value that represents the new status of the client.
        """
        if Error.add_pro_to_table(
            name_entry, phone_entry, email_entry, mora_entry, pro_klient, 1
        ):
            name = str(name_entry.get())
            mora = str(mora_entry.get())
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            status = int(status_entry)
            klient.rename_proklient(name, mora, phone, email, status, pro_klient)
            make_Table()

    # Функция для удаления клиента
    def id_for_delite(id):
        """Deletes a professional client based on the provided ID.

        This function checks if the given ID corresponds to an existing client. If found, it prompts the user for confirmation before deleting the client from the database and updating the client list.

        Args:
            id (Entry): The entry field containing the ID of the client to be deleted.

        Returns:
            None

        Raises:
            None
        """
        if Error.chek_id(id):
            id = int(id.get())
            for klient in pro_klient:
                if klient.get_ID() == id:
                    # Подтверждение удаления клиента
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the klient with ID: {id}, Name: {klient.get_name()}?",
                        parent=windows[1][-1],
                    )
                    if confirm:
                        klient.delete_klient_from_bd()
                        pro_klient.remove(klient)
                        make_Table()
                    break

    # Функция для создания окна удаления клиента
    def delete_element():
        """Creates a window for deleting a professional client.

        This function opens a new window that allows the user to enter the ID of a client they wish to delete. It includes input fields and a button to confirm the deletion, while ensuring that no more than one deletion window is open at a time.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorProKlient: If there are already two or more open windows.
        """
        try:
            if len(windows[2]) < 2:
                wind = Win.Window("Delete pro klient", "500x300")
                wind.make_protokol(lambda: wind.close_window(1))
                windows[1].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                Id_for_delite = Win.Label(
                    frame_for, text="Enter ID of the klient you want to delete:"
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
                raise Error.ErrorProKlient(
                    "Please close other windows for work with pro klient"
                )
        except Error.ErrorProKlient as e:
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    # Функция для добавления нового клиента
    def add_new():
        """Opens a window for adding a new professional client.

        This function creates a user interface that allows the user to input details for a new professional client, including name, phone number, email, debt amount, and status. It ensures that no more than one addition window is open at a time and provides options to save the new client or go back.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorProKlient: If there are already two or more open windows.
        """
        try:
            if len(windows[2]) < 2:
                wind = Win.Window("Add pro klient", "600x300")
                wind.make_protokol(lambda: wind.close_window(1))
                windows[1].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                name_text = Win.Label(
                    frame_for,
                    text='Enter name for pro klient in format:\n"Secondname Name Surname"',
                )
                name_entry = Win.Entry(frame_for)
                name_text.grid(row=1, column=1)
                name_entry.grid(row=1, column=2, padx=5)
                phone_text = Win.Label(
                    frame_for,
                    text='Enter phone number for pro klient in format:\n"88888888888"',
                )
                phone_entry = Win.Entry(frame_for)
                phone_text.grid(row=2, column=1, pady=5)
                phone_entry.grid(row=2, column=2, pady=5, padx=5)
                email_text = Win.Label(
                    frame_for,
                    text='Enter email for pro klient in format:\n"email@domain.com"',
                )
                email_entry = Win.Entry(frame_for)
                email_text.grid(row=3, column=1, pady=5)
                email_entry.grid(row=3, column=2, pady=5, padx=5)
                mora_text = Win.Label(
                    frame_for,
                    text='Enter mora for pro klient in format:\n"0"',
                )
                mora_entry = Win.Entry(frame_for)
                mora_text.grid(row=4, column=1, pady=5)
                mora_entry.grid(row=4, column=2, padx=5)

                status_text = Win.Label(
                    frame_for,
                    text="Enter status",
                )
                status_entry = make_combox("Nothing selected", 5, frame_for)
                status_text.grid(row=5, column=1, pady=5)

                save_button = Win.Button(
                    frame_for,
                    text="Save",
                    command=(
                        lambda: take_this(
                            name_entry,
                            phone_entry,
                            email_entry,
                            mora_entry,
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
                raise Error.ErrorProKlient(
                    "Please close other windows for work with pro klient"
                )
        except Error.ErrorProKlient as e:
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    # Функция для создания таблицы клиентов
    def make_Table():
        """Creates and displays a table of professional clients.

        This function initializes a treeview table to present client information, including ID, name, debt amount, phone number, email, and status. It populates the table with data from the list of professional clients and adds a vertical scrollbar for navigation.

        Args:
            None

        Returns:
            None
        """
        columns = ("ID", "Name", "Mora", "Phone", "Mail", "Status")
        table_new_klient = Win.ttk.Treeview(frame, columns=columns, show="headings")
        table_new_klient.grid(row=1, column=1, sticky="nsew", rowspan=10)
        table_new_klient.heading("ID", text="ID", anchor=Win.W)
        table_new_klient.heading("Name", text="Name", anchor=Win.W)
        table_new_klient.heading("Mora", text="Mora", anchor=Win.W)
        table_new_klient.heading("Phone", text="Phone", anchor=Win.W)
        table_new_klient.heading("Mail", text="Mail", anchor=Win.W)
        table_new_klient.heading("Status", text="Status", anchor=Win.W)
        table_new_klient.column("#1", stretch=Win.NO, width=50)
        for klient in pro_klient:
            table_new_klient.insert("", Win.END, values=klient.get())
        scrollbar = Win.ttk.Scrollbar(
            frame, orient=Win.VERTICAL, command=table_new_klient.yview
        )

    # Функция для получения текста для изменения клиента
    def get_text(id, frame_for):
        """Retrieves and displays client information for editing.

        This function checks if the provided ID corresponds to an existing client and, if found, populates the input fields with the client's current information for editing. It allows the user to update the client's name, phone number, email, debt amount, and status.

        Args:
            id (Entry): The entry field containing the ID of the client to be retrieved.
            frame_for (Frame): The frame in which the client information will be displayed.

        Returns:
            None

        Raises:
            Error.ErrorProKlient: If the client with the specified ID is not found.
        """
        if Error.chek_id(id):
            try:
                flag = 0
                id = int(id.get())
                for klient in pro_klient:
                    if klient.ID == id:
                        flag = 1
                        name_text = Win.Label(
                            frame_for,
                            text='Enter pro name for klient in format:\n"Secondname Name Surname"',
                        )
                        name_entry = Win.Entry(frame_for)
                        name_text.grid(row=2, column=1)
                        name_entry.insert(0, klient.get_name())
                        name_entry.grid(row=2, column=2, padx=5)
                        phone_text = Win.Label(
                            frame_for,
                            text='Enter pro phone number for klient in format:\n"88888888888"',
                        )
                        phone_entry = Win.Entry(frame_for)
                        phone_text.grid(row=3, column=1, pady=5)
                        phone_entry.insert(0, str(klient.get_phone()))
                        phone_entry.grid(row=3, column=2, pady=5, padx=5)
                        email_text = Win.Label(
                            frame_for,
                            text='Enter pro email for klient in format:\n"email@domain.com"',
                        )
                        email_entry = Win.Entry(frame_for)
                        email_text.grid(row=4, column=1, pady=5)
                        email_entry.insert(0, klient.get_email())
                        email_entry.grid(row=4, column=2, pady=5, padx=5)

                        mora_text = Win.Label(
                            frame_for,
                            text='Enter mora for pro klient in format:\n"0"',
                        )
                        mora_entry = Win.Entry(
                            frame_for,
                        )
                        mora_entry.insert(0, str(klient.get_mora()))
                        mora_text.grid(row=4, column=1, pady=5)
                        mora_entry.grid(row=4, column=2, padx=5)

                        status_text = Win.Label(
                            frame_for,
                            text="Enter status",
                        )
                        status_entry = make_combox(klient.get_status(), 5, frame_for)
                        status_text.grid(row=5, column=1, pady=5)

                        save_button = Win.Button(
                            frame_for,
                            text="Save",
                            command=(
                                lambda: do_this(
                                    klient,
                                    name_entry,
                                    phone_entry,
                                    email_entry,
                                    mora_entry,
                                    status_entry.get(),
                                )
                            ),
                        )
                        save_button.grid(row=6, column=1, pady=5)
                        break
                if flag == 0:
                    message = f"klient with ID = {id} not found!"
                    raise Error.ErrorProKlient(message)
            except Error.ErrorProKlient as e:
                Logger.log_error(file_name, str(e), "A Error into ID.")

    # Функция для переименования клиента
    def rename():
        """Opens a window for renaming a professional client.

        This function creates a user interface that allows the user to enter the ID of a client they wish to rename. It provides input fields to find the client and options to go back, ensuring that no more than one renaming window is open at a time.

        Args:
            None

        Returns:
            None

        Raises:
            Error.ErrorProKlient: If there are already two or more open windows.
        """
        try:
            if len(windows[2]) < 2:
                wind = Win.Window("Rename pro klient", "700x400")
                wind.make_protokol(lambda: wind.close_window(1))
                windows[1].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                ID_text = Win.Label(
                    frame_for, text="Enter ID of the klient you want to rename:"
                )
                ID_entry = Win.Entry(frame_for)
                ID_find = Win.Button(
                    frame_for,
                    text="Find element",
                    command=lambda: get_text(ID_entry, frame_for),
                )
                ID_find.grid(row=1, column=3, padx=5)
                ID_text.grid(row=1, column=1)
                ID_entry.grid(row=1, column=2, padx=5)
                delete_button = Win.Button(
                    frame_for, text="Back", command=lambda: wind.close_window(1)
                )
                delete_button.grid(row=6, column=2, pady=5, padx=5)
            else:
                raise Error.ErrorProKlient(
                    "Please close other windows for work with pro klient"
                )
        except Error.ErrorProKlient as e:
            Error.Logger.log_error(file_name, str(e), "Error with opend windows.")

    frame = Win.Frame(master=window_new_klient, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_new_klient = Win.Button(frame, text="Add klient", command=add_new)
    add_new_klient.grid(row=1, column=2, padx=10, pady=10)
    rename_klient = Win.Button(frame, text="Rename klient", command=rename)
    rename_klient.grid(row=2, column=2, padx=10, pady=10)
    Delete_element = Win.Button(frame, text="Delete", command=delete_element)
    Delete_element.grid(row=3, column=2, padx=10, pady=10)
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(1)),
    )
    close_table.grid(row=4, column=2, padx=10, pady=10)
    make_Table()


def make_array():
    """
    Connects to the database and retrieves all records from the 'Klient' table.
    Creates a list of Pro_Klient objects, each representing a client from the database.

    Parameters:
    None

    Returns:
    None

    Side Effects:
    Populates the global variable 'pro_klient' with Pro_Klient objects.
    Closes the database connection.
    """
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klient")
    rows = cursor.fetchall()
    for line in rows:
        klient = Pro.Pro_Klient(
            int(line[0]),
            str(line[1]),
            int(line[3]),
            str(line[4]),
            int(line[5]),
            str(line[6]),
            int(line[7]),
            None,
        )
        pro_klient.append(klient)
    cursor.close()


def do_pro_klient(flag, window_pro_klient):
    """
    Connects to the database, retrieves all records from the 'Klient' table, and creates a list of Pro_Klient objects.
    Depending on the flag value, it either opens a new window with a table of pro clients or logs an error.

    Parameters:
    flag (int): A flag indicating the action to be performed. If flag is 1, a new window with a table of pro clients is opened.
                 If flag is not 1, an error is logged.
    window_pro_klient (Window): The window in which the table of pro clients will be displayed.

    Returns:
    None
    """
    global pro_klient
    pro_klient = []
    make_array()
    if flag == 1:
        pro_Klient_Tabel(window_pro_klient)
    else:
        # Логирование ошибки
        Logger(
            file_name, "Error in creating pro klient", "Invalid flag in do_new_klient"
        )
