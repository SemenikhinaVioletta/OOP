import Window as Win
import newKlient
from newKlient import do_new_klient
import Log
from Log import Logger
from Global_per import windows

file_name = "File FirstDisplay"


# Переход к функциям открывающим возможность работы с данными
def selected(event):
    # Выбираем с чем работать
    selection = combobox.get()
    if selection == "New Klients":
        # Начало работы с новым клиентом
        method_New_Klient(selection)
    else:
        # Таких методов ещё нет, но в будущем они будут

# --------------------------------------------------------------------------------------------------------------------------------
# Работа с новым клиентом


# Добавление элементов для перехода на элементы таблиц
def method_New_Klient(messeg):
    # Создание кнопок для перехода к другим действиям
    lable = Win.Label(frame, text="For " + messeg + "you can:")
    lable.grid(row=3, column=1, padx=10)

    new_window = Win.Button(
        frame,
        text="Open table",
        command=lambda: start_new_klient(1),
    )
    new_window.grid(row=3, column=2, padx=10)

    new_otchet = Win.Button(
        frame,
        text="Make Otchet",
        command=lambda: start_new_klient(2),
    )
    new_otchet.grid(row=4, column=2, padx=10, pady=10)


# Открыть окно нового клиента
def start_new_klient(flag):
    # Открытие окна для начала работы с новым клиентом
    wind = Win.Window("New klient", "1000x300")
    wind.make_protokol(wind.close_window)
    windows.append(wind)
    # Переход к классам работы с новым клиентом
    do_new_klient(flag, wind)

# --------------------------------------------------------------------------------------------------------------------------------


# Старт приложение
def start():
    # Информация о начале работы программы
    window.open()

# Делаем основное окно приложения
Logger(file_name, "", "start program...")
window = Win.Window("PC for management", "600x400")
window.make_protokol(Win.end)
windows.append(window)

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
    command=Win.end,
)
button_to_end.grid(row=5, column=1, pady=10)

start()
