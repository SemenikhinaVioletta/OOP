import sqlite3 as bd
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from a_Log import Logger
from a_Global_per import windows

file_name = "File Window"


class Window(Tk):

    def __init__(self, name, geom):
        """
        Initialize a new instance of the Window class.

        Parameters:
        name (str): The title of the window.
        geom (str): The geometry of the window in the format "widthxheight+x+y".

        Returns:
        None
        """
        super().__init__()
        self.title(name)
        self.geometry(geom)
        self.name = name
        Logger(file_name, "", "Class Window - Method __init__ - make window: " + name)

    # --------------------------------------------------------------------------------------------------------------------------------
    # Дополнительные функции
    def open(self):
        """
        Open the window and start the Tkinter event loop.

        This method starts the Tkinter event loop, allowing the window to respond to user interactions.
        It also logs an event indicating that the window has been opened.

        Parameters:
        None

        Returns:
        None
        """
        self.mainloop()
        Logger(file_name, "", "Class Window - Method open - open window: " + self.name)

    def make_protokol(self, fun):
        """
        The function `make_protokol` sets a protocol for the WM_DELETE_WINDOW event in Python.

        @param fun The `fun` parameter in the `make_protokol` method is expected to be a function that will be called when the window manager event `WM_DELETE_WINDOW` is triggered. This function will be associated with handling the event when the user tries to close the window.
        """
        self.protocol("WM_DELETE_WINDOW", fun)

    def close_window(self, flag):
        """
        Close the current window and remove it from the list of open windows.

        This method logs an event indicating that the window is not adding a new client and is closing.
        It then removes the current window from the provided list of open windows and destroys the window.

        Parameters:
        windows (list): A list of open windows. The current window will be removed from this list.

        Returns:
        None
        """
        Logger(
            file_name,
            "",
            "Class Window - Method close_window - go bak",
        )
        windows[flag].remove(self)
        self.destroy()

    # --------------------------------------------------------------------------------------------------------------------------------

    # Деструктор
    def __del__(self):
        """
        Destructor method for the Window class.

        This method logs an event indicating that the window is being deleted.
        It is automatically called when the instance of the class is about to be destroyed.

        Parameters:
        None

        Returns:
        None
        """
        Logger(
            file_name, "", "Class Window - Method __del__ - delete window: " + self.name
        )


# --------------------------------------------------------------------------------------------------------------------------------
# Конец приложения
def end(flag):
    """
    This function closes all the windows in the application and logs the end event.

    Parameters:
    None

    Returns:
    None

    The function iterates through the list of windows, destroys each window using the `destroy` method,
    and logs the end event using the `Logger` function. The `Logger` function is expected to be defined elsewhere
    and takes three parameters: `file_name` (the name of the file where the log is being written),
    `client_name` (the name of the client associated with the log), and `message` (the actual log message).
    The `windows` list is expected to be a global variable containing a list of open windows.
    """
    Logger(file_name, "", "Method end - end main loop...")
    if flag == 0:
        for window in windows:
            for i in window:
                i.destroy()
    else:
        for i in range(len(windows[flag])):
            windows[flag][i].destroy()
        windows[flag].clear()
    Logger(file_name, "", "Method end - close program...")
