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
        conn = db.connect(database)
        cursor = conn.cursor()
        logger.log_info(file_name, "Connected to SQLite")
        cursor.execute("SELECT * FROM Contracts")
        cursor.execute(
            """UPDATE Contracts SET Status = ? WHERE ID_contract= ?""",
            (self.get_status(), self.get_ID()),
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

    def set_status(self, status):
        for stat in contract_statuses:
            if stat.get_ID() == status:
                self.status = stat
                break

    def set_mora(self):
        self.mora = 0
        for produkt in self.products:
            self.mora += produkt.get_mora()

    def add_product(self, produkt):
        self.products.append(produkt)
        self.mora += produkt.get_mora()

    def remove_product(self, produkt):
        self.products.remove(produkt)

    def get_ID(self):
        return int(self.ID)

    def get_status(self):
        return self.status.get_ID()

    def get_client_id(self):
        if self.client == 0:
            return 0
        return self.client.get_ID()

    def get_client_name(self):
        return self.client.get_name()

    def get_produkts(self):
        produkts = ""
        for produkt in self.products:
            produkts += str(produkt.get_ID()) + " " + produkt.get_name() + "\n"
        return produkts[:-1]

    def get_produkts_to_bd(self):
        produkts = ""
        for produkt in self.products:
            produkts += str(produkt.get_ID()) + " "
        return produkts[:-1]

    def get_mora(self):
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
        return self.data_start

    def get_rial_data_end(self):
        return self.data_end

    def get_data_end(self):
        return str(self.data_end)

    def get(self):
        return (
            int(self.ID),
            self.status.get_status(),
            self.get_client_name(),
            self.get_data_end(),
            self.get_mora(),
        )

    def get_all(self):
        return (
            int(self.ID),
            self.status.get_status(),
            self.get_client_name(),
            self.get_data_start(),
            self.get_data_end(),
            self.get_mora(),
        )

    def set_clients(self, ID):
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
        pass


def set_products(products):
    array = []
    for id in products:
        for produkt in produkts:
            if int(id) == produkt.get_ID():
                array.append(produkt)
                break
    return array
