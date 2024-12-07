import c_Class_Pro_Klient as Pro
import f_Class_status_klient as stat
from a_Global_per import basadate, windows, status_klient
from a_Log import Logger
import c_Error as Error
import a_Window as Win
import sqlite3 as bd


file_name = "File proKlient"


def pro_Klient_Tabel(window_new_klient):

    # Функция для добавления нового клиента
    def take_this(name_entry, phone_entry, email_entry, mora_entry, status_entry):
        if Error.add_pro_to_table(name_entry, phone_entry, email_entry, mora_entry, klients):
            name = str(name_entry.get())
            mora = str(mora_entry.get())
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            status = int(status_entry)
            if len(mora) == 0:
                mora = "0"
            mora = int(mora)
            klient = Pro.Pro_Klient(
                klients[-1].get_ID() + 1, name, mora, "", phone, email, status, None
            )

            klient.enter_klient_to_bd()
            klients.append(klient)
            make_Table()

    # Функция для изменения данных существующего клиента
    def do_this(klient, name_entry, phone_entry, email_entry, mora_entry, status_entry):
        if Error.add_pro_to_table(name_entry, phone_entry, email_entry, mora_entry, klients):
            name = str(name_entry.get())
            mora = str(mora_entry.get())
            phone = int(phone_entry.get())
            email = str(email_entry.get())
            status = int(status_entry)
            klient.rename_proklient(name, mora, "", phone, email, status)
            make_Table()

    # Функция для удаления клиента
    def id_for_delite(id):
        if Error.chek_id(id):
            id = int(id.get())
            for klient in klients:
                if klient.get_ID() == id:
                    # Подтверждение удаления клиента
                    confirm = Error.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete the klient with ID: {id}, Name: {klient.get_name()}?", parent = False
                    )
                    if confirm:
                        klient.delete_klient_from_bd()
                        klients.remove(klient)
                        make_Table()
                    break

    # Функция для создания окна удаления клиента
    def delete_element():
        wind = Win.Window("Delete pro klient", "500x300")
        wind.make_protokol(wind.close_window)
        windows.append(wind)
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

    # Функция для добавления нового клиента
    def add_new():
        wind = Win.Window("Add pro klient", "900x500")
        wind.make_protokol(wind.close_window)
        windows.append(wind)
        frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
        frame_for.pack(expand=True)
        name_text = Win.Label(
            frame_for,
            text="Enter name for pro klient in format:\n\"Secondname Name Surname\"",
        )
        name_entry = Win.Entry(frame_for)
        name_text.grid(row=1, column=1)
        name_entry.grid(row=1, column=2, padx=5)
        phone_text = Win.Label(
            frame_for,
            text="Enter phone number for pro klient in format:\n\"88888888888\"",
        )
        phone_entry = Win.Entry(frame_for)
        phone_text.grid(row=2, column=1, pady=5)
        phone_entry.grid(row=2, column=2, pady=5, padx=5)
        email_text = Win.Label(
            frame_for, text="Enter email for pro klient in format:\n\"email@domain.com\""
        )
        email_entry = Win.Entry(frame_for)
        email_text.grid(row=3, column=1, pady=5)
        email_entry.grid(row=3, column=2, pady=5, padx=5)
        mora_text = Win.Label(
            frame_for,
            text="Enter mora for pro klient in format:\n\"0\"",
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
                    name_entry, phone_entry, email_entry, mora_entry, status_entry.get()
                )
            ),
        )
        save_button.grid(row=6, column=1, pady=5)
        delete_button = Win.Button(
            frame_for, text="Back", command=lambda: wind.close_window()
        )
        delete_button.grid(row=6, column=2, pady=5, padx=5)

    # Функция для создания таблицы клиентов
    def make_Table():
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
        for klient in klients:
            table_new_klient.insert("", Win.END, values=klient.get())
        scrollbar = Win.ttk.Scrollbar(
            frame, orient=Win.VERTICAL, command=table_new_klient.yview
        )


    
            
    def make_combox(now, row_i, frame_for):
        method = []
        for i in status_klient:
            if i.get_status() != now:
                method.append(str(i.get_ID()))
        combobox = Win.Combobox(frame_for, values=method, width=30, state="readonly")
        combobox.grid(row=row_i, column=2, pady=5)
        combobox.set(now)
        return combobox
        

    # Функция для получения текста для изменения клиента
    def get_text(id, frame_for, wind):
        if Error.chek_id(id):
            try:
                flag = 0
                id = int(id.get())
                for klient in klients:
                    if klient.ID == id:
                        flag = 1
                        name_text = Win.Label(
                            frame_for,
                            text="Enter pro name for klient in format:\n\"Secondname Name Surname\"",
                        )
                        name_entry = Win.Entry(frame_for)
                        name_text.grid(row=2, column=1)
                        name_entry.insert(0, klient.get_name())
                        name_entry.grid(row=2, column=2, padx=5)
                        phone_text = Win.Label(
                            frame_for,
                            text="Enter pro phone number for klient in format:\n\"88888888888\"",
                        )
                        phone_entry = Win.Entry(frame_for)
                        phone_text.grid(row=3, column=1, pady=5)
                        phone_entry.insert(0, str(klient.get_phone()))
                        phone_entry.grid(row=3, column=2, pady=5, padx=5)
                        email_text = Win.Label(
                            frame_for,
                            text="Enter pro email for klient in format:\n\"email@domain.com\"",
                        )
                        email_entry = Win.Entry(frame_for)
                        email_text.grid(row=4, column=1, pady=5)
                        email_entry.insert(0, klient.get_email())
                        email_entry.grid(row=4, column=2, pady=5, padx=5)

                        mora_text = Win.Label(
                            frame_for,
                            text="Enter mora for pro klient in format:\n\"0\"",
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
                                    status_entry,
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
        wind = Win.Window("Rename pro klient", "900x500")
        wind.make_protokol(wind.close_window)
        windows.append(wind)
        frame_for = Win.Frame(master=wind, relief=Win.SUNKEN)
        frame_for.pack(expand=True)
        ID_text = Win.Label(
            frame_for, text="Enter ID of the klient you want to rename:"
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
            frame_for, text="Back", command=lambda: wind.close_window()
        )
        delete_button.grid(row=5, column=2, pady=5, padx=5)

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
        command=(lambda: window_new_klient.close_window()),
    )
    close_table.grid(row=4, column=2, padx=10, pady=10)
    make_Table()


def make_array():
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
        klients.append(klient)
    cursor.close()


def do_pro_klient(flag, window_pro_klient):
    global klients
    klients = []
    make_array()
    if flag == 1:
        pro_Klient_Tabel(window_pro_klient)
    else:
        # Логирование ошибки
        Logger(
            file_name, "Error in creating pro klient", "Invalid flag in do_new_klient"
        )
