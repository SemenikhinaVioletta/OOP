import a_Window as Win

windows = [[], [], [], [], []]
database = "Code\DateBase\Pc.db"
client_statuses = []
contract_statuses = []


def create_combobox(current_status, row_index, parent_frame):
    """
    Creates a Combobox widget with available client IDs based on the current status.

    Parameters:
    current_status (str): The current status of the client.
    row_index (int): The row index where the Combobox should be placed in the parent frame.
    parent_frame (Tkinter.Frame): The parent frame where the Combobox should be placed.

    Returns:
    Tkinter.Combobox: The created Combobox widget.
    """
    available_methods = []
    for client in client_statuses:
        if client.get_status() != current_status:
            available_methods.append(str(client.get_ID()))
    combobox = Win.Combobox(
        parent_frame, values=available_methods, width=30, state="readonly"
    )
    combobox.grid(row=row_index, column=2, pady=5)
    combobox.set(current_status)
    return combobox
