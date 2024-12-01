import Window as Win
from newKlient import do_new_klient
import Log
from Log import Logger

file_name = "File FirstDisplay: "


# Старт приложение
def start():
    windows[0].open()


# Конец приложения
def end():
    for window in windows:
        window.close()


# Добавление элементов для перехода на элементы таблиц
def method_New_Klient(messeg):
    new_window = Win.Button(
        frame,
        text="Open table",
        command=lambda: start_new_klient(1),
    )
    
    lable = Win.Label(frame, text="For " + messeg + "you can:")
    lable.grid(row=3, column=1, padx=10)
    new_window.grid(row=3, column=2, padx=10)

    new_otchet = Win.Button(
        frame,
        text="Make Otchet",
        command=lambda: start_new_klient(2),
    )
    new_otchet.grid(row=4, column=2, padx=10, pady=10)


# ПВызовереход к функциям определяющим след действия
def selected(event):
    selection = combobox.get()
    if selection == "New Klients":
        method_New_Klient(selection)
    else:
        Logger(file_name + "Method selected - selected item " + selection + " not found", "Error in add new element")


# Открыть окно пового клиента
def start_new_klient(flag):
    windows.append(Win.Window("New klient", "1000x300"))
    do_new_klient(flag, windows[len(windows) - 1])

# Делаем основное окно приложения
windows = []
windows.append(Win.Window("PC for management", "600x400"))
frame = Win.Frame(master=windows[0], relief=Win.SUNKEN)
frame.pack(expand=True)

method_lbl = Win.Label(frame, text="Select the table you will work with")
method_lbl.grid(row=1, column=1)

method = ["Pro Klients", "New Klients", "Kontrakts", "Produkts"]
combobox = Win.Combobox(frame, values=method, width=30, state="readonly")
combobox.grid(row=2, column=1, pady=10)
combobox.set("Nothing selected")
combobox.bind("<<ComboboxSelected>>", selected)

button_to_end = Win.Button(
    frame,
    text="End all",
    command=end,
)
button_to_end.grid(row=5, column=1, pady=10)

start()
