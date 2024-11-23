import xml.etree.ElementTree as ET
import Window as W
import newKlient
from newKlient import new_Klient_Start


def start():
    """
    The function `start` in a Python file opens a window using `window.mainloop()`.
    """
    print("File Python. Method start: Open window")
    window.mainloop()


def end():
    """
    The function `end` in a Python file prints a message, calls two button-click methods, and then prints another message.
    """
    print("File Python. Method end: End")
    window.button_clicked()
    window_new_klient.button_clicked()
    print("Clouse window")


def method_Pro_Klient(messeg):
    """
    The method_Pro_Klient function creates a new button with a specified message and command.

    @param messeg The `messeg` parameter in the `method_Pro_Klient` function seems to be a message or text that will be
    displayed on a button created in the function. When calling this function, you would pass the specific message or text
    that you want to be displayed on the button as the `mes
    """
    print("File FirstDisplay: Method Pro Klients")
    new_window = W.Button(
        frame,
        text=messeg,
        command=start_new_klient,
    )
    new_window.grid(row=2, column=2, padx=10)


def selected(event):
    """
    The `selected` function prints the selected item from a widget and calls different methods based on the selection.
    
    @param event The `event` parameter in the `selected` function is typically an event object that provides information
    about the event that triggered the function. In this case, it seems like the function is handling an event related
    to selecting an item in a widget (possibly a combobox).
    """
    print("File FirstDisplay: Selected item", event.widget.get())
    selection = combobox.get()
    if selection == "Pro Klients":
        method_Pro_Klient(selection)
    elif selection == "New Klients": # make later
        method_Pro_Klient(selection)
        # method_New_Klient(selection)
    elif selection == "Kontrakts": # make later
        method_Pro_Klient(selection)
        # method_Kontrakt(selection)
    elif selection == "Produkts": # make later
        method_Pro_Klient(selection)
        # method_Prodykt(selection)


def start_new_klient():
    """
    The function `start_new_klient` initializes a new client window and displays the table for new clients.
    """
    print("File FirstDisplay: Start table New Klient")
    global window_new_klient
    window_new_klient = W.Window()
    new_Klient_Start(window_new_klient)


print("File FirstDisplay: Start")

"""The code snippet you provided is setting up the initial window and user interface
elements for a program. Here's a breakdown of what each part of the code is doing:"""
# Set first window
window = W.Window()
window.title("PC for management")
window.geometry("600x400")
frame = W.Frame(master=window, relief=W.SUNKEN)
frame.pack(expand=True)

# Set tex
method_lbl = W.Label(frame, text="Select the table you will work with")
method_lbl.grid(row=1, column=1)

# Add combobox and label
method = ["Pro Klients", "New Klients", "Kontrakts", "Produkts"]
combobox = W.Combobox(frame, values=method, width=30, state="readonly")
combobox.grid(row=2, column=1, pady=10)
combobox.set("Nothing selected")
combobox.bind("<<ComboboxSelected>>", selected)

# Set button to end all
button_to_end = W.Button(
    frame,
    text="End all",
    command=end,
)
button_to_end.grid(row=3, column=1, pady=10)

# Start program
start()
