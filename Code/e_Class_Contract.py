import sqlite3 as bd
import c_Class_Pro_Client as pro
import d_Class_Produkt as prod
from a_Log import Logger
from a_Global_Per import database, windows
from d_Produkt import produkts
from c_proClient import pro_client
from f_Class_Status_Client import contract_statuses

file_name = "File Class_Contract"
logger = Logger(file_name, [], "Application started")


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
        self.set_clients(ID_klient)
        self.ID = ID
        self.set_status(status)
        self.data_start = data_start
        self.data_end = data_end
        self.products = []
        self.set_products(products)
        self.mora = Mora
        self.set_mora()

    def set_products(self, products):
        """
        Sets the products associated with the contract.

        This method takes a space-separated string of product IDs, splits them, and
        iterates through the list to find matching product IDs in the global 'produkts' list.
        If a match is found, the corresponding product is added to the contract's products list.

        Parameters:
        products (str): A space-separated string of product IDs associated with the contract.

        Returns:
        None
        """
        p = products.split()
        for id in p:
            for produkt in produkts:
                if str(id) == str(produkt.get_ID()):
                    self.products.append(produkt)
                    break

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
        return self.data_start

    def get_data_end(self):
        return self.data_end

    def get(self):
        return (
            int(self.ID),
            self.get_status(),
            self.get_client_name(),
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
