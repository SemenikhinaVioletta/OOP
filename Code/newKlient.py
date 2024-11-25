import Window as Win
import sqlite3 as bd
import New_klient as New
import Error as Error
from Error import add_new_to_table


def new_Klient_Tabel(klients, window_new_klient):
    """
    The function `new_Klient_Start` sets up a new window for managing a PC.

    @param window_new_klient The parameter `window_new_klient` is likely a Tkinter `Tk` object, which represents the main
    window of a GUI application in Python. The function `new_Klient_Start` seems to be setting up a new window for a client
    management application by configuring its title, size, and creating
    """

    def add_new():
        print(
            "\tFile newKlient: Method new_Klient_Table: Funktion add_new - try to add new klient"
        )
        window_for_add = Win.Window()
        window_for_add.title("New klient")
        window_for_add.geometry("1000x300")
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
            command=lambda: Error.add_new_to_table(name_entry, phone_entry, email_entry),
        )
        save_button.grid(row=4, column=1, pady=5)
        delete_button = Win.Button(
            frame_for, text="Delete", command=window_for_add.destroy
        )
        delete_button.grid(row=4, column=2, pady=5, padx=5)
        window_for_add.mainloop()

        """new_klient = New.New_Klient()
        if new_klient.validate():
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Klient_new (Name, Phone, Mail) VALUES (?,?,?)", (new_klient.get()))
            conn.commit()
            messagebox.showinfo("Success", "Klient was added successfully!")
            new_klient.clear_fields()
        else:
            messagebox.showerror("Error", "Please, fill all required fields!")
        cursor.close()
        conn.close()
        """

    def make_Table():
        print("\tMaking Table...")
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
        print("\tTable created")

    print("File newKlient: Method new_Klient_Table - make a table")
    window_new_klient.title("New klient")
    window_new_klient.geometry("1000x300")
    frame = Win.Frame(master=window_new_klient, relief=Win.SUNKEN)
    frame.pack(expand=True)

    add_new_klient = Win.Button(frame, text="Add Klient", command=add_new)
    add_new_klient.grid(row=1, column=2, padx=10, pady=10)

    make_Table()

    window_new_klient.mainloop()


def do_new_klient(flag, window_new_klient):
    print("File newKlient: method do_new_klient - start working...")
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
        print("Error: Invalid flag in do_new_klient")
