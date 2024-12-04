import Log
from Log import Logger
import sqlite3 as bd

file_name = "File Class_New_Klient"


class New_Klient:

    def __init__(self, ID, name, phone, meil):
        """
        Initialize a new New_Klient object.

        Parameters:
        ID (int): Unique identifier for the new client.
        name (str): Name of the new client.
        phone (int): Phone number of the new client.
        meil (str): Email address of the new client.

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
        self.meil = str(meil)
        self.ID = int(ID)

    # --------------------------------------------------------------------------------------------------------------------------------
    # Дополнительные функции
    def rename_newklient(self, name, phone, mail):
        """
        Renames the new client's details.

        This method updates the name, phone number, and email address of the new client.
        If the new details are different from the existing ones, the corresponding attributes are updated.

        Parameters:
        name (str): The new name of the client.
        phone (int): The new phone number of the client.
        mail (str): The new email address of the client.

        Returns:
        None
        """
        Logger(
            file_name,
            "",
            "Class New_Klient - Method rename_newklient - rename New klient",
        )
        if self.name != name:
            self.name = name

        if self.phone != phone:
            self.phone = phone

        if self.meil != mail:
            self.meil = mail

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
            meil (str): The email address of the new client.
        """
        Logger(
            file_name,
            "",
            "Class New_Klient - Method get - get information about klient",
        )
        return int(self.ID), str(self.name), int(self.phone), str(self.meil)

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

    def get_mail(self):
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
            file_name, "", "Class New_Klient - Method get_mail - get mail of New klient"
        )
        return str(self.meil)
    
    def get_ID(self):
        Logger(
            file_name, "", "Class New_Klient - Method get_mail - get mail of New klient"
        )
        return int(self.ID)

    def enter_klient_to_bd(self):
        """
        Inserts the new client's details into the database.

        This method establishes a connection to the SQLite database located at "Code\DateBase\Pc.db".
        It retrieves the status of all clients from the "Status_klient" table.
        Then, it inserts the new client's name, phone number, and email address into the "Klient_new" table.
        Finally, it commits the changes to the database.

        Parameters:
        None

        Returns:
        None
        """
        conn = bd.connect("Code\DateBase\Pc.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Status_klient")
        rows = cursor.fetchall()

        cursor.execute('''
                    INSERT INTO Klient_new (Name, Phone, Mail) VALUES(?, ?, ?)
                    ''', (str(self.name), int(self.phone), str(self.meil)))
        conn.commit()
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
