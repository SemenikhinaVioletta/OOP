import Window as Win
import newKlient
from newKlient import do_new_klient
import Log
from Log import Logger
from Global_per import windows

file_name = "File FirstDisplay"


# Переход к функциям открывающим возможность работы с данными
def selected(event):
    """
    This function handles the event when a selection is made in the Combobox.
    It logs the selection and calls the appropriate function based on the selection.

    Parameters:
    event (tkinter.Event): The event object that triggered this function.

    Returns:
    None
    """
    Logger(file_name, "", "Method selected - making element to do work...")
    selection = combobox.get()
    if selection == "New Klients":
        method_New_Klient(selection)
        Logger(
            file_name,
            "",
            "Method selected - we tern it! we hawe element to do work with "
            + selection,
        )
    else:
        Logger(
            file_name,
            "Error in add new element",
            "Method selected - selected item " + selection + " not found",
        )


# --------------------------------------------------------------------------------------------------------------------------------
# Работа с новым клиентом


# Добавление элементов для перехода на элементы таблиц
def method_New_Klient(messeg):
    """
    This function creates and configures buttons and labels for the New Klients functionality.
    It opens a new window and displays buttons to navigate to the New Klients table or make an Otchet.

    Parameters:
    messeg (str): A message string that is used to customize the label text.

    Returns:
    None
    """
    Logger("\t", "", "Method method_New_Klient - making element...")
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
    """
    Opens a new window for the New Klients functionality.

    This function appends a new window to the list of windows, configures its title and size,
    and calls the `do_new_klient` function to start the New Klients functionality.

    Parameters:
    flag (int): A flag indicating the type of operation to be performed.
                 It is passed to the `do_new_klient` function.

    Returns:
    None
    """
    Logger(file_name, "", "Method start_new_klient - open new window...")
    wind = Win.Window("New klient", "1000x300")
    wind.make_protokol(wind.close_window)
    windows.append(wind)
    do_new_klient(flag, wind)


# --------------------------------------------------------------------------------------------------------------------------------


# Старт приложение
def start():
    """
    This function starts the main loop of the application.
    It opens the first window in the list of windows and logs the start event.

    Parameters:
    None

    Returns:
    None
    """
    Logger(file_name, "", "Method start - start main loop...")
    window.open()


# Конец приложения
def end():
    """
    This function closes all the windows in the application and logs the end event.

    Parameters:
    None

    Returns:
    None

    The function iterates through the list of windows, destroys each window using the `destroy` method,
    and logs the end event using the `Logger` function.
    """
    Logger(file_name, "", "Method end - end main loop...")
    for window in windows:
        window.destroy()
    Logger(file_name, "", "Method end - close program...")


# Делаем основное окно приложения
Logger(file_name, "", "start program...")
window = Win.Window("PC for management", "600x400")
window.make_protokol(end)
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
    command=end,
)
button_to_end.grid(row=5, column=1, pady=10)

start()
