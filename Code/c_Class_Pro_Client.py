import b_Class_New_Client as New
import f_Class_Status_Client as Status
import sqlite3 as db
import c_Error as Error
from a_Log import Logger
from a_Global_Per import database

file_name = "File Class_Pro_Client"
logger = Logger(file_name, [], "Application started")


class Pro_Client(New.New_Client):

    def __init__(self, client_id, client_name, mora, contract, phone, email, status, client):
        self.status = status
        self.mora = mora
        self.contract = []
        self.set_contract(contract)
        if client is not None:
            self.client_id = client.client_id
            self.client_name = client.client_name
            self.phone = client.phone
            self.email = client.email
        else:
            self.client_id = client_id
            self.client_name = client_name
            self.phone = phone
            self.email = email
        self.short_name = ""
        self.make_short(self.client_name)

    def make_short(self, client_name):
        names = client_name.split()
        self.short_name = names[0] + " " + names[1][0] + ". " + names[2][0] + "."

    def set_contract(self, contract):
        contracts = list(map(int, contract.split()))
        for i in contracts:
            if i not in self.contract:
                self.contract.append(i)

    def get_client_id(self):
        return int(self.client_id)

    def get_full_name(self):
        return str(self.client_name)

    def get_short_name(self):
        return str(self.short_name)

    def get_phone(self):
        return int(self.phone)

    def get_email(self):
        return str(self.email)

    def get_status(self):
        return int(self.status)

    def get_mora(self):
        return int(self.mora)

    def get_contract_id(self):
        self.contract.sort()
        s = ""
        for i in self.contract:
            s += str(i) + " "
        return s[:-1]

    def get(self):
        return (
            self.get_client_id(),
            self.get_short_name(),
            self.get_mora(),
            self.get_phone(),
            self.get_email(),
            self.get_status(),
        )

    def enter_client_to_db(self):
        try:
            conn = db.connect(database)
            cursor = conn.cursor()
            logger.log_info(file_name, "Connected to SQLite")
            cursor.execute("SELECT * FROM Client")
            cursor.execute(
                """INSERT INTO Client (Name_Client, Short_Name, Mora, Contract_ID, Phone, Email, Status) VALUES(?, ?, ?, ?, ?, ?, ?)""",
                (
                    self.get_full_name(),
                    self.get_short_name(),
                    self.get_mora(),
                    self.get_contract_id(),
                    self.get_phone(),
                    self.get_email(),
                    self.status,
                ),
            )
            conn.commit()
            logger.log_info(
                file_name,
                "Client added to database: "
                + f"Name: {self.get_full_name()}, Phone: {self.get_phone()}, Email: {self.get_email()}",
            )
        except db.Error as error:
            logger.log_error(file_name, "Error while adding client to database: ", error)
        finally:
            cursor.close()
            conn.close()

    def delete_client_from_db(self):
        try:
            sqlite_connection = db.connect(database)
            cursor = sqlite_connection.cursor()
            cursor.execute(
                """DELETE FROM Client WHERE Client_ID = ?""",
                (self.get_client_id(),),
            )
            sqlite_connection.commit()
            logger.log_info(
                file_name, f"Client deleted from database: ID: {self.get_client_id()}"
            )
        except db.Error as error:
            logger.log_error(file_name, "Error while working with SQLite: ", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

# ... existing code ...
    def rename_client(self, client_name, client_phone, client_mora, client_email, client_status, clients):
        try:
            conn = db.connect(database)
            cur = conn.cursor()
            if self.get_full_name() != client_name:
                for client in clients:
                    if client.get_full_name() == client_name:
                        message = (
                            "This element (" + self.get_full_name() + ") has already been"
                        )
                        raise Error.ErrorProClient(message)
                self.make_short(client_name)
                self.name = client_name
                cur.execute(
                    """UPDATE Client SET Name_Client = ? WHERE Id_Client = ?""",
                    (self.get_full_name(), self.get_ID()),
                )
                cur.execute(
                    """UPDATE Client SET Short_name = ? WHERE Id_Client = ?""",
                    (self.get_short_name(), self.get_ID()),
                )
            if self.get_phone() != client_phone:
                for client in clients:
                    if client.get_phone() == client_phone:
                        message = (
                            "This element (" + str(self.get_phone()) + ") has already been"
                        )
                        raise Error.ErrorProClient(message)
                self.phone = client_phone
                cur.execute(
                    """UPDATE Client SET Phone = ? WHERE Id_Client = ?""",
                    (self.get_phone(), self.get_ID()),
                )
            if self.get_status() != client_status:
                self.status = client_status
                cur.execute(
                    """UPDATE Client SET Status = ? WHERE Id_Client = ?""",
                    (client_status, self.get_ID()),
                )
            if self.get_email() != client_email:
                for client in clients:
                    if client.get_email() == client_email:
                        message = (
                            "This element (" + self.get_email() + ") has already been"
                        )
                        raise Error.ErrorProClient(message)
                self.email = client_email
                cur.execute(
                    """UPDATE Client SET Mail = ? WHERE Id_Client = ?""",
                    (self.get_email(), self.get_ID()),
                )
            self.mora = client_mora
            conn.commit()
        except Error.ErrorProClient as e:
            Logger(file_name, "Error renaming from Method rename_client", str(e))
        except db.Error as error:
            Logger(file_name, "Error while adding client to database", error)
        finally:
            conn.close()
# ... existing code ...
