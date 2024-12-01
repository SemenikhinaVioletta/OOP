import Log
from Log import Logger

file_name = "File New_Klient: "


class New_Klient:

    def __init__(self, ID, name, phone, meil):
        self.name = str(name)
        self.phone = int(phone)
        self.meil = str(meil)
        self.ID = int(ID)

    def rename_newklient(self, name, phone, mail):
        if self.name != name:
            self.name = name

        if self.phone != phone:
            self.phone = phone

        if self.meil != mail:
            self.meil = mail

    def get(self):
        return int(self.ID), str(self.name), int(self.phone), str(self.meil)

    def get_name(self):
        return str(self.name)

    def get_phone(self):
        return int(self.phone)

    def get_mail(self):
        return str(self.meil)

    def __del__(self):
        print("delete")