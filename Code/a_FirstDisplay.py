import a_Window as WindowModule
import b_Error as NewClientError
import c_Error as ProClientError
import d_Error as ProductError
import e_Error as ContractError
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
from f_Make_Report import make_othet


file_name = "File FirstDisplay"
window = WindowModule.Window("PC for management", "600x400")

# --------------------------------------------------------------------------------------------------------------------------------


def on_selection(event):
    """
    This function handles the selection event in the GUI application. It logs the selected option,
    destroys the current frame, sets a new frame with the selected option, and creates buttons for
    opening related tables or generating reports.

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
    set_frame(selected_option)
    make_otchet_button = WindowModule.Button(
        frame, text="make report", command=lambda: make_othet(selected_option)
    )
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
        make_otchet_button.grid(row=4, column=2, padx=10, pady=10)
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
        make_otchet_button.grid(row=4, column=2, padx=10, pady=10)
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
        )
        label.grid(row=3, column=1, padx=10)
        new_window_button.grid(row=3, column=2, padx=10)
        make_otchet_button.grid(row=4, column=2, padx=10, pady=10)
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
    Opens a new client window with the specified flag.

    Parameters:
    flag (int): A flag indicating the mode of operation for the new client window.

    Returns:
    None

    Raises:
    NewClientError.ErrorNewClient: If a new client window is already open.
    """
    try:
        if len(windows[2]) != 0:
            raise NewClientError.ErrorNewClient("This window is already open.")
        Logger.log_info(file_name, f"Opening new client window with flag: {flag}")
        new_window = WindowModule.Window("New Client", "700x300")
        new_window.make_protokol(lambda: WindowModule.end(2))
        windows[2].append(new_window)

        do_new_client(flag, new_window)

    except NewClientError.ErrorNewClient as e:
        Logger.log_error(file_name, "Error while opening window", str(e))


# --------------------------------------------------------------------------------------------------------------------------------


def start_pro_client(flag):
    """
    Opens a new pro client window with the specified flag.

    Parameters:
    flag (int): A flag indicating the mode of operation for the pro client window.

    Returns:
    None

    Raises:
    ProClientError.ErrorProClient: If a pro client window is already open.

    The function attempts to open a new pro client window with the given flag.
    If a pro client window is already open, it raises a ProClientError.
    If the operation is successful, it logs the opening of the pro client window,
    creates a new window with the specified dimensions, sets a protocol to close the window,
    appends the new window to the windows list, and calls the do_pro_client function with the flag and the new window.
    If an error occurs during the process, it logs the error and its message.
    """
    try:
        if len(windows[1]) != 0:
            raise ProClientError.ErrorProClient("This window is already open.")

        Logger.log_info(file_name, f"Opening pro client window with flag: {flag}")

        new_window = WindowModule.Window("Pro Client", "1200x300")
        new_window.make_protokol(lambda: WindowModule.end(1))
        windows[1].append(new_window)

        do_pro_client(flag, new_window)

    except ProClientError.ErrorProClient as e:
        Logger.log_error(file_name, "Error opening window", str(e))


# --------------------------------------------------------------------------------------------------------------------------------


def start_products(flag: int) -> None:
    """
    Opens a new product window with the specified flag.

    Parameters:
    flag (int): A flag indicating the mode of operation for the product window.

    Returns:
    None

    Raises:
    ProductError.ErrorProduct: If a product window is already open.

    The function attempts to open a new product window with the given flag.
    If a product window is already open, it raises a ProductError.
    If the operation is successful, it logs the opening of the product window,
    creates a new window with the specified dimensions, sets a protocol to close the window,
    appends the new window to the windows list, and calls the do_product function with the flag and the new window.
    If an error occurs during the process, it logs the error and its message.
    """
    try:
        if len(windows[3]) != 0:
            raise ProductError.ErrorProduct("This window is already open.")
        Logger.log_info(file_name, f"Opening product window with flag: {flag}")
        wind = WindowModule.Window("Product", "700x300")
        wind.make_protokol(lambda: WindowModule.end(3))
        windows[3].append(wind)
        do_product(flag, wind)
    except ProductError.ErrorProduct as e:
        Logger.log_error(
            file_name, "An error occurred while opening the window", str(e)
        )


# --------------------------------------------------------------------------------------------------------------------------------


def start_contract(flag):
    """
    Opens a new contract window with the specified flag.

    Parameters:
    flag (int): A flag indicating the mode of operation for the contract window.

    Returns:
    None

    Raises:
    ContractError.ErrorContract: If a contract window is already open.

    The function attempts to open a new contract window with the given flag.
    If a contract window is already open, it raises a ContractError.
    If the operation is successful, it logs the opening of the contract window,
    creates a new window with the specified dimensions, sets a protocol to close the window,
    appends the new window to the windows list, and calls the do_contract function with the flag and the new window.
    If an error occurs during the process, it logs the error and its message.
    """
    try:
        if len(windows[4]) != 0:
            raise ProductError.ErrorProduct("This window is already open.")
        Logger.log_info(file_name, f"Opening contract window with flag: {flag}")
        wind = WindowModule.Window("Contracts", "1000x300")
        wind.make_protokol(lambda: WindowModule.end(4))
        windows[4].append(wind)
        do_contract(flag, wind)
    except ContractError.ErrorContract as e:
        Logger.log_error(
            file_name, "An error occurred while opening the window", str(e)
        )


# --------------------------------------------------------------------------------------------------------------------------------


def start():
    """
    This function starts the application by opening the main window.

    Parameters:
    None

    Returns:
    None

    The function logs the start of the application using the Logger module,
    and then calls the open method of the window object to display the main window.
    """
    Logger.log_info(file_name, "Starting application...")
    window.open()


def set_frame(message: str) -> None:
    """
    This function sets up the main frame for the application, allowing the user to select a table to work with.

    Parameters:
    message (str): The initial message to display in the combobox.

    Returns:
    None

    The function creates a new frame within the main window, adds a label and a combobox for selecting a table,
    sets the initial message in the combobox, binds the on_selection function to the combobox's selection event,
    and adds a button to end all windows.
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
    combobox.set(message)
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


set_frame("Nothing selected")
make_status()
make_clients()
make_products()
make_contrakts()
print()
start()
