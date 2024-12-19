import a_Window as Win
import sqlite3 as bd
import b_Class_New_Client as New
import b_Error as Error
import c_Error as Error_pro
from c_Error import chek_status
from b_Error import add_new_to_table, delete_from_table
from a_Log import Logger
from a_Global_Per import windows, database, create_combobox
import c_Class_Pro_Client as Pro

file_name = "File newClient"


def new_Client_Tabel(window_new_Client):

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
        if (
            Error.chek_name(name_entry.get())
            and Error.chek_phone(phone_entry.get())
            and Error.chek_mail(email_entry.get())
        ):
            Client.rename_newClient(
                str(name_entry.get()),
                int(phone_entry.get()),
                str(email_entry.get()),
                Clients,
            )
            Clients.clear()
            frame.destroy()
            new_Client_Tabel(window_new_Client)

    def get_text(id, frame_for, wind):
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

    def delete_element():
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

    global frame
    frame = Win.Frame(master=window_new_Client, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_new_Client = Win.Button(frame, text="Add Client", command=add_new)
    add_new_Client.grid(row=11, column=1, padx=10, pady=10)
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(2)),
    )
    close_table.grid(row=11, column=3, padx=10, pady=10)
    make_array()
    make_Table(window_new_Client)


def make_array():
    """
    This function retrieves all records from the 'Client_new' table in the database,
    creates a New_Client object for each record, and appends it to the 'Clients' list.

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


def make_Table(window_new_Client):

    def id_for_delite(id):
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

    def make_this(Client, status_entry):
        try:
            basa = bd.connect(database)
            cur = basa.cursor()
            if chek_status(status_entry):
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
                    raise Error.ErrorNewClient(
                        "There is already a client with this email"
                    )
                if info_phone:
                    raise Error.ErrorNewClient(
                        "There is already a client with this phone"
                    )
                pro = Pro.Pro_Client(0, "", 0, "", 0, "", status_entry, Client)
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

    def id_for_pro(id, poup):
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Make Pro Client", "600x500")
                wind.make_protokol(lambda: wind.close_window(2))
                windows[2].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                flag = 0
                id = int(id)
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

                        status_text = Win.Label(
                            frame_for,
                            text="Enter status",
                        )
                        delete_button = Win.Button(
                            frame_for,
                            text="Back",
                            command=(poup.destroy, lambda: wind.close_window(2)),
                        )
                        delete_button.grid(row=7, column=2, pady=5, padx=5)
                        status_entry = create_combobox("Nothing selected", 6, frame_for)
                        status_text.grid(row=6, column=1, pady=5)
                        save_button = Win.Button(
                            frame_for,
                            text="Save",
                            command=lambda: make_this(Client, status_entry.get()),
                        )
                        save_button.grid(row=7, column=1, pady=5)
                        break
                if flag == 0:
                    message = f"Client with ID = {id} not found!"
                    raise Error.ErrorNewClient(message)
        except Error.ErrorNewClient as e:
            Logger.log_error(file_name, "Error creating to pro", str(e))

    def on_select(event):
        cur_item = table_new_Client.item(table_new_Client.focus())
        col = table_new_Client.identify_column(event.x)
        if col == "#0":
            cell_value = cur_item["text"]
        else:
            if len(cur_item["values"]) != 0:
                cell_value = cur_item["values"][0]
                Logger.log_info(
                    file_name, f"You tap on new client with ID: {cell_value}"
                )
                popup = Win.Toplevel(windows[2][0])
                popup.title("Selecting actions")
                popup.geometry("300x200")
                rename_Client = Win.Button(popup, text="Rename Client", command=rename)
                rename_Client.grid(row=1, column=1, padx=10, pady=10)
                to_Pro = Win.Button(
                    popup, text="Make to Pro", command=id_for_pro(cell_value, popup)
                )
                to_Pro.grid(row=3, column=2, padx=10, pady=10)
                Delete_element = Win.Button(
                    popup, text="Delete", command=delete_element
                )
                Delete_element.grid(row=1, column=3, padx=10, pady=10)

    columns = ("ID", "Name", "Phone", "Mail")
    table_new_Client = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_new_Client.grid(row=1, column=1, sticky="nsew", columnspan=3)
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
    table_new_Client.bind("<ButtonRelease-1>", on_select)


def do_new_client(flag, window_new_Client):
    if flag == 1:
        new_Client_Tabel(window_new_Client)
    else:
        Logger(
            file_name, "Error in creating new client", "Invalid flag in do_new_Client"
        )
