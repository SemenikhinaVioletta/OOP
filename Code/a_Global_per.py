import a_Window as Win
import a_Log as Logger

windows = [[], [], [], [], []]
database = "Code\DateBase\Pc.db"
client_statuses = []
contract_statuses = []
file_mame = "Global File"


def create_combobox(current_status, row_index, parent_frame):
    """
    This function creates a Combobox widget with a list of available client statuses.

    Parameters:
    current_status (str): The current status of the client.
    row_index (int): The row index where the Combobox will be placed in the parent frame.
    parent_frame (Tkinter.Frame): The parent frame where the Combobox will be placed.

    Returns:
    Tkinter.Combobox: The created Combobox widget.
    """
    message = f"Method create_combobox - creating Combobox with state...\n\n"
    available_methods = []
    for client in client_statuses:
        message += (
            f"\t\t\t\tmake client statuses: {client.get_ID()} - {client.get_status()}\n"
        )
        if client.get_status() != current_status:
            available_methods.append(str(client.get_ID()))
    combobox = Win.Combobox(
        parent_frame, values=available_methods, width=30, state="readonly"
    )
    combobox.grid(row=row_index, column=2, pady=5)
    combobox.set(current_status)
    Logger.Logger(file_mame, "", message)
    Logger.Logger(
        file_mame, "", f"Method create_combobox - end creating Combobox with state...\n"
    )
    return combobox
