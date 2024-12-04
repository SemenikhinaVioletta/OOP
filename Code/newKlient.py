import Window as Win
import sqlite3 as bd
import Class_New_klient as New
import Error as Error
from Error import add_new_to_table
import Log
from Log import Logger

file_name = "File newKlient"


# -----------------------------------------------------------------------------------------------------------------------
# Работа со списком новых клиентов


def new_Klient_Tabel(klients, window_new_klient, windows):
    """
    This function creates a new client table and provides functionality to add new clients.

    Parameters:
    - klients (list): A list of New_Klient objects representing existing clients.
    - window_new_klient (Window): The main window for displaying the new client table.
    - windows (list): A list of all open windows.

    Returns:
    None
    """

    # Обновление и запись новых данных
    def take_this(name_entry, phone_entry, email_entry):
        Error.add_new_to_table(name_entry, phone_entry, email_entry, klients)
        make_Table()

    # Кнопка добавления нового клиента
    def add_new():
        """Creates a new client entry interface.

        This function initializes a graphical user interface for adding a new client,
        including fields for the client's name, phone number, and email. It also sets
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
        windows.append(Win.Window("New klient", "1000x300"))
        frame_for = Win.Frame(master=windows[len(windows) - 1], relief=Win.SUNKEN)
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
            command=lambda: take_this(name_entry, phone_entry, email_entry),
        )
        save_button.grid(row=4, column=1, pady=5)
        delete_button = Win.Button(
            frame_for,
            text="Back",
            command=lambda: windows[len(windows) - 1].close_window(windows),
        )
        delete_button.grid(row=4, column=2, pady=5, padx=5)

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
        table_new_klient.grid(row=1, column=1, sticky="nsew")
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

    add_new_klient = Win.Button(frame, text="Add Klient", command=add_new)
    add_new_klient.grid(row=1, column=2, padx=10, pady=10)
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=lambda: window_new_klient.close_window(windows),
    )
    close_table.grid(row=2, column=2, padx=10, pady=10)

    make_Table()


# ------------------------------------------------------------------------------------------------------------------------


# Начальный метод работы с новым клиентом
def do_new_klient(flag, window_new_klient, windows):
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
    Logger(file_name, "", "Method o_new_klient - making list of new klient...")
    klients = []
    conn = bd.connect("Code\DateBase\Pc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klient_new")
    rows = cursor.fetchall()

    # Загрузка клиентов из базы данных в список клиентов
    for line in rows:
        klient = New.New_Klient(int(line[0]), str(line[1]), int(line[2]), str(line[3]))
        klients.append(klient)

    # Выбор способа работы
    if flag == 1:
        Logger(file_name, "", "Make table...")
        new_Klient_Tabel(klients, window_new_klient, windows)
    else:
        # MAKE LATEST VERSION
        Logger(file_name, "Error in create new klient", "Invalid flag in do_new_klient")
