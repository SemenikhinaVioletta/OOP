import Log
from Log import Logger

file_name = "File Class_New_Klient"


class New_Klient:

    def __init__(self, ID, name, phone, meil):
        Logger(file_name, "", "Class New_Klient - Method __init__ - make New klient:" + str(ID) + " " + str(name))
        self.name = str(name)
        self.phone = int(phone)
        self.meil = str(meil)
        self.ID = int(ID)

#--------------------------------------------------------------------------------------------------------------------------------
# Дополнительные функции
    def rename_newklient(self, name, phone, mail):
        Logger(file_name, "", "Class New_Klient - Method rename_newklient - rename New klient")
        if self.name != name:
            self.name = name

        if self.phone != phone:
            self.phone = phone

        if self.meil != mail:
            self.meil = mail

    def get(self):
        Logger(file_name, "", "Class New_Klient - Method get - get information about klient")
        return int(self.ID), str(self.name), int(self.phone), str(self.meil)

    def get_name(self):
        Logger(file_name, "", "Class New_Klient - Method get_name - get name of New klient")
        return str(self.name)

    def get_phone(self):
        Logger(file_name, "", "Class New_Klient - Method get_phone - get phone of New klient")
        return int(self.phone)

    def get_mail(self):
        Logger(file_name, "", "Class New_Klient - Method get_mail - get mail of New klient")
        return str(self.meil)

#--------------------------------------------------------------------------------------------------------------------------------

    def __del__(self):
        Logger(file_name, "", "Class New_Klient - Method __del__ - delete klient: " + str(self.ID),)
