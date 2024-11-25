class New_Klient:
    
    
    def __init__(self, ID, name, phone, meil):
        """
        Initialize a new New_Klient object with given ID, name, phone, and meil.

        Parameters:
        ID (int): The unique identifier for the new client.
        name (str): The name of the new client.
        phone (int): The phone number of the new client.
        meil (str): The email address of the new client.

        Returns:
        None
        """
        print("File New_Klient: class New_Klient: method __init__ - make a newklient")
        self.name = str(name)
        self.phone = int(phone)
        self.meil = str(meil)
        self.ID = int(ID)
    
    def rename_newklient(self, name, phone, mail):
        """
        Renames the client's name, phone number, and email address.

        This method checks if the provided values are different from the current values and updates them accordingly.
        It also prints relevant information to the console.

        Parameters:
        name (str): The new name for the client.
        phone (int): The new phone number for the client.
        mail (str): The new email address for the client.

        Returns:
        None
        """
        print("File New_Klient: class New_Klient: method rename_newklient - rename element  ID: " + str(self.ID))
        if(self.name != name):
            print("\tFile New_Klient: class New_Klient: method rename_newklient - rename element, make name: " + name)
            self.name = name

        if(self.phone != phone):
            print("\tFile New_Klient: class New_Klient: method rename_newklient - rename element, make phone: " + phone)
            self.phone = phone

        if(self.meil != mail):
            print("\tFile New_Klient: class New_Klient: method rename_newklient - rename element, make mail: " + mail)
            self.meil = mail
            
    def get(self):
        """
        Retrieves the client's ID, name, phone number, and email address.

        This method returns the current values of the client's ID, name, phone number, and email address.

        Parameters:
        None

        Returns:
        tuple: A tuple containing the client's ID (int), name (str), phone number (int), and email address (str).
        """
        return int(self.ID), str(self.name), int(self.phone), str(self.meil)
    
    def get_name(self):
        """
        Retrieves the client's name.

        This method returns the current name of the client.

        Parameters:
        None

        Returns:
        str: The client's name.
        """
        return str(self.name)
    
    def get_phone(self):
        """
        Retrieves the client's phone number.

        This method returns the current phone number of the client.

        Parameters:
        None

        Returns:
        int: The client's phone number.
        """
        return int(self.phone)

    def get_mail(self):
        """
        Retrieves the client's email address.

        This method returns the current email address of the client.

        Parameters:
        None

        Returns:
        str: The client's email address.
        """
        return str(self.meil)
        
    def __del__(self):
        """
        Destructor method for the New_Klient class.

        This method is called when an instance of the New_Klient class is about to be destroyed.
        It prints a message to the console indicating the deletion of the client with their ID.

        Parameters:
        None

        Returns:
        None
        """
        print("File New_Klient: class New_Klient: method __del__ - delete element  ID: " + str(self.ID))
    
        