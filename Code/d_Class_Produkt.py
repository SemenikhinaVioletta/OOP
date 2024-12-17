import d_Error as Error
import sqlite3 as bd
from a_Log import Logger
from a_Global_Per import database, windows


file_name = "File Class_Produkt"
logger = Logger(file_name, [], "Application started")


class Produkt:
    def __init__(self, ID, name, mora, number, zakazali):
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
        self.ID = int(ID)
        self.name = str(name)
        self.mora = int(mora)
        self.number = int(number)
        self.zakazano = int(zakazali)

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
        Logger.log_info(
            file_name,
            "Fetching produkt data: "
            + f"ID: {self.ID}, Name: {self.name}, mora: {self.mora}, number: {self.number}",
        )
        return int(self.ID), str(self.name), int(self.mora), int(self.number)

    def get_all(self, flag):
        if flag == 0:
            return (
                int(self.ID),
                str(self.name),
                int(self.mora),
                int(self.number),
                int(self.zakazano),
            )
        return (
            int(self.ID),
            str(self.name),
            int(self.mora),
            int(self.number),
            int(self.zakazano) * int(self.mora),
        )

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
        Logger.log_info(file_name, "Fetching produkt name: " + f"Name: {self.name}")
        return str(self.name)

    def get_zakazano(self):
        return int(self.zakazano)

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
        Logger.log_info(file_name, "Fetching produkt mora: " + f"mora: {self.mora}")
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
        Logger.log_info(
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
        Logger.log_info(file_name, "Fetching produkt ID: " + f"ID: {self.ID}")
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

    def order(self, order):
        """
        Updates the 'In_sclad' field of the product with the given ID in the SQLite database.

        Parameters:
        order (int): The new value for the 'In_sclad' field.

        Returns:
        None

        Raises:
        Error.ErrorProduct: If an error occurs while renaming the product.
        bd.Error: If an error occurs while interacting with the SQLite database.
        """
        try:
            conn = bd.connect(database)
            cur = conn.cursor()
            cur.execute(
                """UPDATE Produkts SET In_sclad = ? WHERE Id_produkt = ?""",
                (order, self.get_ID()),
            )
            conn.commit()
            Logger.log_info(
                file_name,
                "Updated order of produkt with ID: " + f"{self.get_ID()}, to: {order}",
            )
        except Error.ErrorProduct as e:
            Logger(file_name, "Error renaming from Method rename_produkt", str(e))
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            conn.close()

    def set_zakazano(self, zakazano):
        try:
            self.zakazano += zakazano
            conn = bd.connect(database)
            cur = conn.cursor()
            cur.execute(
                """UPDATE Produkts SET Zakaz = ? WHERE Id_produkt = ?""",
                (self.zakazano, self.get_ID()),
            )
            conn.commit()
            Logger.log_info(
                file_name,
                "Updated zakazali of produkt with ID: "
                + f"{self.get_ID()}, to: {self.zakazano}",
            )
        except Error.ErrorProduct as e:
            Logger(file_name, "Error renaming from Method rename_produkt", str(e))
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            conn.close()

    def set_number(self, iterable):
        self.number += iterable

    def rename_produkt(self, name, mora, produkts):
        """
        Updates the name, mora, and number of the product in the database and in the instance attributes.

        This method connects to the SQLite database, checks if the new name already exists in the database,
        and raises an error if it does. It then updates the name, mora, and number of the product in the database
        and in the instance attributes.

        Parameters:
        name (str): The new name for the product.
        mora (int): The new mora value for the product.
        number (int): The new number value for the product.
        produkts (list): A list of Produkt objects.

        Returns:
        None

        Raises:
        Error.ErrorProduct: If the new name already exists in the database.
        """
        try:
            conn = bd.connect(database)
            cur = conn.cursor()
            if self.get_name() != name:
                for produkt in produkts:
                    if produkt.get_name() == name:
                        message = (
                            "This element (" + self.get_name() + ") has already been"
                        )
                        raise Error.ErrorProduct(message)
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
            cur.execute(
                """UPDATE Produkts SET In_sclad = ? WHERE Id_produkt = ?""",
                (self.get_number(), self.get_ID()),
            )
            cur.execute(
                """UPDATE Produkts SET Zakaz = ? WHERE Id_produkt = ?""",
                (self.get_zakazano(), self.get_ID()),
            )
            conn.commit()
        except Error.ErrorProduct as e:
            Logger(file_name, "Error renaming from Method rename_produkt", str(e))
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            conn.close()

    def enter_produkt_to_bd(self):
        """
        Inserts the current product instance into the SQLite database.

        This method establishes a connection to the SQLite database, retrieves the current product details,
        and inserts them into the "Produkts" table. It logs the successful insertion of the product into the database.

        Parameters:
        self (Produkt): The instance of the class.

        Returns:
        None

        Raises:
        bd.Error: If an error occurs while interacting with the SQLite database.
        """
        try:
            conn = bd.connect(database)
            cursor = conn.cursor()
            Logger.log_info(file_name, "Connected to SQLite")
            cursor.execute("SELECT * FROM Produkts")
            cursor.execute(
                """INSERT INTO Produkts (Name, Mora, In_sclad) VALUES(?, ?, ?)""",
                (self.get_name(), self.get_mora(), self.get_number()),
            )
            conn.commit()
            Logger.log_info(
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
        """
        Deletes the current product instance from the SQLite database.

        This method establishes a connection to the SQLite database, retrieves the ID of the current product,
        and deletes the corresponding record from the "Produkts" table. It logs the successful deletion
        of the product from the database.

        Parameters:
        self (Produkt): The instance of the class.

        Returns:
        None

        Raises:
        bd.Error: If an error occurs while interacting with the SQLite database.
        """
        try:
            sqlite_connection = bd.connect(database)
            cursor = sqlite_connection.cursor()
            Logger.log_info(file_name, "Connected to SQLite")
            cursor.execute(
                """DELETE FROM Produkts where Id_produkt = ?""",
                (self.get_ID(),),
            )
            sqlite_connection.commit()
            Logger.log_info(
                file_name, "produkt deleted from database: " + f"ID: {self.get_ID()}"
            )
        except bd.Error as error:
            Logger(file_name, "Error while working with SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
