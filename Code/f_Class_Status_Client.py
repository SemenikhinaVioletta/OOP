import sqlite3 as bd
from a_Global_Per import database, client_statuses, contract_statuses


class Client_statuses:

    def __init__(self, id, status):
        self.id = id
        self.status = status

    def get(self):
        return int(self.id), str(self.status)

    def get_status(self):
        return str(self.status)

    def get_ID(self):
        return int(self.id)


class Contract_statues:
    
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
    conn = bd.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Status_klient")
    rows = cursor.fetchall()
    for line in rows:
        stat_klient = Client_statuses(int(line[0]), str(line[1]))
        client_statuses.append(stat_klient)
    cursor.close()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Status_kontrakt")
    rows = cursor.fetchall()
    for line in rows:
        stat_kontrakt = Contract_statues(int(line[0]), str(line[1]))
        contract_statuses.append(stat_kontrakt)
    cursor.close()
    conn.close()
