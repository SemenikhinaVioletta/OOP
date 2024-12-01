import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import Log
from Log import Logger

file_name = "File Window: "


class Window(Tk):
    """
    This class represents a GUI window for an application. It inherits from the Tk class in the tkinter module.

    Attributes:
        None

    Methods:
        __init__(self):
            Constructor for the Window class. Sets up the main window for the GUI application.

        button_clicked(self):
            Destroys the current window when called.
    """

    def __init__(self):
        """
        Constructor for the Window class. Sets up the main window for the GUI application.

        Parameters:
            None

        Returns:
            None
        """
        super().__init__()
        Logger(file_name + "Class Window: Method __init__ - make window: ", "")

    def button_clicked(self):
        """
        Destroys the current window when called.

        Parameters:
            None

        Returns:
            None
        """
        Logger(file_name + "Class Window: Method button_clicked - destroy window: ", "")
        self.destroy()
