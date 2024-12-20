import sqlite3 as db
import c_Class_Pro_Client as pro
import datetime as t
from datetime import date
from a_Log import Logger
from a_Global_Per import database
from d_Produkt import produkts
from c_proClient import pro_client
from f_Class_Status_Client import contract_statuses

file_name = "File Class_Contract"
logger = Logger(file_name, [], "Application started")
Data = date.today()


class Contract:
    """
    A comprehensive class representing a contract with detailed management and database interaction capabilities.

    The Contract class provides methods for creating, updating, retrieving, and managing contract information, including client association, product management, and database operations.

    Attributes:
        ID (int): Unique identifier for the contract.
        status (ContractStatus): Current status of the contract.
        data_start (date): Start date of the contract.
        data_end (date): End date of the contract.
        client (ProClient): Professional client associated with the contract.
        products (list): List of products included in the contract.
        mora (int): Total mora value of the contract.

    Methods:
        Getter and setter methods for contract attributes
        Database interaction methods for inserting, updating, and deleting contracts
        Methods for managing associated clients and products
        Methods for calculating and updating contract details
    """

    def __init__(self, ID, status, data_start, data_end, products, Mora, ID_klient):
        """
        Initializes a new instance of the Contract class.

        Parameters:
        ID (int): The unique identifier of the contract.
        status (int): The status of the contract (represented by an ID).
        data_start (str): The start date of the contract in 'YYYY-MM-DD' format.
        data_end (str): The end date of the contract in 'YYYY-MM-DD' format.
        products (str): A space-separated string of product IDs associated with the contract.
        Mora (int): The total mora associated with the contract.
        ID_klient (int): The unique identifier of the client associated with the contract.

        Returns:
        None
        """
        self.client = pro.Pro_Client(0, "- - -", 0, "", 0, "", 1, None)
        if ID_klient != 0:
            self.set_client(ID_klient)
        self.ID = ID
        start = str(data_start).split("-")
        end = str(data_end).split("-")
        self.data_start = date(int(start[0]), int(start[1]), int(start[2].split()[0]))
        self.data_end = date(int(end[0]), int(end[1]), int(end[2].split()[0]))
        if Data > self.data_end and status != 2:
            self.set_status(3)
        else:
            self.set_status(status)
        self.update_status()
        array = set_products(products)
        self.products = array
        self.mora = Mora

    def update_status(self):
        """
        Updates the contract's status and end date in the database.

        This method establishes a database connection, updates the contract's status and end date for the specific contract ID, and then closes the database connection.

        Returns:
            None
        """
        conn = db.connect(database)
        cursor = conn.cursor()
        logger.log_info(file_name, "Connected to SQLite")
        cursor.execute("SELECT * FROM Contracts")
        cursor.execute(
            """UPDATE Contracts SET Status = ? WHERE ID_contract= ?""",
            (self.get_status(), self.get_ID()),
        )
        cursor.execute(
            """UPDATE Contracts SET Data_End = ? WHERE ID_contract= ?""",
            (self.get_data_end(), self.get_ID()),
        )
        conn.commit()
        cursor.close()
        conn.close()

    def set_client(self, ID_klient):
        """
        Sets the client associated with the contract.

        This method iterates through the 'client' list to find a matching client ID.
        If a match is found, the corresponding client is assigned to the contract's 'client' attribute.

        Parameters:
        ID_klient (int): The unique identifier of the client to be associated with the contract.

        Returns:
        None
        """
        for id in pro_client:
            if ID_klient == id.get_ID():
                self.client = id
                break

    def set_data_end(self, today):
        """
        Sets the contract's end date to the provided date.

        This method updates the contract's end date attribute with the specified date value.

        Args:
            today (date): The date to be set as the contract's end date.

        Returns:
            None
        """

        self.data_end = today

    def set_status(self, status):
        """
        Sets the contract status by matching the provided status ID with available contract statuses.

        This method searches through the list of contract statuses to find and assign the matching status object to the contract.

        Args:
            status (int): The unique identifier of the contract status to be set.

        Returns:
            None
        """

        for stat in contract_statuses:
            if stat.get_ID() == status:
                self.status = stat
                break

    def set_mora(self):
        """
        Calculates the total mora value for the contract by summing the mora values of all associated products.

        This method iterates through the contract's product list, accumulating the individual product mora values to determine the total contract mora.

        Returns:
            None
        """
        self.mora = 0
        for produkt in self.products:
            self.mora += produkt.get_mora()

    def add_product(self, produkt):
        """
        Adds a product to the contract's product list and updates the total mora.

        This method appends the provided product to the contract's product list and
        updates the total mora by adding the mora of the added product.

        Parameters:
        produkt (Product): The product object to be added to the contract's product list.

        Returns:
        None
        """
        self.products.append(produkt)
        self.mora += produkt.get_mora()

    def remove_product(self, produkt):
        """
        Removes a product from the contract's product list.

        This method removes the specified product from the contract's product list.
        If the product is not found in the list, no action is taken.

        Parameters:
        produkt (Product): The product object to be removed from the contract's product list.

        Returns:
        None
        """
        self.products.remove(produkt)

    def get_ID(self):
        """
        Retrieves the unique identifier of the contract.

        This method returns the unique identifier of the contract, which is stored in the 'ID' attribute.
        The 'ID' attribute is expected to be an integer.

        Parameters:
        None

        Returns:
        int: The unique identifier of the contract.
        """
        return int(self.ID)

    def get_status(self):
        """
        Retrieves the status ID of the contract.

        This method returns the status ID associated with the contract.
        The status ID is obtained by calling the 'get_ID' method of the 'status' attribute.

        Parameters:
        None

        Returns:
        int: The status ID of the contract.
        """
        return self.status.get_ID()

    def get_client_id(self):
        """
        Retrieves the unique identifier of the client associated with the contract.

        If the contract does not have an associated client (i.e., the 'client' attribute is set to 0),
        this method returns 0. Otherwise, it calls the 'get_ID' method of the 'client' attribute
        to retrieve the client's unique identifier.

        Parameters:
        None

        Returns:
        int: The unique identifier of the client associated with the contract.
             If no client is associated, returns 0.
        """
        if self.client == 0:
            return 0
        return self.client.get_ID()

    def get_client_name(self):
        """
        Retrieves the name of the client associated with the contract.

        This method retrieves the name of the client associated with the contract by calling the 'get_name' method
        of the 'client' attribute.

        Parameters:
        None

        Returns:
        str: The name of the client associated with the contract.
        """
        return self.client.get_name()

    def get_produkts(self):
        """
        Retrieves a formatted string of product details associated with the contract.

        This method iterates through the 'products' list and constructs a string containing
        the product IDs and names, separated by spaces and newlines. The trailing newline is removed.

        Parameters:
        None

        Returns:
        str: A formatted string containing the product IDs and names, separated by spaces and newlines.
             The string does not include the trailing newline.
        """
        produkts = ""
        for produkt in self.products:
            produkts += str(produkt.get_ID()) + " " + produkt.get_name() + "\n"
        return produkts[:-1]

    def get_produkts_to_bd(self):
        """
        Retrieves a string representation of product IDs associated with the contract for database storage.

        This method iterates through the 'products' list and concatenates the product IDs into a single string,
        separated by spaces. The resulting string is then returned, excluding the trailing space.

        Parameters:
        None

        Returns:
        str: A string containing space-separated product IDs associated with the contract.
        """
        produkts = ""
        for produkt in self.products:
            produkts += str(produkt.get_ID()) + " "
        return produkts[:-1]

    def get_mora(self):
        """
        Retrieves the total mora associated with the contract.

        This method returns the mora value associated with the contract.
        The mora is calculated based on the sum of moras of all products associated with the contract.

        Parameters:
        None

        Returns:
        int: The total mora associated with the contract.
        """
        return int(self.mora)

    def get_data_start(self):
        """
        Returns the start date of the contract.

        This method retrieves the start date of the contract from the instance variable 'data_start'.

        Parameters:
        None

        Returns:
        str: The start date of the contract in 'YYYY-MM-DD' format.
        """
        return str(self.data_start)

    def get_rial_data_start(self):
        """
        Retrieves the start date of the contract in a specific format.

        This method retrieves the start date of the contract from the instance variable 'data_start'
        and returns it in the original format (date object).

        Parameters:
        None

        Returns:
        date: The start date of the contract in a date object format.
        """
        return self.data_start

    def get_rial_data_end(self):
        """
        Retrieves the end date of the contract in a specific format.

        This method retrieves the end date of the contract from the instance variable 'data_end'
        and returns it in the original format (date object).

        Parameters:
        None

        Returns:
        date: The end date of the contract in a date object format.
        """
        return self.data_end

    def get_data_end(self):
        """
        Returns the end date of the contract.

        This method retrieves the end date of the contract from the instance variable 'data_end'.

        Parameters:
        None

        Returns:
        str: The end date of the contract in 'YYYY-MM-DD' format.
        """
        return str(self.data_end)

    def get(self):
        """
        Retrieves specific contract information as a tuple.

        This method returns a tuple containing the contract ID, status, client name, end date, and mora.

        Parameters:
        None

        Returns:
        tuple: A tuple containing the following elements:
               - Contract ID (int)
               - Contract status (str)
               - Client name (str)
               - Contract end date (str)
               - Contract mora (int)
        """
        return (
            int(self.ID),
            self.status.get_status(),
            self.get_client_name(),
            self.get_data_end(),
            self.get_mora(),
        )

    def get_all(self):
        """
        Retrieves all relevant contract information.

        This method returns a tuple containing various attributes of the contract instance.
        The returned tuple includes the contract ID, status, client name, start date, end date, and mora.

        Parameters:
        None

        Returns:
        tuple: A tuple containing the following elements:
               - Contract ID (int)
               - Contract status (str)
               - Client name (str)
               - Contract start date (str)
               - Contract end date (str)
               - Contract mora (int)
        """
        return (
            int(self.ID),
            self.status.get_status(),
            self.get_client_name(),
            self.get_data_start(),
            self.get_data_end(),
            self.get_mora(),
        )

    def set_clients(self, ID):
        """
        Sets the client associated with the contract based on the provided ID.

        This method iterates through the 'pro_client' list to find a client with a matching ID.
        If a match is found, the corresponding client is assigned to the contract's 'client' attribute.
        If no matching client is found, a ValueError is raised with an appropriate error message.

        Parameters:
        ID (int): The unique identifier of the client to be associated with the contract.

        Returns:
        None

        Raises:
        ValueError: If no client with the provided ID is found in the 'pro_client' list.
        """
        flag = True
        try:
            if len(pro_client) > 0:
                id = pro_client[0]
                for id in pro_client:
                    if ID == id.get_ID():
                        self.client = id
                        flag = False
                        break
            if flag:
                message = "No client with this ID found in table"
                raise ValueError(message)
        except Exception as e:
            logger.log_error(
                file_name, "An error occurred during ID validation", str(e)
            )

    def add_to_bd(self):
        """
        Adds the current contract to the SQLite database.

        This method connects to the SQLite database, executes an INSERT query to add the contract's details,
        and logs relevant information using the Logger object.

        Parameters:
        None

        Returns:
        None

        Raises:
        db.Error: If an error occurs while connecting to the database or executing the query.
        """
        try:
            conn = db.connect(database)
            cursor = conn.cursor()
            logger.log_info(file_name, "Connected to SQLite")
            cursor.execute("SELECT * FROM Contracts")
            cursor.execute(
                """INSERT INTO Contracts (Status, Data_start, Data_End, Produkts, Mora, ID_klient) VALUES(?, ?, ?, ?, ?, ?)""",
                (
                    self.get_status(),
                    self.get_data_start(),
                    self.get_data_end(),
                    self.get_produkts_to_bd(),
                    self.get_mora(),
                    self.get_client_id(),
                ),
            )
            conn.commit()
            logger.log_info(
                file_name,
                "Client added to database: " + f"Name: {str(self.get_ID())}",
            )
        except db.Error as error:
            logger.log_error(
                file_name, "Error while adding client to database: ", error
            )
        finally:
            cursor.close()
            conn.close()

    def delete_contract_from_bd(self):
        """
        Deletes the current contract from the database and updates the associated client's contract list.

        This method connects to the SQLite database, executes a DELETE query to remove the contract with the current ID,
        and then iterates through the 'pro_client' list to find and remove the current contract from the associated client's contract list.
        It also updates the client's contract ID in the 'Client' table.
        If any errors occur during the database operations, they are logged using the 'logger' object.

        Parameters:
        None

        Returns:
        None
        """
        try:
            sqlite_connection = db.connect(database)
            cursor = sqlite_connection.cursor()
            cursor.execute(
                """DELETE FROM Contracts WHERE ID_contract = ?""",
                (self.get_ID(),),
            )
            for client in pro_client:
                for cont in client.contract:
                    if cont.get_ID() == self.get_ID():
                        client.contract.remove(cont)
                        cursor.execute(
                            """UPDATE Client SET Contract_id = ? WHERE Id_Client= ?""",
                            (client.get_contract_id(), cont.get_ID()),
                        )
            logger.log_info(
                file_name, f"Client deleted from database: ID: {self.get_client_id()}"
            )
            sqlite_connection.commit()
        except db.Error as error:
            logger.log_error(file_name, "Error while working with SQLite: ", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    def __del__(self):
        """
        Destructor method for the Contract class.

        This method is called when an instance of the Contract class is about to be destroyed.
        It is responsible for performing any necessary cleanup tasks, such as releasing resources or closing connections.

        Parameters:
        None

        Returns:
        None
        """
        pass


def set_products(products):
    """
    This function takes a list of product IDs as input and returns a list of corresponding Product objects.

    Parameters:
    products (list): A list of strings representing product IDs. Each string is expected to be a valid integer.

    Returns:
    list: A list of Product objects. The length of the list will be equal to the length of the input 'products' list.
          If a product with a given ID is not found in the 'produkts' list, the corresponding position in the output list will be None.
    """
    array = []
    for id in products:
        for produkt in produkts:
            if int(id) == produkt.get_ID():
                array.append(produkt)
                break
    return array
