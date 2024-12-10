import sqlite3 as bd
import b_Error as Error
from a_Global_Per import database
from a_Log import Logger

file_name = "File Class_New_Client"


class New_Client:
    """Represents a new Client with associated attributes and methods.

    This class encapsulates the details of a Client, including their unique identifier, name, phone number, and email address. It provides methods for updating Client information, retrieving Client data, and managing interactions with a database.

    Args:
        ID (int): The unique identifier of the Client.
        name (str): The name of the Client.
        phone (int): The phone number of the Client.
        email (str): The email address of the Client.

    Returns:
        None
    """

    def __init__(self, ID, name, phone, email):
        """
        Initialize a new instance of the New_Client class.

        This method initializes a new Client object with the provided ID, name, phone, and email.
        It also ensures that the ID, name, phone, and email are of the correct data types.

        Parameters:
        ID (int): The unique identifier of the Client.
        name (str): The name of the Client.
        phone (int): The phone number of the Client.
        email (str): The email address of the Client.

        Returns:
        None
        """
        self.name = str(name)
        self.phone = int(phone)
        self.email = str(email)
        self.ID = int(ID)

    def rename_newClient(self, name, phone, email, Clients):
        """
        Updates the name, phone, and email of the Client in the database.

        This method checks if the new name, phone, or email are unique among all Clients in the database.
        If any of the new values are not unique, it raises an ErrorNewClient exception.
        If all values are unique, it updates the corresponding fields in the database and updates the Client object.

        Parameters:
        name (str): The new name of the Client.
        phone (int): The new phone number of the Client.
        email (str): The new email address of the Client.

        Returns:
        None

        Raises:
        ErrorNewClient: If any of the new values (name, phone, or email) are not unique among all Clients.
        """
        try:
            conn = bd.connect(database)
            cur = conn.cursor()
            if self.get_name() != name:
                for Client in Clients:
                    if Client.get_name() == name and Client.get_ID() != self.get_ID():
                        message = (
                            "This element (" + self.get_name() + ") has already been"
                        )
                        raise Error.ErrorNewClient(message)
                self.name = name
                cur.execute(
                    """UPDATE Client_new SET Name = ? WHERE Id_Client = ?""",
                    (self.get_name(), self.get_ID()),
                )
            if self.get_phone() != phone:
                for Client in Clients:
                    if Client.get_phone() == phone and Client.get_ID() != self.get_ID():
                        message = (
                            "This element ("
                            + str(self.get_phone())
                            + ") has already been"
                        )
                        raise Error.ErrorNewClient(message)
                self.phone = phone
                cur.execute(
                    """UPDATE Client_new SET Phone = ? WHERE Id_Client = ?""",
                    (self.get_phone(), self.get_ID()),
                )
            if self.get_email() != email:
                for Client in Clients:
                    if Client.get_email() == email and Client.get_ID() != self.get_ID():
                        message = (
                            "This element (" + self.get_email() + ") has already been"
                        )
                        raise Error.ErrorNewClient(message)
                self.email = email
                cur.execute(
                    """UPDATE Client_new SET Mail = ? WHERE Id_Client = ?""",
                    (self.get_email(), self.get_ID()),
                )
            conn.commit()
        except Error.ErrorNewClient as e:
            Logger(file_name, "Error renaming from Method rename_newClient", str(e))
        finally:
            conn.close()

    def get(self):
        return int(self.ID), str(self.name), int(self.phone), str(self.email)

    def get_name(self):
        return str(self.name)

    def get_phone(self):
        Logger.log_info(file_name, "Fetching Client phone: " + f"Phone: {self.phone}")
        return int(self.phone)

    def get_email(self):
        Logger.log_info(file_name, "Fetching Client email: " + f"Email: {self.email}")
        return str(self.email)

    def clear_array(self, Clients):
        if self in Clients:
            Clients.remove(self)
        else:
            raise ValueError("Client object not found in 'Clients' list")

    def get_ID(self):
        Logger.log_info(file_name, "Fetching Client ID: " + f"ID: {self.ID}")
        return int(self.ID)

    def enter_Client_to_bd(self):
        try:
            conn = bd.connect(database)
            cursor = conn.cursor()
            Logger.log_info(file_name, "Connected to SQLite")
            cursor.execute("SELECT * FROM Status_Client")
            cursor.execute(
                """INSERT INTO Client_new (Name, Phone, Mail) VALUES(?, ?, ?)""",
                (self.get_name(), self.get_phone(), self.get_email()),
            )
            conn.commit()
            Logger.log_info(
                file_name,
                "Client added to database: "
                + f"Name: {self.get_name()}, Phone: {self.get_phone()}, Email: {self.get_email()}",
            )
        except bd.Error as error:
            Logger(file_name, "Error while adding Client to database", error)
        finally:
            cursor.close()
            conn.close()

    def delete_Client_from_bd(self):
        try:
            sqlite_connection = bd.connect(database)
            cursor = sqlite_connection.cursor()
            Logger.log_info(file_name, "Connected to SQLite")
            cursor.execute(
                """DELETE FROM Client_new where Id_Client = ?""",
                (self.get_ID(),),
            )
            sqlite_connection.commit()
            Logger.log_info(
                file_name, "Client deleted from database: " + f"ID: {self.get_ID()}"
            )
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
