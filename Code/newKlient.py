import Window as Win
import sqlite3 as bd
import Class_New_klient as New
import Error as Error
from Error import add_new_to_table
import Log
from Log import Logger

file_name = "File newKlient: "


def new_Klient_Tabel(klients, window_new_klient):

    def add_new():
        Logger(
            file_name
            + "Method new_Klient_Table: Funktion add_new - try to add new klient",
            "",
        )
        window_for_add = Win.Window("New klient", "1000x300")
        frame_for = Win.Frame(master=window_for_add, relief=Win.SUNKEN)
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
            command=lambda: Error.add_new_to_table(
                name_entry, phone_entry, email_entry
            ),
        )
        save_button.grid(row=4, column=1, pady=5)
        delete_button = Win.Button(
            frame_for, text="Back", command=window_for_add.destroy
        )
        delete_button.grid(row=4, column=2, pady=5, padx=5)
        window_for_add.open()


    def make_Table():
        Logger("" + "Making Table...", "")
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
        Logger("" + "Table created", "")

    Logger(file_name + "Method new_Klient_Table - make a table", "")
    frame = Win.Frame(master=window_new_klient, relief=Win.SUNKEN)
    frame.pack(expand=True)

    add_new_klient = Win.Button(frame, text="Add Klient", command=add_new)
    add_new_klient.grid(row=1, column=2, padx=10, pady=10)

    make_Table()

    open.mainloop()


def do_new_klient(flag, window_new_klient):
    Logger(file_name + "Method do_new_klient - start working...", "")
    klients = []

    conn = bd.connect("Code\DateBase\Pc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klient_new")
    rows = cursor.fetchall()

    for line in rows:
        klient = New.New_Klient(int(line[0]), str(line[1]), int(line[2]), str(line[3]))
        klients.append(klient)

    if flag == 1:
        new_Klient_Tabel(klients, window_new_klient)
    else:
        # MAKE LATEST VERSION
        Logger(
            file_name + "Invalid flag in do_new_klient", "Error in create new klient"
        )
