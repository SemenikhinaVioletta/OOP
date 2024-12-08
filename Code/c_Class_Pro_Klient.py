import b_Class_New_klient as New
import f_Class_status_klient as stat
import sqlite3 as bd
import c_Error as Error
from a_Log import Logger
from a_Global_per import basadate

file_name = "File Class_Pro_Klient"
logger = Logger(file_name, [], "Application started")


class Pro_Klient(New.New_Klient):
    """Represents a professional klient with associated attributes and methods.

    This class extends the New_Klient class to manage klient information, including personal details,
    contract IDs, and methods for database interactions such as adding, deleting, and updating klient records.

    Args:
        ID (int): Unique identifier for the klient.
        name (str): Full name of the klient.
        mora (int): Amount of debt for the klient.
        kontrakt (str): Contract IDs associated with the klient, separated by spaces.
        phone (int): Phone number of the klient.
        email (str): Email address of the klient.
        status (int): Status of the klient (represented by an integer).
        klient (Pro_Klient): Optional parameter to initialize a new klient based on an existing one.

    Returns:
        None
    """

    def __init__(self, ID, name, mora, kontrakt, phone, email, status, klient):
        """
        Initialize a new instance of Pro_Klient class.

        Parameters:
        - ID (int): Unique identifier for the klient.
        - name (str): Full name of the klient.
        - mora (int): Amount of debt for the klient.
        - kontrakt (str): Contract IDs associated with the klient, separated by spaces.
        - phone (int): Phone number of the klient.
        - email (str): Email address of the klient.
        - status (int): Status of the klient (represented by an integer).
        - klient (Pro_Klient): Optional parameter to initialize a new klient based on an existing one.

        Returns:
        - None
        """
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
        """
        Generate a shortened version of a klient's full name.

        This method takes a klient's full name and generates a shortened version
        by keeping only the first name, the first letter of the middle name,
        and the first letter of the last name.

        Parameters:
        - name (str): The full name of the klient. It should be a string consisting of three words separated by spaces.

        Returns:
        - str: The shortened version of the klient's name.
        """
        names = name.split()
        self.short = names[0] + " " + names[1][0] + ". " + names[2][0] + "."

    def set_kontrakt(self, kontrakt):
        """
        Set the contracts associated with the klient.

        This method takes a string of contract IDs separated by spaces, converts them into integers,
        and adds them to the klient's contract list. If a contract ID is already present in the list,
        it is not added again.

        Parameters:
        - kontrakt (str): A string of contract IDs separated by spaces.

        Returns:
        - None
        """
        kontrakts = list(map(int, kontrakt.split()))
        for i in kontrakts:
            if i not in self.kontrakt:  # Если контракт еще не добавлен
                self.kontrakt.append(i)

    def get_ID(self):
        """
        Retrieve the unique identifier of the klient.

        This method returns the integer value representing the unique identifier of the klient.

        Parameters:
        - None

        Returns:
        - int: The unique identifier of the klient.
        """
        return int(self.ID)

    def get_full_name(self):
        """
        Retrieve the full name of the klient.

        This method returns the full name of the klient as a string. The full name is stored in the 'name' attribute of the class instance.

        Parameters:
        - None

        Returns:
        - str: The full name of the klient.
        """
        return str(self.name)

    def get_short_name(self):
        """
        Retrieve the shortened version of the klient's name.

        This method returns the shortened version of the klient's name, which is generated by keeping only the first name,
        the first letter of the middle name, and the first letter of the last name. The shortened name is stored in the 'short' attribute of the class instance.

        Parameters:
        - None

        Returns:
        - str: The shortened version of the klient's name.
        """
        return str(self.short)

    def get_phone(self):
        """
        Retrieve the phone number of the klient.

        This method returns the integer value representing the phone number of the klient.
        The phone number is stored in the 'phone' attribute of the class instance.

        Parameters:
        - None

        Returns:
        - int: The phone number of the klient.
        """
        return int(self.phone)

    def get_email(self):
        """
        Retrieve the email address of the klient.

        This method returns the email address of the klient as a string.
        The email address is stored in the 'email' attribute of the class instance.

        Parameters:
        - None

        Returns:
        - str: The email address of the klient.
        """
        return str(self.email)

    def get_status(self):
        """
        Retrieve the status of the klient.

        This method returns the integer value representing the status of the klient.
        The status is stored in the 'status' attribute of the class instance.

        Parameters:
        - None

        Returns:
        - int: The status of the klient. The status is represented by an integer.
        """
        return int(self.status)

    def get_mora(self):
        """
        Retrieve the debt amount of the klient.

        This method returns the integer value representing the debt amount of the klient.
        The debt amount is stored in the 'mora' attribute of the class instance.

        Parameters:
        - None

        Returns:
        - int: The debt amount of the klient.
        """
        return int(self.mora)

    def get_kontrakt_id(self):
        """
        Retrieve the contract IDs associated with the klient, sorted in ascending order.

        This method retrieves the contract IDs associated with the klient from the 'kontrakt' attribute,
        sorts them in ascending order, and returns them as a string with each ID separated by a space.

        Parameters:
        - None

        Returns:
        - str: A string of contract IDs, separated by spaces, sorted in ascending order.
        """
        self.kontrakt.sort()
        s = ""
        for i in self.kontrakt:
            s += str(i) + " "
        return s[:-1]

    def get(self):
        """
        Retrieve all relevant klient information in a tuple.

        This method returns a tuple containing the unique identifier, shortened name, debt amount,
        phone number, email address, and status of the klient. The information is obtained by calling
        the respective getter methods for each attribute.

        Parameters:
        - None

        Returns:
        - tuple: A tuple containing the following elements:
            - int: The unique identifier of the klient.
            - str: The shortened version of the klient's name.
            - int: The debt amount of the klient.
            - int: The phone number of the klient.
            - str: The email address of the klient.
            - int: The status of the klient. The status is represented by an integer.
        """
        return (
            self.get_ID(),
            self.get_short_name(),
            self.get_mora(),
            self.get_phone(),
            self.get_email(),
            self.get_status(),
        )

    def enter_klient_to_pro_bd(self):
        """
        This method attempts to add the current klient instance to the SQLite database.

        The method establishes a connection to the SQLite database, retrieves the necessary data from the klient instance,
        and inserts a new record into the 'Klient' table. The method logs relevant information using the Logger class.

        Parameters:
        - self: The instance of the class.

        Returns:
        - None

        Raises:
        - bd.Error: If an error occurs while interacting with the SQLite database.
        """
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
        Delete the current klient instance from the SQLite database.

        This method attempts to delete the klient record associated with the current instance from the SQLite database.
        It establishes a connection to the SQLite database, executes a DELETE query based on the klient's unique identifier,
        and commits the changes. If an error occurs during the process, it logs the error using the Logger class.

        Parameters:
        - self: The instance of the class.

        Returns:
        - None

        Raises:
        - bd.Error: If an error occurs while interacting with the SQLite database.
        """
        try:
            sqlite_connection = bd.connect(basadate)
            cursor = sqlite_connection.cursor()
            cursor.execute(
                """DELETE FROM Klient WHERE Id_klient = ?""",
                (self.get_ID(),),
            )
            sqlite_connection.commit()
            logger.log_info(
                file_name, f"klient deleted from database: ID: {self.get_ID()}"
            )
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    def rename_proklient(self, name, phone, mora, email, status, klients):
        """
        This method updates the klient's information in the SQLite database.

        The method checks if the new name, phone, email, or status are different from the current values.
        If any of these values are changed, it updates the corresponding fields in the 'Klient' table in the SQLite database.
        It also ensures that the new name, phone, and email are not already associated with other klients.

        Parameters:
        - name (str): The new name of the klient.
        - phone (int): The new phone number of the klient.
        - mora (int): The new debt amount of the klient.
        - email (str): The new email address of the klient.
        - status (int): The new status of the klient.
        - klients (list): A list of all existing klient instances.

        Returns:
        - None

        Raises:
        - Error.ErrorProKlient: If the new name, phone, or email are already associated with other klients.
        - bd.Error: If an error occurs while interacting with the SQLite database.
        """
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
            Logger(file_name, "Error while adding klient to database", error)
        finally:
            conn.close()

    def __del__(self):
        """
        Destructor method for the Pro_Klient class.

        This method is called when an instance of the Pro_Klient class is about to be destroyed.
        Currently, it does nothing, but it can be used to perform any necessary cleanup tasks, such as releasing resources or closing connections.

        Parameters:
        - self: The instance of the class.

        Returns:
        - None
        """
        pass
