import xml.etree.ElementTree as ET
import Window as W


def new_Klient_Start(window_new_klient):
    """
    The function `new_Klient_Start` sets up a new window for managing a PC.
    
    @param window_new_klient The parameter `window_new_klient` is likely a Tkinter `Tk` object, which represents the main
    window of a GUI application in Python. The function `new_Klient_Start` seems to be setting up a new window for a client
    management application by configuring its title, size, and creating
    """
    print("File newKlient: Start")
    window_new_klient.title("PC for management")
    window_new_klient.geometry("600x400")
    frame = W.Frame(master=window_new_klient, relief=W.SUNKEN)
    frame.pack(expand=True)
    window_new_klient.mainloop()

