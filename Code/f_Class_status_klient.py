import sqlite3 as bd
from a_Global_per import basadate, status_klient, status_kontrakt


class status_Klient:
    """
    A class representing a client status.

    Attributes
    ----------
    id : int
        The unique identifier of the client status.
    status : str
        The description of the client status.

    Methods
    -------
    get()
        Returns the client status ID and description as a tuple.
    get_status()
        Returns the description of the client status.
    get_ID()
        Returns the unique identifier of the client status.
    """

    def __init__(self, id, status):
        """
        Constructs all the necessary attributes for the status_Klient class.

        Parameters
        ----------
        id : int
            The unique identifier of the client status.
        status : str
            The description of the client status.
        """
        self.id = id
        self.status = status

    def get(self):
        """
        Returns the client status ID and description as a tuple.

        Returns
        -------
        tuple
            A tuple containing the client status ID and description.
        """
        return int(self.id), str(self.status)

    def get_status(self):
        """
        Returns the description of the client status.

        Returns
        -------
        str
            The description of the client status.
        """
        return str(self.status)

    def get_ID(self):
        """
        Returns the unique identifier of the client status.

        Returns
        -------
        int
            The unique identifier of the client status.
        """
        return int(self.id)


class status_Kontrakt:
    """Represents a contract status for a client.

    This class encapsulates the unique identifier and status of a client, providing methods to retrieve this information. It serves as a simple data structure to manage client contract statuses effectively.

    Args:
        id (int): The unique identifier for the client.
        status (str): The status of the client.

    Returns:
        None
    """

    def __init__(self, id, status):
        """Initializes a new client with a unique identifier and status.

        This constructor sets up the client object by assigning the provided ID and status. It ensures that each client has a unique identifier and a corresponding status upon creation.

        Args:
            id (int): The unique identifier for the client.
            status (str): The status of the client.

        Returns:
            None
        """
        self.id = id
        self.status = status

    def get(self):
        """Retrieves all relevant information about the client.

        This method collects and returns a tuple containing the client's unique identifier, name, debt amount, phone number, email address, and status. It provides a convenient way to access all essential client details in a single call.

        Args:
            None

        Returns:
            tuple: A tuple containing the following elements:
                - int: The unique identifier of the client.
                - str: The name of the client.
                - int: The debt amount of the client.
                - int: The phone number of the client.
                - str: The email address of the client.
                - int: The status of the client.
        """
        return int(self.id), str(self.status)

    def get_status(self):
        """Retrieves the status of the client.

        This method returns the current status of the client as a string. It provides a simple way to access the client's status information.

        Args:
            None

        Returns:
            str: The status of the client.
        """
        return str(self.status)

    def get_ID(self):
        """Retrieves the unique identifier of the client.

        This method returns the client's ID as an integer. It provides a straightforward way to access the unique identifier associated with the client.

        Args:
            None

        Returns:
            int: The unique identifier of the client.
        """
        return int(self.id)


def make_status():
    """
    This function connects to the SQLite database, retrieves status data from the 'Status_klient' and 'Status_kontrakt' tables,
    and creates instances of the 'status_Klient' and 'status_Kontrakt' classes with the retrieved data.

    Parameters:
    None

    Returns:
    None
    """
    conn = bd.connect(basadate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Status_klient")
    rows = cursor.fetchall()
    for line in rows:
        stat_klient = status_Klient(int(line[0]), str(line[1]))
        status_klient.append(stat_klient)
    cursor.close()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Status_kontrakt")
    rows = cursor.fetchall()
    for line in rows:
        stat_kontrakt = status_Kontrakt(int(line[0]), str(line[1]))
        status_kontrakt.append(stat_kontrakt)
    cursor.close()
    conn.close()
