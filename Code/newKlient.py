import xml.etree.ElementTree as ET
import Window as W
import sqlite3 as bd


def new_Klient_Tabel(window_new_klient):
    """
    The function `new_Klient_Start` sets up a new window for managing a PC.
    
    @param window_new_klient The parameter `window_new_klient` is likely a Tkinter `Tk` object, which represents the main
    window of a GUI application in Python. The function `new_Klient_Start` seems to be setting up a new window for a client
    management application by configuring its title, size, and creating
    """
    print("File newKlient: Method new_Klient_Table - start")
    window_new_klient.title("New klient")
    window_new_klient.geometry("600x400")
    frame = W.Frame(master=window_new_klient, relief=W.SUNKEN)
    frame.pack(expand=True)
    conn = bd.connect("Code\DateBase\Pc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klient_new")
    rows = cursor.fetchall()

    y = 1
    for line in rows:
        ID = W.Label(frame, text=line[0],)
        ID.grid(row = y, column=1)
        Name = W.Label(frame, text=line[1],)
        Name.grid(row = y, column=2)
        y += 1
        
    window_new_klient.mainloop()

