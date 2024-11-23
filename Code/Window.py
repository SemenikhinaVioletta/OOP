import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


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
        print("\tFile Window: Class Window: Method ___init__ - make window: ", self.)

    def button_clicked(self):
        """
        Destroys the current window when called.

        Parameters:
            None

        Returns:
            None
        """
        print("\tFile Window: Class Window: Method button_clicked - destroy window: ", self)
        self.destroy()
