import c_Class_Pro_Client as Pro
from a_Global_Per import database, windows, create_combobox
import c_Error as Error
import a_Window as Win
import sqlite3 as bd
from a_Log import Logger


file_name = "File proClient"


def pro_client_Tabel(window_new_Client):
    def take_this(name_entry, phone_entry, email_entry, mora_entry, status_entry):
        if Error.add_pro_to_table(
            name_entry, phone_entry, email_entry, mora_entry, pro_client, status_entry, 0
        ):
            name = str(name_entry.get())
            mora = str(mora_entry.get())
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            status = int(status_entry)
            if len(mora) == 0:
                mora = "0"
            mora = int(mora)
            Client = Pro.Pro_Client(
                pro_client[-1].get_ID() + 1, name, mora, "", phone, email, status, None
            )

            Client.enter_client_to_db()
            pro_client.append(Client)
            make_Table()

    # Функция для изменения данных существующего клиента
    def do_this(Client, name_entry, phone_entry, email_entry, mora_entry, status_entry):
        if Error.add_pro_to_table(
            name_entry, phone_entry, email_entry, mora_entry, pro_client, status_entry, 1
        ):
            name = str(name_entry.get())
            mora = str(mora_entry.get())
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            status = int(status_entry)
            Client.rename_proClient(name, mora, phone, email, status, pro_client)
            make_Table()

    # Функция для удаления клиента
    def id_for_delite(id):
        if Error.chek_id(id, pro_client):
            id = int(id.get())
            for Client in pro_client:
                if Client.get_ID() == id:
                    # Подтверждение удаления клиента
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the Client with ID: {id}, Name: {Client.get_name()}?",
                        parent=windows[1][-1],
                    )
                    if confirm:
                        Client.delete_Client_from_bd()
                        pro_client.remove(Client)
                        make_Table()
                    break

    # Функция для создания окна удаления клиента
    def delete_element():
        try:
            if len(windows[2]) < 2:
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

    # Функция для добавления нового клиента
    def add_new():
        try:
            if len(windows[2]) < 2:
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
                mora_text = Win.Label(
                    frame_for,
                    text='Enter mora for pro Client in format:\n"0"',
                )
                mora_entry = Win.Entry(frame_for)
                mora_text.grid(row=4, column=1, pady=5)
                mora_entry.grid(row=4, column=2, padx=5)

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
                raise Error.ErrorProClient(
                    "Please close other windows for work with pro Client"
                )
        except Error.ErrorProClient as e:
            Logger.log_error(file_name, "Error with opend windows.", str(e))

    # Функция для создания таблицы клиентов
    def make_Table():
        columns = ("ID", "Name", "Mora", "Phone", "Mail", "Status")
        table_new_Client = Win.ttk.Treeview(frame, columns=columns, show="headings")
        table_new_Client.grid(row=1, column=1, sticky="nsew", rowspan=10)
        table_new_Client.heading("ID", text="ID", anchor=Win.W)
        table_new_Client.heading("Name", text="Name", anchor=Win.W)
        table_new_Client.heading("Mora", text="Mora", anchor=Win.W)
        table_new_Client.heading("Phone", text="Phone", anchor=Win.W)
        table_new_Client.heading("Mail", text="Mail", anchor=Win.W)
        table_new_Client.heading("Status", text="Status", anchor=Win.W)
        table_new_Client.column("#1", stretch=Win.NO, width=50)
        for Client in pro_client:
            table_new_Client.insert("", Win.END, values=Client.get())
        scrollbar = Win.ttk.Scrollbar(
            frame, orient=Win.VERTICAL, command=table_new_Client.yview
        )

    # Функция для получения текста для изменения клиента
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

                        mora_text = Win.Label(
                            frame_for,
                            text='Enter mora for pro Client in format:\n"0"',
                        )
                        mora_entry = Win.Entry(
                            frame_for,
                        )
                        mora_entry.insert(0, str(Client.get_mora()))
                        mora_text.grid(row=4, column=1, pady=5)
                        mora_entry.grid(row=4, column=2, padx=5)

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
                                    mora_entry,
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

    # Функция для переименования клиента
    def rename():
        try:
            if len(windows[2]) < 2:
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

    frame = Win.Frame(master=window_new_Client, relief=Win.SUNKEN)
    frame.pack(expand=True)
    add_new_Client = Win.Button(frame, text="Add Client", command=add_new)
    add_new_Client.grid(row=1, column=2, padx=10, pady=10)
    rename_Client = Win.Button(frame, text="Rename Client", command=rename)
    rename_Client.grid(row=2, column=2, padx=10, pady=10)
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


def do_pro_client(flag, window_pro_client):
    global pro_client
    pro_client = []
    make_array()
    if flag == 1:
        pro_client_Tabel(window_pro_client)
    else:
        Logger(
            file_name, "Error in creating pro Client", "Invalid flag in do_new_Client"
        )
