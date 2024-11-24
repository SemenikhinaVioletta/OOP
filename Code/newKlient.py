import Window as Win
import sqlite3 as bd
import New_klient as New


def new_Klient_Tabel(window_new_klient):
    """
    The function `new_Klient_Start` sets up a new window for managing a PC.
    
    @param window_new_klient The parameter `window_new_klient` is likely a Tkinter `Tk` object, which represents the main
    window of a GUI application in Python. The function `new_Klient_Start` seems to be setting up a new window for a client
    management application by configuring its title, size, and creating
    """
    
    
    klients = []
    
    def make_Table():
        columns = ("ID", "Name", "Phone", "Mail")
        table_new_klient = Win.ttk.Treeview(frame, columns=columns, show="headings")
        table_new_klient.grid(row=1, column=1, sticky="nsew")
        table_new_klient.pack(fill=Win.BOTH, expand=1)
        table_new_klient.heading("ID", text="ID", anchor=Win.W)
        table_new_klient.heading("Name", text="Name", anchor=Win.W)
        table_new_klient.heading("Phone", text="Phone", anchor=Win.W)
        table_new_klient.heading("Mail", text="Mail", anchor=Win.W)
        
        
        table_new_klient.column("#1", stretch=Win.NO, width=50)

        for line in rows:
            klient = New.New_Klient(line[0], line[1], line[2], line[3])
            table_new_klient.insert("", Win.END, values=klient)
            klients.append(klient)
        
        print(klients)
        scrollbar = Win.ttk.Scrollbar(frame, orient=Win.VERTICAL, command=table_new_klient.yview)
        
    print("File newKlient: Method new_Klient_Table - start")
    window_new_klient.title("New klient")
    window_new_klient.geometry("1000x300")
    frame = Win.Frame(master=window_new_klient, relief=Win.SUNKEN)
    frame.pack(expand=True)
    conn = bd.connect("Code\DateBase\Pc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klient_new")
    rows = cursor.fetchall()
    
    add_new_klient = Win.Button(frame, text="Add Klient")
    add_new_klient.grid(row=2, column=1)
    
    make_Table()
    
    window_new_klient.mainloop()

