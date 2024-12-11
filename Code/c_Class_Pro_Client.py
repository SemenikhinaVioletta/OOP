import b_Class_New_Client as New
import f_Class_Status_Client as Status
import sqlite3 as db
import c_Error as Error
from a_Log import Logger
from a_Global_Per import database

file_name = "File Class_Pro_Client"
logger = Logger(file_name, [], "Application started")


class Pro_Client(New.New_Client):
    """
    Represents a professional client, inheriting from the New_Client class.

    This class extends the functionality of the New_Client class to include additional 
    attributes and methods specific to professional clients. It allows for the management 
    of pro client-specific data and behaviors.

    Args:
        New.New_Client: Inherits attributes and methods from the New_Client class.
    """
    
    def __init__(self, client_id, client_name, mora, contract, phone, email, status, client):
        """
        Initializes a new instance of the Pro_Client class.

        Parameters:
        client_id (int): The unique identifier of the client.
        client_name (str): The full name of the client.
        mora (int): The mora status of the client.
        contract (str): A string containing contract IDs separated by spaces.
        phone (int): The phone number of the client.
        email (str): The email of the client.
        status (int): The status of the client.
        client (Pro_Client): An optional parameter representing another instance of the Pro_Client class.
                             If provided, the attributes of the current instance will be updated with the values
                             from the provided client instance.

        Returns:
        None

        The function initializes the attributes of the Pro_Client instance, including the status, mora, contract,
        ID, name, phone, email, short_name, and calls the make_short method to create the shortened version of the client's
        full name.
        """
        self.status = status
        self.mora = mora
        self.contract = []
        self.set_contract(contract)
        if client is not None:
            self.ID = client.ID
            self.name = client.name
            self.phone = client.phone
            self.email = client.email
        else:
            self.ID = client_id
            self.name = client_name
            self.phone = phone
            self.email = email
        self.short_name = ""
        self.make_short(self.name)

    def make_short(self, client_name):
        """
        Creates a shortened version of the client's full name.

        This function takes a full name as input, splits it into individual names, and constructs a shortened version
        by taking the first name, the first character of the middle name, and the first character of the last name,
        followed by a dot.

        Parameters:
        client_name (str): The full name of the client. The name should be a string consisting of three space-separated
                           names (first name, middle name, and last name).

        Returns:
        None

        The function modifies the 'short_name' attribute of the client instance.
        """
        names = client_name.split()
        self.short_name = names[0] + " " + names[1][0] + ". " + names[2][0] + "."

    def set_contract(self, contract):
        """
        Parses and sets the contract IDs for the client.

        This function takes a string of contract IDs separated by spaces, converts them to integers,
        and adds them to the client's contract list if they are not already present.

        Parameters:
        contract (str): A string containing contract IDs separated by spaces.

        Returns:
        None

        The function modifies the 'contract' attribute of the client instance.
        """
        contracts = list(map(int, contract.split()))
        for i in contracts:
            if i not in self.contract:
                self.contract.append(i)

    def get_client_id(self):
        """
        Returns the unique identifier of the client.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        int: The unique identifier of the client.
        """
        return int(self.ID)

    def get_full_name(self):
        """
        Returns the full name of the client.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        str: The full name of the client.
        """
        return str(self.name)

    def get_short_name(self):
        """
        Returns the shortened version of the client's full name.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        str: The shortened version of the client's full name. The shortened name is constructed by taking the first
             name, the first character of the middle name, and the first character of the last name, followed by a dot.
             For example, if the full name is "John Smith Doe", the shortened name would be "J. S. D.".
        """
        return str(self.short_name)

    def get_phone(self):
        """
        Returns the phone number of the client.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        int: The phone number of the client.
        """
        return int(self.phone)

    def get_email(self):
        """
        Returns the email of the client.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        str: The email of the client.
        """
        return str(self.email)

    def get_status(self):
        """
        Returns the current status of the client.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        int: The status of the client. The value represents the status, where 0 indicates a certain status,
             1 indicates another status, and so on.
        """
        return int(self.status)

    def get_mora(self):
        """
        Returns the mora status of the client.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        int: The mora status of the client. The value represents the mora status, where 0 indicates no mora,
             1 indicates mora, and so on.
        """
        return int(self.mora)

    def get_contract_id(self):
        """
        Returns a string representation of the client's contract IDs, sorted in ascending order.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        str: A string containing the client's contract IDs separated by spaces.
        """
        self.contract.sort()
        s = ""
        for i in self.contract:
            s += str(i) + " "
        return s[:-1]

    def get(self):
        """
        Returns a tuple containing the client's ID, short name, mora status, phone number, email, and status.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        tuple: A tuple containing the client's ID, short name, mora status, phone number, email, and status.
        """
        return (
            self.get_client_id(),
            self.get_short_name(),
            self.get_mora(),
            self.get_phone(),
            self.get_email(),
            self.get_status(),
        )

    def enter_client_to_db(self):
        """
        Inserts the client's information into the SQLite database.

        Parameters:
        self (Pro_Client): The instance of the class.

        Returns:
        None

        Raises:
        db.Error: If there is an error while connecting to the database or executing SQL queries.

        The function connects to the SQLite database, executes an INSERT query to add the client's information,
        commits the changes, and logs the successful addition. If an error occurs during the process, it logs the error.
        Finally, it ensures the database connection is closed.
        """
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
        """
        Deletes the client from the database based on the client's ID.

        Parameters:
        None

        Returns:
        None

        Raises:
        db.Error: If there is an error while connecting to the database or executing SQL queries.

        The function connects to the SQLite database, executes a DELETE query to remove the client with the current ID,
        commits the changes, and logs the successful deletion. If an error occurs during the process, it logs the error.
        Finally, it ensures the database connection is closed.
        """
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

    def rename_client(self, client_name, client_phone, client_mora, client_email, client_status, clients):
        """
        This function renames a client in the database and updates its attributes.

        Parameters:
        client_name (str): The new full name of the client.
        client_phone (int): The new phone number of the client.
        client_mora (int): The new mora status of the client.
        client_email (str): The new email of the client.
        client_status (int): The new status of the client.
        clients (list): A list of all clients to check for duplicates.

        Returns:
        None

        Raises:
        Error.ErrorProClient: If the new name, phone, or email already exists in the database.
        db.Error: If there is an error while connecting to the database or executing SQL queries.
        """
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
