import Window as Win
import sqlite3 as bd
import Class_New_klient as New
import Error as Error
from Error import add_new_to_table, delete_from_table
import Log
from Log import Logger
from Global_per import windows, basadate, klients

file_name = "File newKlient"


# -----------------------------------------------------------------------------------------------------------------------
# Работа со списком новых клиентов
def new_Klient_Tabel(window_new_klient):
    """
    This function creates a new client table and provides functionality to add new clients.

    Parameters:
    - window_new_klient (Window): The main window for displaying the new client table.

    Returns:
    None
    """

    # ГОТОВО
    # Обновление и запись новых данных
    def take_this(name_entry, phone_entry, email_entry):
        """
        The function `take_this` adds a new entry to a table and then creates a new table.

        @param name_entry The `name_entry` parameter likely refers to the name of a client or individual being entered into a table or database.
        @param phone_entry The `phone_entry` parameter in the `take_this` function is likely intended to store the phone number information provided by the user. This parameter is expected to be passed to the `Error.add_new_to_table` function along with the `name_entry` and `email_entry` parameters. The purpose
        @param email_entry The `email_entry` parameter in the `take_this` function is used to store the email address of a client. This information is then passed to the `Error.add_new_to_table` function along with the `name_entry` (client"s name) and `phone_entry` (client"s phone
        """
        if add_new_to_table(name_entry, phone_entry, email_entry) == 0:
            klient = New.New_Klient(
                klients[-1].get_ID() + 1,
                str(name_entry.get()),
                int(phone_entry.get()),
                str(email_entry.get()),
            )
            klient.enter_klient_to_bd()
            klients.append(klient)
        klients.clear()
        make_array()
        make_Table()

    def do_this(klient, name_entry, phone_entry, email_entry):
        if add_new_to_table(name_entry, phone_entry, email_entry):
            klient.rename_newklient(
                str(name_entry.get()), int(phone_entry.get()), str(email_entry.get())
            )
            make_Table()

    # ГОТОВО
    # Удаление клиента по ID
    def id_for_delite(id, window):
        """
        The function `id_for_delite` attempts to delete a client from a list based on their ID.

        @param id The `id` parameter in the `id_for_delite` function seems to represent the identifier of a client or record that is being processed for deletion. It is used to identify the specific client within a list of clients (`klients`) and perform operations such as deleting the client from a database and
        @param window The `window` parameter in the `id_for_delite` function seems to be missing from the code snippet you provided. It is likely used as a reference to the window or GUI element where the deletion operation is taking place. Typically, in GUI applications, the `window` parameter would refer to
        """
        Logger(
            file_name,
            "",
            "Method new_Klient_Tabel - id_for_delite - try to delete from list of new klient...",
        )
        if delete_from_table(id) == 0:
            id = int(id.get())
            for klient in klients:
                if klient.get_ID() == id:
                    klient.delete_klient_from_bd()
                    klients.remove(klient)
                    make_Table()
        window.close_window()

    # ГОТОВО
    # Создание окна для удаления элемента таблици
    def delete_element():
        """
        This function creates a window with a form to enter an ID for deleting a client.
        """
        wind = Win.Window("Delete New klient", "1000x300")
        wind.make_protokol(wind.close_window)
        windows.append(wind)
        frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
        frame_for.pack(expand=True)
        Id_for_delite = Win.Label(
            frame_for,
            text="Enter id for new klient, witch you wont delete",
        )
        Id_for_delite.grid(row=1, column=1, padx=5, pady=5)
        text_for_delite = Win.Entry(
            frame_for,
        )
        text_for_delite.grid(row=1, column=2, padx=5)
        button_for_delite = Win.Button(
            frame_for,
            text="Delete",
            command=lambda: id_for_delite(text_for_delite, wind),
        )
        button_for_delite.grid(row=2, column=2, padx=5)
        Id_for_delite.grid(row=1, column=1, padx=5, pady=5)

    # ГОТОВО
    # Кнопка добавления нового клиента
    def add_new():
        """Creates a new client entry interface.

        This function initializes a graphical user interface for adding a new client,
        including fields for the client"s name, phone number, and email. It also sets
        up buttons for saving the new client information or closing the window.

        Args:
            None

        Returns:
            None
        """
        Logger(
            file_name,
            "",
            "Method new_Klient_Tabel - Method add_new - try to add a new klient...",
        )
        wind = Win.Window("Add New klient", "1000x300")
        wind.make_protokol(wind.close_window)
        windows.append(wind)
        frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
        frame_for.pack(expand=True)

        name_text = Win.Label(
            frame_for,
            text='Enter name for new klient, in formate:\n"Secondname Name Surname"',
        )
        name_entry = Win.Entry(
            frame_for,
        )
        name_text.grid(row=1, column=1)
        name_entry.grid(row=1, column=2, padx=5)
        phone_text = Win.Label(
            frame_for,
            text='Enter phone number for new klient, in formate:\n"88888888888"',
        )
        phone_entry = Win.Entry(
            frame_for,
        )
        phone_text.grid(row=2, column=1, pady=5)
        phone_entry.grid(row=2, column=2, pady=5, padx=5)
        email_text = Win.Label(
            frame_for,
            text='Enter email for new klient, in formate:\n"email@domain.com"',
        )
        email_entry = Win.Entry(
            frame_for,
        )
        email_text.grid(row=3, column=1, pady=5)
        email_entry.grid(row=3, column=2, pady=5, padx=5)

        save_button = Win.Button(
            frame_for,
            text="Save",
            command=(lambda: take_this(name_entry, phone_entry, email_entry)),
        )
        save_button.grid(row=4, column=1, pady=5)
        delete_button = Win.Button(
            frame_for,
            text="Back",
            command=lambda: wind.close_window(),
        )
        delete_button.grid(row=4, column=2, pady=5, padx=5)

    # ГОТОВО
    # Создание таблицы клиентов
    def make_Table():
        """Creates and displays a table of new clients.

        This function initializes a treeview widget to display client information,
        including their ID, name, phone number, and email. It also sets up the
        necessary columns and headings for the table.

        Args:
            None

        Returns:
            None
        """
        Logger(
            file_name,
            "",
            "Method new_Klient_Tabel - Method make_Table - making table of new klient...",
        )
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

    def get_text(id, frame_for, wind):
        if Error.delete_from_table(id) == 0:
            try:
                flag = 0
                id = int(id.get())
                for klient in klients:
                    if klient.ID == id:
                        flag = 1
                        name_text = Win.Label(
                            frame_for,
                            text='Enter new name for new klient, in formate:\n"Secondname Name Surname"',
                        )
                        name_entry = Win.Entry(
                            frame_for,
                        )
                        name_text.grid(row=2, column=1)
                        name_entry.insert(0, klient.get_name())
                        name_entry.grid(row=2, column=2, padx=5)

                        phone_text = Win.Label(
                            frame_for,
                            text='Enter new phone number for new klient, in formate:\n"88888888888"',
                        )
                        phone_entry = Win.Entry(
                            frame_for,
                        )
                        phone_text.grid(row=3, column=1, pady=5)
                        phone_entry.insert(0, str(klient.get_phone()))
                        phone_entry.grid(row=3, column=2, pady=5, padx=5)

                        email_text = Win.Label(
                            frame_for,
                            text='Enter new email for new klient, in formate:\n"email@domain.com"',
                        )
                        email_entry = Win.Entry(
                            frame_for,
                        )
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
                    message = f"Klient with ID = {id} not found!"
                    raise Error.ErrorNewKlient(message)
            except Error.ErrorNewKlient:
                wind.close_window()
                Logger(
                    file_name,
                    "Error renaname from Method new_Klient_Tabel - Method get_text",
                    str(Error.ErrorNewKlient(message)),
                )

    def rename():
        Logger(
            file_name,
            "",
            "Method new_Klient_Tabel - Method renam - try to rename a new klient...",
        )
        wind = Win.Window("Rename New klient", "1000x300")
        wind.make_protokol(wind.close_window)
        windows.append(wind)
        frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
        frame_for.pack(expand=True)

        ID_text = Win.Label(
            frame_for,
            text="Enter ID for new klient, witch You wont to rename",
        )
        ID_entry = Win.Entry(
            frame_for,
        )
        ID_find = Win.Button(
            frame_for,
            text="Find element",
            command=lambda: get_text(ID_entry, frame_for, wind),
        )
        ID_find.grid(row=1, column=3, padx=5)
        ID_text.grid(row=1, column=1)
        ID_entry.grid(row=1, column=2, padx=5)

        delete_button = Win.Button(
            frame_for,
            text="Back",
            command=lambda: wind.close_window(),
        )
        delete_button.grid(row=5, column=2, pady=5, padx=5)

    frame = Win.Frame(master=window_new_klient, relief=Win.SUNKEN)
    frame.pack(expand=True)

    add_new_klient = Win.Button(frame, text="Add Klient", command=add_new)
    add_new_klient.grid(row=1, column=2, padx=10, pady=10)

    rename_klient = Win.Button(frame, text="Rename Klient", command=rename)
    rename_klient.grid(row=2, column=2, padx=10, pady=10)

    Delete_element = Win.Button(
        frame,
        text="Delete",
        command=delete_element,
    )
    Delete_element.grid(row=3, column=2, padx=10, pady=10)

    close_table = Win.Button(
        frame,
        text="Close Table",
        command=lambda: window_new_klient.close_window(),
    )
    close_table.grid(row=4, column=2, padx=10, pady=10)

    make_Table()


# ------------------------------------------------------------------------------------------------------------------------


# Создание массива
def make_array():
    """
    This function retrieves new client data from the database and populates a list of New_Klient objects.

    Returns:
    None

    The function connects to the SQLite database specified by the "basadate" variable, executes a SQL query to select all records from the "Klient_new" table, and then iterates through the result set. For each record, it creates a new New_Klient object using the data from the record and appends it to the "klients" list. Finally, it closes the database connection.
    """
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klient_new")
    rows = cursor.fetchall()

    # Загрузка клиентов из базы данных в список клиентов
    for line in rows:
        klient = New.New_Klient(int(line[0]), str(line[1]), int(line[2]), str(line[3]))
        klients.append(klient)

    cursor.close()


# Начальный метод работы с новым клиентом
def do_new_klient(flag, window_new_klient):
    """
    This function manages the process of creating new clients. It retrieves existing clients from the database,
    and based on the provided flag, it either creates a new client table or performs another operation.

    Parameters:
    - flag (int): A flag indicating the desired operation. If flag is 1, a new client table is created.
                  Otherwise, an error is logged.
    - window_new_klient (Window): The main window for displaying the new client table.
    - windows (list): A list of all open windows.

    Returns:
    None
    """
    Logger(file_name, "", "Method do_new_klient - making list of new klient...")
    make_array()

    # Выбор способа работы
    if flag == 1:
        Logger(file_name, "", "Make table...")
        new_Klient_Tabel(window_new_klient)
    else:
        # MAKE LATEST VERSION
        Logger(file_name, "Error in create new klient", "Invalid flag in do_new_klient")
