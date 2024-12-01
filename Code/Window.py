import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import Log
from Log import Logger

file_name = "File Window"


class Window(Tk):

    def __init__(self, name, geom):
        super().__init__()
        self.title(name)
        self.geometry(geom)
        self.name = name
        Logger(file_name, "", "Class Window - Method __init__ - make window: " + name)

    def open(self):
        self.mainloop()
        Logger(file_name, "", "Class Window - Method open - open window: " + self.name)

    def close(self):
        self.destroy()
        Logger(file_name, "", "Class Window - Method close - close window: " + self.name)
