from a_Global_per import basadate
import a_Window as Win
import sqlite3 as bd

file_name = "File Produkt"


def produkt_Table(wind):
    


def make_array():
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    for line in rows:
        klient = New.New_Klient(int(line[0]), str(line[1]), int(line[2]), str(line[3]))
        produkts.append(klient)
    cursor.close()


def do_new_klient(flag, window_new_klient):
    global produkts
    produkts = []
    make_array()
    if flag == 1:
        produkt_Tabel(window_new_klient)
    else:
        # Логирование ошибки
        Logger(
            file_name, "Error in creating new client", "Invalid flag in do_new_klient"
        )
