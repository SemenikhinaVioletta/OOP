import a_Window as Win
import a_Log as Logger
from c_proClient import pro_client as clients
from d_Produkt import produkts
from e_Contract import contracts
from a_Global_Per import windows, client_statuses, contract_statuses
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno

file_name = "File Make_Report"
methods = ["Pro clients", "Contracts", "Products"]


class ErrorReport(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            showerror(
                title="ERROR IN INPUT", message=self.message, parent=windows[5][-1]
            )
            return "Error Report, message: {0}".format(self.message)
        else:
            return "Error Report, raised"


def make_frame(wind):
    frame = Win.Frame(master=wind, relief=Win.SUNKEN)
    frame.pack(expand=True)
    return frame


def make_Table_product(flag, frame):
    columns = ("ID", "Name", "Cost of one copy", "Copies in stock", "Prise_sold")
    table_produkt = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_produkt.grid(row=1, column=1, sticky="nsew", rowspan=10)
    table_produkt.heading("ID", text="ID", anchor=Win.W)
    table_produkt.heading("ID", text="ID", anchor=Win.W)
    table_produkt.heading("Name", text="Name", anchor=Win.W)
    table_produkt.heading("Cost of one copy", text="Cost of one copy", anchor=Win.W)
    table_produkt.heading("Copies in stock", text="Copies in stock", anchor=Win.W)
    if flag == 0:
        table_produkt.heading("Prise_sold", text="Copies in stock", anchor=Win.W)
        table_produkt.column("#1", stretch=Win.NO, width=50)
        Prod = produkts
        for i in range(len(Prod) -1):
            for j in range(i + 1, len(Prod)):
                if Prod[j].zakazano > Prod[i].zakazano:
                    k = Prod[j]
                    Prod[j] = Prod[i]
                    Prod[i] = k
        for produkt in Prod:
            table_produkt.insert("", Win.END, values=produkt.get_all(flag))
    else:
        Prod = produkts
        for i in range(len(Prod) -1):
            for j in range(i + 1, len(Prod)):
                if Prod[j].zakazano * Prod[j].mora > Prod[i].zakazano * Prod[i].mora:
                    k = Prod[j]
                    Prod[j] = Prod[i]
                    Prod[i] = k
        table_produkt.heading("Prise_sold", text="Sales amont", anchor=Win.W)
        table_produkt.column("#1", stretch=Win.NO, width=50)
        for produkt in Prod:
            table_produkt.insert("", Win.END, values=produkt.get_all(flag))

    scrollbar = Win.ttk.Scrollbar(
        frame, orient=Win.VERTICAL, command=table_produkt.yview
    )


def make_othet(selected_option):
    try:
        if len(windows[5]) != 0:
            raise ErrorReport("This window is already open.")
        Logger.Logger.log_info(file_name, "Opening report window...")
        new_window = Win.Window("Report", "1000x300")
        new_window.make_protokol(lambda: Win.end(5))
        windows[5].append(new_window)
        frame = make_frame(new_window)
        if selected_option == methods[2]:
            make_Table_product(0, frame)
        make_front(frame, selected_option, new_window)
    except ErrorReport as e:
        Logger.Logger.log_error(file_name, "Error while opening window", str(e))


def make_front(frame, selected_option, wind):
    frame.destroy()
    frame = make_frame(wind)
    if selected_option == methods[2]:
        button_top_prise = Win.Button(frame, text="Sort of prise", command=lambda:make_Table_product(0, frame))
        button_top_sales = Win.Button(frame, text="Sort of sale", command=lambda:make_Table_product(1, frame))
        button_top_prise.grid(row=1, column=2, padx=5, pady=5)
        button_top_sales.grid(row=2, column=2, padx=5, pady=5)
