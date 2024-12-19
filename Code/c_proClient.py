import c_Class_Pro_Client as Pro
import c_Error as Error
import a_Window as Win
import sqlite3 as bd
from a_Log import Logger
from a_Global_Per import database, windows, create_combobox


pro_client = []


file_name = "File proClient"


def pro_client_Table(window_new_Client):

    def take_this(name_entry, phone_entry, email_entry, status_entry):
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

    def do_this(Client, name_entry, phone_entry, email_entry, status_entry):
        if Error.add_pro_to_table(
            name_entry,
            phone_entry,
            email_entry,
            pro_client,
            status_entry,
            1,
        ):
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
            pro_client_Table(window_new_Client)

    def id_for_delite(id):
        if Error.chek_id(id, pro_client):
            id = int(id.get())
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
                    break

    def delete_element():
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Delete pro Client", "500x300")
                wind.make_protokol(lambda: wind.close_window(1))
                windows[1].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                Id_for_delite = Win.Label(
                    frame_for, text="Enter ID of the Client you want to delete:"
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
                raise Error.ErrorProClient(
                    "Please close other windows for work with pro Client"
                )
        except Error.ErrorProClient as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    def add_new():
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

    def get_text(id, frame_for):
        if Error.chek_id(id, pro_client):
            try:
                flag = 0
                id = int(id.get())
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
                                )
                            ),
                        )
                        save_button.grid(row=6, column=1, pady=5)
                        break
                if flag == 0:
                    message = f"Client with ID = {id} not found!"
                    raise Error.ErrorProClient(message)
            except Error.ErrorProClient as e:
                Logger.log_error(file_name, "A Error into ID.", str(e))

    def rename():
        try:
            if len(windows[1]) < 2:
                wind = Win.Window("Rename pro Client", "700x400")
                wind.make_protokol(lambda: wind.close_window(1))
                windows[1].append(wind)
                frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
                frame_for.pack(expand=True)
                ID_text = Win.Label(
                    frame_for, text="Enter ID of the Client you want to rename:"
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
    """
        rename_Client = Win.Button(frame, text="Rename Client", command=rename)
        rename_Client.grid(row=2, column=2, padx=10, pady=10)
        Delete_element = Win.Button(frame, text="Delete", command=delete_element)
        Delete_element.grid(row=3, column=2, padx=10, pady=10)
    """
    close_table = Win.Button(
        frame,
        text="Close Table",
        command=(lambda: Win.end(1)),
    )
    close_table.grid(row=11, column=3, padx=10, pady=10)
    make_array()
    make_Table()


def make_array():
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


def make_Table():
    def on_select(event):
        cur_item = table_pro_Client.item(table_pro_Client.focus())
        col = table_pro_Client.identify_column(event.x)
        if col == "#0":
            cell_value = cur_item["text"]
        else:
            if len(cur_item["values"]) != 0:
                cell_value = cur_item["values"][0]
                Logger.log_info(file_name, f"You tap on pro client with ID: {cell_value}")

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
    make_array()
    if flag == 1:
        pro_client_Table(window_pro_client)
    else:
        Logger(
            file_name, "Error in creating pro Client", "Invalid flag in do_new_Client"
        )
