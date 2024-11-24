class New_Klient:
    
    
    def __init__(self, ID, name, phone, meil):
        print("File New_Klient: class New_Klient: method __init__ - make a newklient")
        self.name = name
        self.phone = phone
        self.meil = meil
        self.ID = ID
    
    def rename_newklient(self, name, phone, mail):
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
            
    def __del__(self):
        print("File New_Klient: class New_Klient: method __del__ - delete element  ID: " + str(self.ID))
        