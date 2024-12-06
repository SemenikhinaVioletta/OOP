import c_Class_Pro_Klient as Pro
import f_Class_status_klient as stat
from a_Global_per import basadate
from a_Log import Logger
import c_Error as Error
import a_Window as Win
import sqlite3 as bd



def make_array():
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Klient_new")
    rows = cursor.fetchall()
    for line in rows:
        klient = Pro.Pro_Klient(int(line[0]), str(line[1]), int(line[3]), str(line[4]), int(line[5]), str(line[6]), int(line[7]), None)
        klients.append(klient)
    cursor.close()


def do_pro_klient(flag, window_pro_klient):
    global klients
    klients = []
    make_array()
    if flag == 1:
        pro_Klient_Tabel(window_pro_klient)
    else:
        # Логирование ошибки
        Logger(
            file_name, "Error in creating new client", "Invalid flag in do_new_klient"
        )
