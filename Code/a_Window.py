import sqlite3 as bd
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from a_Log import Logger
from a_Global_Per import windows

file_name = "File Window"


class Window(Tk):
    """
    A custom Tkinter window class with enhanced logging and event handling capabilities.

    The Window class extends the Tkinter Tk class to provide additional functionality for creating,
    managing, and interacting with graphical windows in a Python application.

    Attributes:
        name (str): The name of the window.

    Methods:
        __init__(name, geom): Creates a new window with specified name and geometry.
        open(): Starts the Tkinter event loop for the window.
        make_protokol(fun): Sets a protocol handler for window closing events.
        close_window(flag): Closes the window and removes it from a specified window list.
    """

    def __init__(self, name, geom):
        """
        Initialize a new instance of the Window class.

        Creates a new window with the specified name and geometry.
        Logs an informational event indicating the creation of the window.

        Parameters:
        name (str): The name of the window.
        geom (str): The geometry of the window, specified as a string in the format "widthxheight+x+y".

        Returns:
        None
        """
        super().__init__()
        self.title(name)
        self.geometry(geom)
        self.name = name
        Logger.log_info(
            file_name, "Class Window - Method __init__ - make window: " + name
        )


    # --------------------------------------------------------------------------------------------------------------------------------

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
        Set a protocol handler for the "WM_DELETE_WINDOW" event.

        This method sets a protocol handler for the "WM_DELETE_WINDOW" event, which is triggered when the user attempts to close the window.
        The provided function `fun` will be called when this event occurs.

        Parameters:
        fun (function): A function to be called when the "WM_DELETE_WINDOW" event is triggered.
                        This function should handle the closing of the window or perform any necessary cleanup.

        Returns:
        None
        """
        self.protocol("WM_DELETE_WINDOW", fun)

    def close_window(self, flag):
        """
        Closes the current window and removes it from the list of windows associated with the given flag.

        This method logs an event indicating that the window is being closed.
        It then removes the current window instance from the list of windows associated with the given flag.
        Finally, it destroys the current window.

        Parameters:
        flag (int): A flag indicating which list of windows to remove the current window from.

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


def end(flag):
    """
    Ends the main loop of the application and closes all windows based on the provided flag.

    This function logs an event indicating that the main loop is ending.
    It then checks the value of the `flag` parameter to determine which windows to close.
    If `flag` is 0, it iterates through all windows in the `windows` list and destroys each window.
    If `flag` is not 0, it iterates through the windows in the `windows[flag]` list, destroys each window,
    and clears the `windows[flag]` list.
    Finally, it logs an event indicating that the program is closing.

    Parameters:
    flag (int): A flag indicating which windows to close. If `flag` is 0, all windows are closed.
                 If `flag` is not 0, only the windows in the `windows[flag]` list are closed.

    Returns:
    None
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
