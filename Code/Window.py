import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import Log
from Log import Logger
from Global_per import windows

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

#--------------------------------------------------------------------------------------------------------------------------------
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


    def close_window(self):
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
        windows.remove(self)
        self.destroy()
#--------------------------------------------------------------------------------------------------------------------------------

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
        Logger(file_name, "", "Class Window - Method __del__ - delete window: " + self.name)
        windows.remove(self)
