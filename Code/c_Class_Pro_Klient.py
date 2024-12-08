import b_Class_New_klient as New
import f_Class_status_klient as stat
from a_Global_per import basadate
import sqlite3 as bd
from a_Log import Logger
import c_Error as Error

file_name = "File Class_Pro_Klient"
logger = Logger(file_name, [], "Application started")


class Pro_Klient(New.New_Klient):

    def __init__(self, ID, name, mora, kontrakt, phone, email, status, klient):
        self.status = status
        self.mora = mora
        self.kontrakt = []
        self.set_kontrakt(kontrakt)
        if klient != None:
            self.ID = klient.ID
            self.name = klient.name
            self.phone = klient.phone
            self.email = klient.email
        else:
            self.ID = ID
            self.name = name
            self.phone = phone
            self.email = email
        self.short = ""
        self.make_short(self.name)

    def make_short(self, name):
        names = name.split()
        self.short = names[0] + " " + names[1][0] + ". " + names[2][0] + "."

    def set_kontrakt(self, kontrakt):
        kontrakts = list(map(int, kontrakt.split()))
        for i in kontrakts:
            if i not in self.kontrakt:  # Если контра��т еще не добавлен
                self.kontrakt.append(i)

    def get_ID(self):
        return int(self.ID)

    def get_full_name(self):
        return str(self.name)

    def get_short_name(self):
        return str(self.short)

    def get_phone(self):
        return int(self.phone)

    def get_email(self):
        return str(self.email)

    def get_status(self):
        return int(self.status)

    def get_mora(self):
        return int(self.mora)

    def get_kontrakt_id(self):
        self.kontrakt.sort()
        s = ""
        for i in self.kontrakt:
            s += str(i) + " "
        return s[:-1]

    def get(self):
        return (
            self.get_ID(),
            self.get_short_name(),
            self.get_mora(),
            self.get_phone(),
            self.get_email(),
            self.get_status(),
        )

    def enter_klient_to_pro_bd(self):
        try:
            conn = bd.connect(basadate)
            cursor = conn.cursor()
            logger.log_info(file_name, "Connected to SQLite")
            cursor.execute("SELECT * FROM Klient")
            cursor.execute(
                """INSERT INTO Klient (Name_klient, Short_name, Mora, Kontrakt_id, Phone, Mail, Status) VALUES(?, ?, ?, ?, ?, ?, ?)""",
                (
                    self.get_full_name(),
                    self.get_short_name(),
                    self.get_mora(),
                    self.get_kontrakt_id(),
                    self.get_phone(),
                    self.get_email(),
                    self.status,
                ),
            )
            conn.commit()
            logger.log_info(
                file_name,
                "Client added to database: "
                + f"Name: {self.get_name()}, Phone: {self.get_phone()}, Email: {self.get_email()}",
            )
        except bd.Error as error:
            Logger(file_name, "Error while adding client to database", error)
        finally:
            cursor.close()
            conn.close()

    def delete_klient_from_bd(self):
        try:
            sqlite_connection = bd.connect(basadate)
            cursor = sqlite_connection.cursor()
            cursor.execute(
                """DELETE FROM Klient WHERE Id_klient = ?""",
                (self.get_ID(),),
            )
            sqlite_connection.commit()
            logger.log_info(
                file_name, f"Client deleted from database: ID: {self.get_ID()}"
            )
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    def rename_proklient(self, name, phone, mora, email, status, klients):
        try:
            conn = bd.connect(basadate)
            cur = conn.cursor()
            if self.get_name() != name:
                for klient in klients:
                    if klient.get_name() == name:
                        message = (
                            "This element (" + self.get_name() + ") has already been"
                        )
                        raise Error.ErrorProKlient(message)
                self.name = name
                cur.execute(
                    """UPDATE Klient SET Name = ? WHERE Id_klient = ?""",
                    (self.get_name(), self.get_ID()),
                )
            if self.get_phone() != phone:
                for klient in klients:
                    if klient.get_phone() == phone:
                        message = (
                            "This element ("
                            + str(self.get_phone())
                            + ") has already been"
                        )
                        raise Error.ErrorProKlient(message)
                self.phone = phone
                cur.execute(
                    """UPDATE Klient SET Phone = ? WHERE Id_klient = ?""",
                    (self.get_phone(), self.get_ID()),
                )
            if self.get_status() != status:
                self.status = status
                cur.execute(
                    """UPDATE Klient SET Status = ? WHERE Id_klient = ?""",
                    (status, self.get_ID()),
                )
            if self.get_email() != email:
                for klient in klients:
                    if klient.get_email() == email:
                        message = (
                            "This element (" + self.get_email() + ") has already been"
                        )
                        raise Error.ErrorProKlient(message)
                self.email = email
                cur.execute(
                    """UPDATE Klient SET Mail = ? WHERE Id_klient = ?""",
                    (self.get_email(), self.get_ID()),
                )
            self.mora = mora
            conn.commit()
        except Error.ErrorProKlient as e:
            Logger(file_name, "Error renaming from Method rename_newklient", str(e))
        except bd.Error as error:
            Logger(file_name, "Error while adding client to database", error)
        finally:
            conn.close()

    def __del__(self):
        pass
