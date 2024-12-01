import Window as Win
from newKlient import do_new_klient
import Log
from Log import Logger

file_name = "File FirstDisplay"

# Переход к функциям открывающим возможность работы с данными 
def selected(event):
    Logger(file_name, "", "Method selected - making element to do work...")
    selection = combobox.get()
    if selection == "New Klients":
        method_New_Klient(selection)
        Logger(file_name, "", "Method selected - we tern it! we hawe element to do work with " + selection)
    else:
        Logger(file_name, "Error in add new element", "Method selected - selected item " + selection + " not found")

#--------------------------------------------------------------------------------------------------------------------------------
# Работа с новым клиентом

# Добавление элементов для перехода на элементы таблиц
def method_New_Klient(messeg):
    Logger("", "", "Method ethod_New_Klient - making element...")
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


# Открыть окно нового клиента
def start_new_klient(flag):
    Logger(file_name, "", "Method start_new_klient - open new window...")
    windows.append(Win.Window("New klient", "1000x300"))
    do_new_klient(flag, windows[len(windows) - 1], windows)

#--------------------------------------------------------------------------------------------------------------------------------


# Старт приложение
def start():
    Logger(file_name, "", "Method start - start main loop...")
    windows[0].open()


# Конец приложения
def end():
    Logger(file_name, "", "Method end - end main loop...")
    for window in windows:
        window.destroy()
    Logger(file_name, "", "Method end - close program...")

# Делаем основное окно приложения
Logger(file_name, "", "start program...")
windows = []
windows.append(Win.Window("PC for management", "600x400"))

Logger(file_name, "", "make frame...")
frame = Win.Frame(master=windows[0], relief=Win.SUNKEN)
frame.pack(expand=True)

Logger(file_name, "", "make box...")
method_lbl = Win.Label(frame, text="Select the table you will work with")
method_lbl.grid(row=1, column=1)

method = ["Pro Klients", "New Klients", "Kontrakts", "Produkts"]
combobox = Win.Combobox(frame, values=method, width=30, state="readonly")
combobox.grid(row=2, column=1, pady=10)
combobox.set("Nothing selected")
combobox.bind("<<ComboboxSelected>>", selected)

Logger(file_name, "", "make button to end")
button_to_end = Win.Button(
    frame,
    text="End all",
    command=end,
)
button_to_end.grid(row=5, column=1, pady=10)

start()
