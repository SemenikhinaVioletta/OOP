import sqlite3 as bd
import b_Error as Error
from a_Global_per import basadate
from a_Log import Logger

file_name = "File Class_New_Klient"
logger = Logger(file_name, [], "Application started")


class New_Klient:
    """Represents a new klient with associated attributes and methods.

    This class encapsulates the details of a klient, including their unique identifier, name, phone number, and email address. It provides methods for updating klient information, retrieving klient data, and managing interactions with a database.

    Args:
        ID (int): The unique identifier of the klient.
        name (str): The name of the klient.
        phone (int): The phone number of the klient.
        email (str): The email address of the klient.

    Returns:
        None
    """

    def __init__(self, ID, name, phone, email):
        """
        Initialize a new instance of the New_Klient class.

        This method initializes a new klient object with the provided ID, name, phone, and email.
        It also ensures that the ID, name, phone, and email are of the correct data types.

        Parameters:
        ID (int): The unique identifier of the klient.
        name (str): The name of the klient.
        phone (int): The phone number of the klient.
        email (str): The email address of the klient.

        Returns:
        None
        """
        self.name = str(name)
        self.phone = int(phone)
        self.email = str(email)
        self.ID = int(ID)

    def rename_newklient(self, name, phone, email, klients):
        """
        Updates the name, phone, and email of the klient in the database.

        This method checks if the new name, phone, or email are unique among all klients in the database.
        If any of the new values are not unique, it raises an ErrorNewKlient exception.
        If all values are unique, it updates the corresponding fields in the database and updates the klient object.

        Parameters:
        name (str): The new name of the klient.
        phone (int): The new phone number of the klient.
        email (str): The new email address of the klient.

        Returns:
        None

        Raises:
        ErrorNewKlient: If any of the new values (name, phone, or email) are not unique among all klients.
        """
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
                    if klient.get_phone() == phone and klient.get_ID() != self.get_ID():
                        message = (
                            "This element ("
                            + str(self.get_phone())
                            + ") has already been"
                        )
                        raise Error.ErrorNewKlient(message)
                self.phone = phone
                cur.execute(
                    """UPDATE Klient_new SET Phone = ? WHERE Id_klient = ?""",
                    (self.get_phone(), self.get_ID()),
                )
            if self.get_email() != email:
                for klient in klients:
                    if klient.get_email() == email and klient.get_ID() != self.get_ID():
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
        except Error.ErrorNewKlient as e:
            Logger(file_name, "Error renaming from Method rename_newklient", str(e))
        finally:
            conn.close()

    def get(self):
        """
        Fetch klient data from the object.

        This method retrieves the ID, name, phone, and email of the klient.
        It logs the fetched data using the logger object.

        Parameters:
        None

        Returns:
        tuple: A tuple containing the ID, name, phone, and email of the klient.
        """
        logger.log_info(
            file_name,
            "Fetching klient data: "
            + f"ID: {self.ID}, Name: {self.name}, Phone: {self.phone}, Email: {self.email}",
        )
        return int(self.ID), str(self.name), int(self.phone), str(self.email)

    def get_name(self):
        """
        Retrieves the name of the klient.

        This method retrieves the name of the klient from the object's internal state.
        It logs the fetched name using the logger object.

        Parameters:
        None

        Returns:
        str: The name of the klient.
        """
        logger.log_info(file_name, "Fetching klient name: " + f"Name: {self.name}")
        return str(self.name)

    def get_phone(self):
        """
        Retrieves the phone number of the klient.

        This method retrieves the phone number of the klient from the object's internal state.
        It logs the fetched phone number using the logger object.

        Parameters:
        None

        Returns:
        int: The phone number of the klient.
        """
        logger.log_info(file_name, "Fetching klient phone: " + f"Phone: {self.phone}")
        return int(self.phone)

    def get_email(self):
        """
        Retrieves the email address of the klient.

        This method retrieves the email address of the klient from the object's internal state.
        It logs the fetched email address using the logger object.

        Parameters:
        None

        Returns:
        str: The email address of the klient.
        """
        logger.log_info(file_name, "Fetching klient email: " + f"Email: {self.email}")
        return str(self.email)

    def clear_array(self, klients):
        """
        Removes the current klient object from the 'klients' list.

        This method is used to remove the current klient object from the 'klients' list.
        It is typically called when the klient object is no longer needed or when the klient
        is being deleted from the system.

        Parameters:
        None

        Returns:
        None

        Raises:
        ValueError: If the klient object is not found in the 'klients' list.
        """
        if self in klients:
            klients.remove(self)
        else:
            raise ValueError("klient object not found in 'klients' list")

    def get_ID(self):
        """
        Retrieves the unique identifier of the klient.

        This method retrieves the ID of the klient from the object's internal state.
        It logs the fetched ID using the logger object.

        Parameters:
        None

        Returns:
        int: The unique identifier of the klient.
        """
        logger.log_info(file_name, "Fetching klient ID: " + f"ID: {self.ID}")
        return int(self.ID)

    def enter_klient_to_bd(self):
        """
        Inserts the klient's data into the SQLite database.

        This method establishes a connection to the SQLite database, retrieves the klient's data,
        and inserts it into the 'Klient_new' table. It also logs relevant information using the logger object.

        Parameters:
        None

        Returns:
        None

        Raises:
        bd.Error: If an error occurs while interacting with the SQLite database.
        """
        try:
            conn = bd.connect(basadate)
            cursor = conn.cursor()
            logger.log_info(file_name, "Connected to SQLite")
            cursor.execute("SELECT * FROM Status_klient")
            cursor.execute(
                """INSERT INTO Klient_new (Name, Phone, Mail) VALUES(?, ?, ?)""",
                (self.get_name(), self.get_phone(), self.get_email()),
            )
            conn.commit()
            logger.log_info(
                file_name,
                "klient added to database: "
                + f"Name: {self.get_name()}, Phone: {self.get_phone()}, Email: {self.get_email()}",
            )
        except bd.Error as error:
            Logger(file_name, "Error while adding klient to database", error)
        finally:
            cursor.close()
            conn.close()

    def delete_klient_from_bd(self):
        """
        Deletes the klient from the SQLite database.

        This method establishes a connection to the SQLite database, retrieves the klient's ID,
        and deletes the corresponding record from the 'Klient_new' table. It also logs relevant information
        using the logger object.

        Parameters:
        None

        Returns:
        None

        Raises:
        bd.Error: If an error occurs while interacting with the SQLite database.
        """
        try:
            sqlite_connection = bd.connect(basadate)
            cursor = sqlite_connection.cursor()
            logger.log_info(file_name, "Connected to SQLite")
            cursor.execute(
                """DELETE FROM Klient_new where Id_klient = ?""",
                (self.get_ID(),),
            )
            sqlite_connection.commit()
            logger.log_info(
                file_name, "klient deleted from database: " + f"ID: {self.get_ID()}"
            )
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
