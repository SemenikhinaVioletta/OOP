import a_Window as Win
import b_Error as new_Error
import c_Error as pro_Error
import d_Error as prod_Error
from f_Class_status_klient import make_status
from c_proKlient import do_pro_klient
from b_newKlient import do_new_klient
from d_Produkt import do_produkt
from a_Log import Logger
from a_Global_per import windows

file_name = "File FirstDisplay"
window = Win.Window("PC for management", "600x400")
logger = Logger(file_name, [], "Application started")


# Переход к функциям открывающим возможность работы с данными
def selected(event):
    selection = combobox.get()
    logger.log_info(file_name, f"Selected option: {selection}")  # Log selection
    if selection == "New Klients":
        logger.log_info(file_name, "Starting new klient process")  # Log process start
        method_New_Klient(selection)
    elif selection == "Pro Klients":
        logger.log_info(file_name, "Starting Pro Klients process")  # Log process start
        method_pro_klient(selection)
    elif selection == "Produkts":
        logger.log_info(file_name, "Starting Produkts process")  # Log process start
        method_produkts(selection)
    elif selection == "Kontrakts":
        # logger.log_info(file_name, "Starting Kontrakts process")  # Log process start
        # method_Kontrakts()
        logger.log_info(file_name, "No method available for selection")  # Log no method
    else:
        logger.log_info(file_name, "No method available for selection")  # Log no method


# --------------------------------------------------------------------------------------------------------------------------------
# Работа с новым клиентом


def method_New_Klient(messeg):
    """
    The function `method_New_Klient` creates a GUI window with options to open a table or create a report for a given message.

    @param messeg It looks like the `method_New_Klient` function is creating a GUI interface with two buttons for opening a table and making a report. The `messeg` parameter seems to be a message that is displayed in the GUI interface.
    """
    logger.log_info(
        file_name, f"Entering method_New_Klient with message: {messeg}"
    )  # Log method entry
    lable = Win.Label(frame, text="For " + messeg + " you can:")
    lable.grid(row=3, column=1, padx=10)

    new_window = Win.Button(
        frame,
        text="Open table",
        command=lambda: start_new_klient(1),
    )
    new_window.grid(row=3, column=2, padx=10)
    """
    new_otchet = Win.Button(
        frame,
        text="Make Otchet",
        command=lambda: start_new_klient(2),
    )
    new_otchet.grid(row=4, column=2, padx=10, pady=10)"""


def start_new_klient(flag):
    """
    The function `start_new_klient` opens a new klient window with a specified flag and performs additional operations related to the new klient.

    @param flag The `flag` parameter in the `start_new_klient` function is used to determine some behavior or configuration related to opening a new klient window. It is passed as an argument to the function and then used within the function to perform specific actions based on its value.
    """
    try:
        if len(windows[2]) != 0:
            raise new_Error.ErrorNewKlient("The window already open")
        logger.log_info(
            file_name, f"Opening new klient window with flag: {flag}"
        )  # Log window opening
        wind = Win.Window("New klient", "1000x300")
        wind.make_protokol(lambda: Win.end(2))
        windows[2].append(wind)
        do_new_klient(flag, wind)
    except new_Error.ErrorNewKlient as e:
        logger.log_error(file_name, str(e), "A Error intoopen window")


# --------------------------------------------------------------------------------------------------------------------------------
# Работа с про клиентом


def method_pro_klient(message):
    logger.log_info(
        file_name, f"Entering method_pro_Klient with message: {message}"
    )  # Log method entry
    lable = Win.Label(frame, text="For " + message + " you can:")
    lable.grid(row=3, column=1, padx=10)

    new_window = Win.Button(
        frame,
        text="Open table",
        command=lambda: start_pro_klient(1),
    )
    new_window.grid(row=3, column=2, padx=10)


def start_pro_klient(flag):
    try:
        if len(windows[1]) != 0:
            raise pro_Error.ErrorProKlient("The window already open")
        logger.log_info(
            file_name, f"Opening new klient window with flag: {flag}"
        )  # Log window opening
        wind = Win.Window("Pro klient", "1500x300")
        wind.make_protokol(lambda: Win.end(1))
        windows[1].append(wind)
        do_pro_klient(flag, wind)
    except pro_Error.ErrorProKlient as e:
        logger.log_error(file_name, str(e), "A Error intoopen window")


# --------------------------------------------------------------------------------------------------------------------------------
# Работа с Продуктами


def method_produkts(message: str) -> None:
    """
    This function is responsible for displaying a GUI window with options to open a table for managing products.
    It logs the entry into the method and displays a label and a button in the GUI window.

    Parameters:
    message (str): A message that is displayed in the GUI window to inform the user about the purpose of the function.

    Returns:
    None: The function does not return any value.
    """
    logger.log_info(
        file_name, f"Entering method_produkts with message: {message}"
    )  # Log method entry
    lable = Win.Label(frame, text="For " + message + " you can:")
    lable.grid(row=3, column=1, padx=10)

    new_window = Win.Button(
        frame,
        text="Open table",
        command=lambda: start_produkts(1),
    )
    new_window.grid(row=3, column=2, padx=10)


def start_produkts(flag: int) -> None:
    """
    This function opens a new window for managing products based on a given flag.
    It also logs the opening of the window and handles any exceptions that may occur.

    Parameters:
    flag (int): A flag indicating the type of operation to be performed.
                 In this case, it is used to determine the behavior of the function.

    Returns:
    None: The function does not return any value.
    """
    try:
        if len(windows[3]) != 0:
            raise prod_Error.ErrorProduct("The window already open")
        logger.log_info(
            file_name, f"Opening produkt window with flag: {flag}"
        )  # Log window opening
        wind = Win.Window("Produkt", "1000x300")
        wind.make_protokol(lambda: Win.end(3))
        windows[3].append(wind)
        do_produkt(flag, wind)
    except prod_Error.ErrorProdukt as e:
        logger.log_error(file_name, str(e), "A Error intoopen window")


# --------------------------------------------------------------------------------------------------------------------------------
# Старт приложение
def start():
    """
    The `start()` function logs the application start and opens a window.
    """
    logger.log_info(file_name, "Starting application")  # Log application start
    window.open()


# Делаем основное окно приложения
window.make_protokol(lambda: Win.end(0))
windows[0].append(window)

frame = Win.Frame(master=window, relief=Win.SUNKEN)
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
    command=lambda: Win.end(0),
)
button_to_end.grid(row=5, column=1, pady=10)

make_status()
start()
