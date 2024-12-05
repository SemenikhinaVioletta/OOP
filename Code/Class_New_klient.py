import Log
from Log import Logger
import sqlite3 as bd
import Error as Error
from Global_per import basadate, klients

file_name = "File Class_New_Klient"


class New_Klient:

    def __init__(self, ID, name, phone, email):
        """
        Initialize a new New_Klient object.

        Parameters:
        ID (int): Unique identifier for the new client.
        name (str): Name of the new client.
        phone (int): Phone number of the new client.
        email (str): email address of the new client.

        Returns:
        None
        """
        Logger(
            file_name,
            "",
            "Class New_Klient - Method __init__ - make New klient: "
            + str(ID)
            + " "
            + str(name),
        )
        self.name = str(name)
        self.phone = int(phone)
        self.email = str(email)
        self.ID = int(ID)

    # --------------------------------------------------------------------------------------------------------------------------------
    # Дополнительные функции
    def rename_newklient(self, name, phone, email):
        """
        Renames the new client"s details.

        This method updates the name, phone number, and email address of the new client.
        If the new details are different from the existing ones, the corresponding attributes are updated.

        Parameters:
        name (str): The new name of the client.
        phone (int): The new phone number of the client.
        email (str): The new email address of the client.

        Returns:
        None
        """
        Logger(
            file_name,
            "",
            "Class New_Klient - Method rename_newklient - rename New klient",
        )
        try:
            conn = bd.connect(basadate)
            cur = conn.cursor()
            if self.get_name() != name:
                for klient in klients:
                    if klient.get_name() == name and klient.get_ID() != self.get_ID():
                        message = (
                            "This element (" + self.get_name() + ") has already been"
                        )
                        raise Error.ErrorNewKlient(message)
                self.name = name
                cur.execute(
                    """UPDATE Klient_new SET Name = ? WHERE Id_klient = ?""",
                    (self.get_name(), self.get_ID()),
                )

            if self.get_phone() != phone:
                for klient in klients:
                    if klient.get_phone() == name and klient.get_ID() != self.get_ID():
                        message = (
                            "This element (" + str(self.get_phone()) + ") has already been"
                        )
                        raise Error.ErrorNewKlient(message)
                self.phone = phone
                cur.execute(
                    """UPDATE Klient_new SET Phone = ? WHERE Id_klient = ?""",
                    (self.get_phone(), self.get_ID()),
                )

            if self.get_email() != email:
                for klient in klients:
                    if klient.get_email() == name and klient.get_ID() != self.get_ID():
                        message = (
                            "This element (" + self.get_email() + ") has already been"
                        )
                        raise Error.ErrorNewKlient(message)
                self.email = email
                cur.execute(
                    """UPDATE Klient_new SET Mail = ? WHERE Id_klient = ?""",
                    (self.get_email(), self.get_ID()),
                )

            conn.commit()

        except Error.ErrorNewKlient:
            Logger(
                file_name,
                "Error renaname from Method rename_newklient",
                str(Error.ErrorNewKlient(message)),
            )
        finally:
            conn.close()

    def get(self):
        """
        Retrieves the information about the new client.

        This method returns the unique identifier, name, phone number, and email address of the new client.

        Parameters:
        None

        Returns:
        tuple: A tuple containing the following elements:
            ID (int): The unique identifier of the new client.
            name (str): The name of the new client.
            phone (int): The phone number of the new client.
            email (str): The email address of the new client.
        """
        Logger(
            file_name,
            "",
            "Class New_Klient - Method get - get information about klient",
        )
        return int(self.ID), str(self.name), int(self.phone), str(self.email)

    def get_name(self):
        """
        Retrieves the name of the new client.

        This method returns the name of the new client.

        Parameters:
        None

        Returns:
        str: The name of the new client.
        """
        Logger(
            file_name, "", "Class New_Klient - Method get_name - get name of New klient"
        )
        return str(self.name)

    def get_phone(self):
        """
        Retrieves the phone number of the new client.

        This method returns the phone number of the new client.

        Parameters:
        None

        Returns:
        int: The phone number of the new client.
        """
        Logger(
            file_name,
            "",
            "Class New_Klient - Method get_phone - get phone of New klient",
        )
        return int(self.phone)

    def get_email(self):
        """
        Retrieves the email address of the new client.

        This method returns the email address of the new client.
        It also logs a message indicating the retrieval of the email address.

        Parameters:
        None

        Returns:
        str: The email address of the new client.
        """
        Logger(
            file_name,
            "",
            "Class New_Klient - Method get_email - get email of New klient",
        )
        return str(self.email)

    def get_ID(self):
        """
        Retrieves the unique identifier of the new client.

        This method returns the unique identifier of the new client, which is used to uniquely identify the client within the system.
        It also logs a message indicating the retrieval of the client"s ID.

        Parameters:
        None

        Returns:
        int: The unique identifier of the new client.
        """
        Logger(file_name, "", "Class New_Klient - Method get_ID - get id of New klient")
        return int(self.ID)

    def enter_klient_to_bd(self):
        """
        Inserts the new client"s details into the database.

        This method establishes a connection to the SQLite database located at "Code\DateBase\Pc.db".
        It retrieves the status of all clients from the "Status_klient" table.
        Then, it inserts the new client"s name, phone number, and email address into the "Klient_new" table.
        Finally, it commits the changes to the database.

        Parameters:
        None

        Returns:
        None
        """
        conn = bd.connect(basadate)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Status_klient")

        cursor.execute(
            """INSERT INTO Klient_new (Name, Phone, Mail) VALUES(?, ?, ?)""",
            (self.get_name(), self.get_phone(), self.get_email()),
        )
        conn.commit()
        cursor.close()

    def delete_klient_from_bd(self):
        """
        Deletes the new client from the SQLite database.

        This method establishes a connection to the SQLite database located at "Code\DateBase\Pc.db".
        It then attempts to delete the new client from the "Klient_new" table using their unique identifier.
        If the deletion is successful, it logs a message indicating the successful deletion.
        If any error occurs during the process, it logs the error message.
        Finally, it closes the database connection.

        Parameters:
        None

        Returns:
        None
        """
        Logger(
            file_name,
            "",
            "Method delete_klient_from_bd - delete from list of new klient...",
        )
        try:
            sqlite_connection = bd.connect(basadate)
            cursor = sqlite_connection.cursor()
            Logger("\t", "", "connected to SQLite")

            cursor.execute(
                """DELETE FROM Klient_new where Id_klient = ?""",
                (self.get_ID(),),
            )
            sqlite_connection.commit()
            Logger("\t", "", "the entry was successfully deleted")
            cursor.close()

        except bd.Error as error:
            Logger("\t", "Error while working with SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                Logger("\t", "", "connection to SQLite closed")

    # --------------------------------------------------------------------------------------------------------------------------------

    def __del__(self):
        """
        Destructor method for the New_Klient class.

        This method is called when an instance of the New_Klient class is about to be destroyed.
        It logs a message indicating the deletion of the new client with their unique identifier.

        Parameters:
        None

        Returns:
        None
        """
        Logger(
            file_name,
            "",
            "Class New_Klient - Method __del__ - delete klient: " + str(self.ID),
        )
