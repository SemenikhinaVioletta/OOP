import d_Error as Error
from a_Log import Logger


file_name = "File Class_Produkt"
logger = Logger(file_name, [], "Application started")


class Produkt:
    def __init__(self, ID, name, mora, number):
        """
        Initialize a new instance of the Produkt class.

        Parameters:
        ID (int): The unique identifier for the product.
        name (str): The name of the product.
        mora (int): The mora associated with the product.
        number (int): The number associated with the product.

        Returns:
        None
        """
        self.name = str(name)
        self.mora = int(mora)
        self.number = int(number)
        self.ID = int(ID)

    def __del__(self):
        """
        Destructor method for the Produkt class.

        This method is called when the instance of the class is about to be destroyed.
        It does not have any parameters and does not return any value.

        The purpose of this method is to perform any necessary cleanup tasks before the object is destroyed.
        In this case, the method is currently empty and does not perform any specific actions.
        """
        pass

    def get(self):
        """
        Fetch and return the details of the client.

        This method retrieves the ID, name, mora, and number of the client from the instance attributes.
        It logs the details of the fetched client using the Logger class.

        Parameters:
        None

        Returns:
        tuple: A tuple containing the ID, name, mora, and number of the client.
        """
        logger.log_info(
            file_name,
            "Fetching klient data: "
            + f"ID: {self.ID}, Name: {self.name}, mora: {self.mora}, number: {self.number}",
        )
        return int(self.ID), str(self.name), int(self.mora), int(self.number)

    def get_name(self):
        """
        Retrieve the name of the client.

        This method retrieves the name attribute of the client instance.
        It logs the fetched name using the Logger class.

        Parameters:
        None

        Returns:
        str: The name of the client.
        """
        logger.log_info(file_name, "Fetching klient name: " + f"Name: {self.name}")
        return str(self.name)

    def get_mora(self) -> int:
        """
        Retrieve the mora value associated with the client.

        This method retrieves the mora attribute of the client instance.
        It logs the fetched mora value using the Logger class.

        Parameters:
        None

        Returns:
        int: The mora value of the client.
        """
        logger.log_info(file_name, "Fetching klient mora: " + f"mora: {self.mora}")
        return int(self.mora)

    def get_number(self) -> int:
        """
        Retrieve the number associated with the client.

        This method retrieves the number attribute of the client instance.
        It logs the fetched number value using the Logger class.

        Parameters:
        None

        Returns:
        int: The number value of the client.
        """
        logger.log_info(
            file_name, "Fetching klient number: " + f"number: {self.number}"
        )
        return int(self.number)

    def get_ID(self):
        """Retrieve the klient ID.

        This method logs the action of fetching the klient ID and returns it as an integer. It ensures that the ID is accessible for further processing or validation.

        Args:
            self: The instance of the class.

        Returns:
            int: The klient ID as an integer.
        """
        logger.log_info(file_name, "Fetching klient ID: " + f"ID: {self.ID}")
        return int(self.ID)

    def clear_array(self, klients):
        """Remove the klient from the provided list if present.

        This method checks if the klient exists in the given list and removes it. If the klient is not found, it raises a ValueError to indicate the absence.

        Args:
            self: The instance of the class.
            klients (list): The list of klient objects from which to remove the current klient.

        Raises:
            ValueError: If the klient object is not found in the "klients" list.
        """
        if self in klients:
            klients.remove(self)
        else:
            raise ValueError('klient object not found in "klients" list')


'''
    def rename_newklient(self, name, mora, number, klients):
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
            if self.get_phone() != mora:
                for klient in klients:
                    if klient.get_phone() == mora and klient.get_ID() != self.get_ID():
                        message = (
                            "This element ("
                            + str(self.get_phone())
                            + ") has already been"
                        )
                        raise Error.ErrorNewKlient(message)
                self.mora = mora
                cur.execute(
                    """UPDATE Klient_new SET mora = ? WHERE Id_klient = ?""",
                    (self.get_phone(), self.get_ID()),
                )
            if self.get_email() != number:
                for klient in klients:
                    if (
                        klient.get_email() == number
                        and klient.get_ID() != self.get_ID()
                    ):
                        message = (
                            "This element (" + self.get_email() + ") has already been"
                        )
                        raise Error.ErrorNewKlient(message)
                self.number = number
                cur.execute(
                    """UPDATE Klient_new SET Mail = ? WHERE Id_klient = ?""",
                    (self.get_email(), self.get_ID()),
                )
            conn.commit()
        except Error.ErrorNewKlient as e:
            Logger(file_name, "Error renaming from Method rename_newklient", str(e))
        finally:
            conn.close()

    def enter_klient_to_bd(self):
        try:
            conn = bd.connect(basadate)
            cursor = conn.cursor()
            logger.log_info(file_name, "Connected to SQLite")
            cursor.execute("SELECT * FROM Status_klient")
            cursor.execute(
                """INSERT INTO Klient_new (Name, mora, Mail) VALUES(?, ?, ?)""",
                (self.get_name(), self.get_phone(), self.get_email()),
            )
            conn.commit()
            logger.log_info(
                file_name,
                "klient added to database: "
                + f"Name: {self.get_name()}, mora: {self.get_phone()}, number: {self.get_email()}",
            )
        except bd.Error as error:
            Logger(file_name, "Error while adding klient to database", error)
        finally:
            cursor.close()
            conn.close()

    def delete_klient_from_bd(self):
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
'''
