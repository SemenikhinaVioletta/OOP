import sqlite3 as bd
from a_Global_per import basadate, status_klient, status_kontrakt


class status_Klient:

    def __init__(self, id, status):
        self.id = id
        self.status = status

    def get(self):
        return int(self.id), str(self.status)

    def get_status(self):
        return str(self.status)

    def get_ID(self):
        return int(self.id)

class status_Kontrakt:
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def get(self):
        return int(self.id), str(self.status)

    def get_status(self):
        return str(self.status)

    def get_ID(self):
        return int(self.id)
    


def make_status():
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Status_klient")
    rows = cursor.fetchall()
    for line in rows:
        stat_klient = status_Klient(int(line[0]), str(line[1]))
        status_klient.append(stat_klient)
    cursor.close()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Status_kontrakt")
    rows = cursor.fetchall()
    for line in rows:
        stat_kontrakt = status_Kontrakt(int(line[0]), str(line[1]))
        status_kontrakt.append(stat_kontrakt)
    cursor.close()
    conn.close()

