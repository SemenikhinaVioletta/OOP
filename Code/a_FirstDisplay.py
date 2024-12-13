import a_Window as WindowModule
import b_Error as NewClientError
import c_Error as ProClientError
import d_Error as ProductError

# import e_Error as ContractError
from a_Log import Logger
from a_Global_Per import windows
from b_newClient import do_new_client
from c_proClient import do_pro_client
from c_proClient import make_array as make_clients
from d_Produkt import do_product
from d_Produkt import make_array as make_products
from e_Contract import do_contract
from e_Contract import make_array as make_contrakts
from f_Class_Status_Client import make_status


file_name = "File FirstDisplay"
window = WindowModule.Window("PC for management", "600x400")

# --------------------------------------------------------------------------------------------------------------------------------


def on_selection(event):
    """
    This function handles the user's selection from the Combobox component.
    It logs the selected option, creates a Label and a Button based on the selection,
    and configures the Button's command to open the corresponding window.

    Parameters:
    event (Event): The event object that triggered this function.

    Returns:
    None
    """
    selected_option = combobox.get()
    Logger.log_info(
        file_name, f"Method on_selection - selected option: {selected_option}\n"
    )
    frame.destroy()
    set_frame()
    if selected_option == "New clients":
        Logger.log_info(file_name, f"Starting New client process...")
        Logger.log_info(
            file_name, f"Entering handle_new_client with message: {selected_option}"
        )
        label = WindowModule.Label(frame, text="For " + selected_option + " you can:")
        new_window_button = WindowModule.Button(
            frame, text="Open table", command=lambda: start_new_client(1)
        )
        label.grid(row=3, column=1, padx=10)
        new_window_button.grid(row=3, column=2, padx=10)
    elif selected_option == "Pro clients":
        Logger.log_info(file_name, "Starting Pro clients process...")
        Logger.log_info(
            file_name, f"Entering handle_new_client with message: {selected_option}"
        )
        label = WindowModule.Label(frame, text="For " + selected_option + " you can:")
        new_window_button = WindowModule.Button(
            frame, text="Open table", command=lambda: start_pro_client(1)
        )
        label.grid(row=3, column=1, padx=10)
        new_window_button.grid(row=3, column=2, padx=10)
    elif selected_option == "Products":
        Logger.log_info(file_name, "Starting Products process...")
        Logger.log_info(
            file_name, f"Entering handle_new_client with message: {selected_option}"
        )
        label = WindowModule.Label(frame, text="For " + selected_option + " you can:")
        new_window_button = WindowModule.Button(
            frame, text="Open table", command=lambda: start_products(1)
        )
        label.grid(row=3, column=1, padx=10)
        new_window_button.grid(row=3, column=2, padx=10)
    elif selected_option == "Contracts":
        Logger.log_info(file_name, "No method available for selection")
        Logger.log_info(
            file_name, f"Entering handle_new_client with message: {selected_option}"
        )
        label = WindowModule.Label(frame, text="For " + selected_option + " you can:")
        new_window_button = WindowModule.Button(
            frame,
            text="Open table",
            command=lambda: start_contract(1),
            # state=["disabled"],
        )
        label.grid(row=3, column=1, padx=10)
        new_window_button.grid(row=3, column=2, padx=10)
    else:
        Logger.log_info(file_name, "No method available for selection")
        Logger.log_info(
            file_name, f"Entering handle_new_client with message: {selected_option}"
        )
        label = WindowModule.Label(frame, text="For " + selected_option + " you can:")
        new_window_button = WindowModule.Button(
            frame, text="Open table", state=["disabled"]
        )


# --------------------------------------------------------------------------------------------------------------------------------


def start_new_client(flag: int) -> None:
    """
    This function opens a new client window based on the provided flag.
    It checks if a new client window is already open and raises an exception if it is.
    If the window is not open, it logs the opening event, creates a new window,
    sets the window protocol, adds the window to the list of windows,
    and calls the function to handle new client operations.

    Parameters:
    flag (int): A flag indicating the type of operation to be performed.

    Returns:
    None
    """
    try:
        if len(windows[2]) != 0:
            raise NewClientError.ErrorNewClient("This window is already open.")
        Logger.log_info(file_name, f"Opening new client window with flag: {flag}")
        new_window = WindowModule.Window("New Client", "1000x300")
        new_window.make_protokol(lambda: WindowModule.end(2))
        windows[2].append(new_window)

        do_new_client(flag, new_window)

    except NewClientError.ErrorNewClient as e:
        Logger.log_error(file_name, "Error while opening window", str(e))


# --------------------------------------------------------------------------------------------------------------------------------


def start_pro_client(flag):
    """
    This function starts a pro client window based on the provided flag.
    It checks if a pro client window is already open and raises an exception if it is.
    If the window is not open, it logs the opening event, creates a new window,
    sets the window protocol, adds the window to the list of windows,
    and calls the function to handle pro client operations.

    Parameters:
    flag (int): A flag indicating the type of operation to be performed.

    Returns:
    None

    Raises:
    ProClientError.ErrorProClient: If a pro client window is already open.
    """
    try:
        if len(windows[1]) != 0:
            raise ProClientError.ErrorProClient("This window is already open.")

        Logger.log_info(file_name, f"Opening pro client window with flag: {flag}")

        new_window = WindowModule.Window("Pro Client", "1500x300")
        new_window.make_protokol(lambda: WindowModule.end(1))
        windows[1].append(new_window)

        do_pro_client(flag, new_window)

    except ProClientError.ErrorProClient as e:
        Logger.log_error(file_name, "Error opening window", str(e))


# --------------------------------------------------------------------------------------------------------------------------------


def start_products(flag: int) -> None:
    """
    This function starts a product window based on the provided flag.
    It checks if a product window is already open and raises an exception if it is.
    If the window is not open, it logs the opening event, creates a new window,
    sets the window protocol, adds the window to the list of windows,
    and calls the function to handle product operations.

    Parameters:
    flag (int): A flag indicating the type of operation to be performed.

    Returns:
    None

    Raises:
    ProductError.ErrorProduct: If a product window is already open.
    """
    try:
        if len(windows[3]) != 0:
            raise ProductError.ErrorProduct("This window is already open.")
        Logger.log_info(file_name, f"Opening product window with flag: {flag}")
        wind = WindowModule.Window("Product", "1000x300")
        wind.make_protokol(lambda: WindowModule.end(3))
        windows[3].append(wind)
        do_product(flag, wind)
    except ProductError.ErrorProduct as e:
        Logger.log_error(
            file_name, "An error occurred while opening the window", str(e)
        )


# --------------------------------------------------------------------------------------------------------------------------------


def start_contract(flag):
    try:
        if len(windows[4]) != 0:
            raise ProductError.ErrorProduct("This window is already open.")
        Logger.log_info(file_name, f"Opening contract window with flag: {flag}")
        wind = WindowModule.Window("Contracts", "1000x300")
        wind.make_protokol(lambda: WindowModule.end(4))
        windows[4].append(wind)
        do_contract(flag, wind)
    except ProductError.ErrorProduct as e:
        Logger.log_error(
            file_name, "An error occurred while opening the window", str(e)
        )


# --------------------------------------------------------------------------------------------------------------------------------


def start():
    """
    This module is responsible for the initial display setup of the application.

    It includes the necessary components and configurations to create the first user interface that users will interact with. The module aims to facilitate the presentation of information and user inputs in a clear and organized manner.
    """
    Logger.log_info(file_name, "Starting application...")
    window.open()


def set_frame():
    """
    This function sets up the main frame for the application's user interface.
    It creates a frame, a label, a combobox, and a button, and configures their layout and behavior.

    Parameters:
    None

    Returns:
    None
    """
    global frame
    frame = WindowModule.Frame(master=window, relief=WindowModule.SUNKEN)
    frame.pack(expand=True)
    method_label = WindowModule.Label(
        frame, text="Select the table you will work with:"
    )

    methods = [
        "Pro clients",
        "New clients",
        "Contracts",
        "Products",
    ]

    global combobox
    combobox = WindowModule.Combobox(frame, values=methods, width=30, state="readonly")
    method_label.grid(row=1, column=1)

    combobox.grid(row=2, column=1, pady=10)
    combobox.set("Nothing selected")
    combobox.bind("<<ComboboxSelected>>", on_selection)
    button_to_end = WindowModule.Button(
        frame,
        text="End all",
        command=lambda: WindowModule.end(0),
    )
    button_to_end.grid(row=5, column=1, pady=10)


# --------------------------------------------------------------------------------------------------------------------------------

window.make_protokol(lambda: WindowModule.end(0))
windows[0].append(window)


set_frame()
make_status()
make_clients()
make_products()
make_contrakts()
start()
