import sqlite3 as bd
from a_Global_Per import database, client_statuses, contract_statuses


class Client_statuses:
    """
    Represents the status of a client with an associated ID.

    This class allows for the management of a client's ID and current status, providing methods
    to retrieve these attributes in various formats. It facilitates operations related to client
    status management within the application.

    Args:
        id (int): The unique identifier for the client.
        status (str): The current status of the client.

    Returns:
        None
    """

    def __init__(self, id, status):
        """
        Initializes a contract status with an associated ID and status.

        This constructor sets the unique identifier and the current status for the contract.
        It allows for the management of contract attributes within the application.

        Args:
            id (int): The unique identifier for the contract.
            status (str): The current status of the contract.

        Returns:
            None
        """
        self.id = id
        self.status = status

    def get(self):
        """
        Retrieves the client's ID and status as a tuple.

        This method returns the client's ID as an integer and the client's status as a string,
        providing a convenient way to access these attributes together.

        Args:
            None

        Returns:
            tuple: A tuple containing the client's ID (int) and status (str).
        """
        return int(self.id), str(self.status)

    def get_status(self):
        """
        Retrieves the status of the contract as a string.

        This method returns the current status attribute of the contract, providing a simple way
        to access this information in string format.

        Args:
            None

        Returns:
            str: The contract's status as a string.
        """
        return str(self.status)

    def get_ID(self):
        """
        Retrieves the ID of the contract as an integer.

        This method converts the contract's ID attribute to an integer type, allowing for numerical
        operations and comparisons involving the ID.

        Args:
            None

        Returns:
            int: The contract's ID as an integer.
        """
        return int(self.id)


class Contract_statues:
    """
    Represents a contract status with an associated ID and status.

    This class allows for the management of a contract's ID and its current status. It provides
    methods to retrieve the ID and status in various formats.

    Args:
        id (int): The unique identifier for the contract.
        status (str): The current status of the contract.

    Returns:
        None
    """

    def __init__(self, id, status):
        """
        Converts the client ID to an integer.

        This method allows for the conversion of the client's ID attribute to an integer type,
        facilitating operations that require numerical manipulation of the ID.

        Args:
            None

        Returns:
            int: The client's ID as an integer.
        """
        self.id = id
        self.status = status

    def get(self):
        """
        Retrieves the client's ID and status as a tuple.

        This method returns the client's ID as an integer and the client's status as a string,
        providing a convenient way to access these attributes together.

        Args:
            None

        Returns:
            tuple: A tuple containing the client's ID (int) and status (str).
        """
        return int(self.id), str(self.status)

    def get_status(self):
        """
        Retrieves the client's status as a string.

        This method returns the current status of the client, providing a simple way to access
        this attribute in string format.

        Args:
            None

        Returns:
            str: The client's status.
        """
        return str(self.status)

    def get_ID(self):
        """
        Retrieves the client's ID as an integer.

        This method returns the current ID of the client, providing a straightforward way to access
        this attribute in integer format.

        Args:
            None

        Returns:
            int: The client's ID.
        """
        return int(self.id)


def make_status():
    """
    This function connects to the SQLite database, retrieves the status data from the 'Status_Client' and 'Status_Contract' tables,
    and populates the 'client_statuses' and 'contract_statuses' lists with instances of the 'Client_statuses' and 'Contract_statues' classes respectively.

    Parameters:
    None

    Returns:
    None
    """
    conn = bd.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Status_Client")
    rows = cursor.fetchall()
    for line in rows:
        stat_Client = Client_statuses(int(line[0]), str(line[1]))
        client_statuses.append(stat_Client)
    cursor.close()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Status_Contract")
    rows = cursor.fetchall()
    for line in rows:
        stat_Contract = Contract_statues(int(line[0]), str(line[1]))
        contract_statuses.append(stat_Contract)
    cursor.close()
    conn.close()
