import Window as Win
from newKlient import do_new_klient


def start():
    """
    The function `start` in a Python file opens a window using `window.mainloop()`.
    """
    print("File FirstDisplay: Method start - open window")
    window.mainloop()


def end():
    """
    The function `end` in a Python file prints a message, calls two button-click methods, and then prints another message.
    """
    print("File FirstDisplay: Method end - end all windows")
    window.button_clicked()
    window_new_klient.button_clicked()
    print("\tClouse window")


def method_New_Klient(messeg):
    """
    This function creates and displays buttons for opening a new client window and making an otchet.

    Parameters:
    messeg (str): A message string that is used to customize the label text.

    Returns:
    None. This function only creates and displays UI elements.
    """
    print("File FirstDisplay: Method Pro Klients - make button for open new window")
    new_window = Win.Button(
        frame,
        text="Open table",
        command=lambda: start_new_klient(1),
    )
    lable = Win.Label(frame, text="For " + messeg + "you csn:")
    lable.grid(row=3, column=1, padx=10)
    new_window.grid(row=3, column=2, padx=10)

    new_otchet = Win.Button(
        frame,
        text="Make Otchet",
        command=lambda: start_new_klient(2),
    )
    new_otchet.grid(row=4, column=2, padx=10, pady=10)


def selected(event):
    """
    This function handles the selection event in the Combobox widget. It retrieves the selected item,
    checks its value, and calls the corresponding function to display UI elements.

    Parameters:
    event (tkinter.Event): The event object that triggered this function. It contains information about the event,
                           such as the widget that triggered the event.

    Returns:
    None. This function only prints messages and calls other functions.
    """
    print("File FirstDisplay: Method selected - selected item", event.widget.get())
    selection = combobox.get()
    if selection == "New Klients":
        method_New_Klient(selection)
        """elif selection == "Pro Klients":
        method_Pro_Klient(selection)
        elif selection == "Kontrakts":
        method_Kontrakt(selection)
        elif selection == "Produkts":
        method_Prodykt(selection)"""
    else:
        print(
            "\tFile FirstDisplay: Method selected - selected item",
            selection,
            "not found",
        )

def start_new_klient(flag):
    """
    This function initializes a new client window based on the provided flag.

    Parameters:
    flag (int): An integer flag that determines the type of client window to be opened.
                1 - Opens a new client table.
                2 - Opens a new client report.

    Returns:
    None. This function only initializes the new client window and calls the `do_new_klient` function.
    """
    print("File FirstDisplay: Method start_new_klient - start table New Klient")
    global window_new_klient
    window_new_klient = Win.Window()
    do_new_klient(flag, window_new_klient)


print("File FirstDisplay: Start")

"""The code snippet you provided is setting up the initial window and user interface
elements for a program. Here's a breakdown of what each part of the code is doing:"""
# Set first window
window = Win.Window()
window.title("PC for management")
window.geometry("600x400")
frame = Win.Frame(master=window, relief=Win.SUNKEN)
frame.pack(expand=True)

# Set tex
method_lbl = Win.Label(frame, text="Select the table you will work with")
method_lbl.grid(row=1, column=1)

# Add combobox and label
method = ["Pro Klients", "New Klients", "Kontrakts", "Produkts"]
combobox = Win.Combobox(frame, values=method, width=30, state="readonly")
combobox.grid(row=2, column=1, pady=10)
combobox.set("Nothing selected")
combobox.bind("<<ComboboxSelected>>", selected)

# Set button to end all
button_to_end = Win.Button(
    frame,
    text="End all",
    command=end,
)
button_to_end.grid(row=5, column=1, pady=10)

# Start program
start()

