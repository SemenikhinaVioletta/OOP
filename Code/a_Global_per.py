import a_Window as Win

windows = [[], [], [], [], []]
basadate = "Code\DateBase\Pc.db"
status_klient = []
status_kontrakt = []

def make_combox(now, row_i, frame_for):
    """
    This function creates a Combobox widget with specific values based on the 'status_klient' list.
    The Combobox is then configured to be read-only and placed in the specified frame at the given row and column.

    Parameters:
    now (str): The current status to exclude from the Combobox values.
    row_i (int): The row position in the frame where the Combobox should be placed.
    frame_for (Tkinter.Frame): The frame where the Combobox should be placed.

    Returns:
    Tkinter.Combobox: The configured Combobox widget.
    """
    method = []
    for i in status_klient:
        if i.get_status() != now:
            method.append(str(i.get_ID()))
    combobox = Win.Combobox(frame_for, values=method, width=30, state="readonly")
    combobox.grid(row=row_i, column=2, pady=5)
    combobox.set(now)
    return combobox