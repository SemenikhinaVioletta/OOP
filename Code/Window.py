import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import Log
from Log import Logger

file_name = "File Window: "


class Window(Tk):

    def __init__(self, name, geom):
        super().__init__()
        self.title(name)
        self.geometry(geom)

    def open(self):
        self.mainloop()

    def close(self):
        self.destroy()
