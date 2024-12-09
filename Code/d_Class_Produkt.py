import d_Error as Error
import sqlite3 as bd
from a_Log import Logger
from a_Global_per import basadate, windows



file_name = "File Class_Produkt"
logger = Logger(file_name, [], "Application started")


class Produkt:
    def __init__(self, ID, name, mora, number):
        """
        Initialize a new instance of the Produkts class.

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
        Destructor method for the Produkts class.

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
            "Fetching produkt data: "
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
        logger.log_info(file_name, "Fetching produkt name: " + f"Name: {self.name}")
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
        logger.log_info(file_name, "Fetching produkt mora: " + f"mora: {self.mora}")
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
            file_name, "Fetching produkt number: " + f"number: {self.number}"
        )
        return int(self.number)

    def get_ID(self):
        """Retrieve the produkt ID.

        This method logs the action of fetching the produkt ID and returns it as an integer. It ensures that the ID is accessible for further processing or validation.

        Args:
            self: The instance of the class.

        Returns:
            int: The produkt ID as an integer.
        """
        logger.log_info(file_name, "Fetching produkt ID: " + f"ID: {self.ID}")
        return int(self.ID)

    def clear_array(self, produkts):
        """Remove the produkt from the provided list if present.

        This method checks if the produkt exists in the given list and removes it. If the produkt is not found, it raises a ValueError to indicate the absence.

        Args:
            self: The instance of the class.
            produkts (list): The list of produkt objects from which to remove the current produkt.

        Raises:
            ValueError: If the produkt object is not found in the "produkts" list.
        """
        if self in produkts:
            produkts.remove(self)
        else:
            raise ValueError('produkt object not found in "produkts" list')


    def rename_produkt(self, name, mora, number, produkts):
        try:
            conn = bd.connect(basadate)
            cur = conn.cursor()
            if self.get_name() != name:
                for produkt in produkts:
                    if produkt.get_name() == name:
                        message = (
                            "This element (" + self.get_name() + ") has already been"
                        )
                        raise Error.ErrorProdukt(message)
                self.name = name
                cur.execute(
                    """UPDATE Produkts SET Name = ? WHERE Id_produkt = ?""",
                    (self.get_name(), self.get_ID()),
                )
            if self.get_mora() != mora:
                self.mora = mora
                cur.execute(
                    """UPDATE Produkts SET Mora = ? WHERE Id_produkt = ?""",
                    (self.get_mora(), self.get_ID()),
                )
            if self.get_number() != number:
                self.number = number
                cur.execute(
                    """UPDATE Produkts SET In_sclad = ? WHERE Id_produkt = ?""",
                    (self.get_number(), self.get_ID()),
                )
            conn.commit()
        except Error.ErrorProdukt as e:
            Logger(file_name, "Error renaming from Method rename_produkt", str(e))
        finally:
            conn.close()

    def enter_produkt_to_bd(self):
        try:
            conn = bd.connect(basadate)
            cursor = conn.cursor()
            logger.log_info(file_name, "Connected to SQLite")
            cursor.execute("SELECT * FROM Produkts")
            cursor.execute(
                """INSERT INTO Produkts (Name, Mora, In_sclad) VALUES(?, ?, ?)""",
                (self.get_name(), self.get_mora(), self.get_number()),
            )
            conn.commit()
            logger.log_info(
                file_name,
                "produkt added to database: "
                + f"Name: {self.get_name()}, mora: {self.get_mora()}, number: {self.get_number()}",
            )
        except bd.Error as error:
            Logger(file_name, "Error while adding produkt to database", error)
        finally:
            cursor.close()
            conn.close()

    def delete_produkt_from_bd(self):
        try:
            sqlite_connection = bd.connect(basadate)
            cursor = sqlite_connection.cursor()
            logger.log_info(file_name, "Connected to SQLite")
            cursor.execute(
                """DELETE FROM Produkts where Id_produkt = ?""",
                (self.get_ID(),),
            )
            sqlite_connection.commit()
            logger.log_info(
                file_name, "produkt deleted from database: " + f"ID: {self.get_ID()}"
            )
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

