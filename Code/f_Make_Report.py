import a_Window as Win
import a_Log as Logger
import datetime
import xml.etree.ElementTree as ET
import fpdf as fpdf
from datetime import date
from e_Error import chek_date
from c_proClient import pro_client as clients
from c_proClient import make_array as make_pro
from d_Produkt import produkts
from d_Produkt import make_array as make_prod
from e_Contract import contracts
from e_Contract import make_array as make_contr
from a_Global_Per import windows
from tkinter.messagebox import showerror
from fpdf import FPDF

file_name = "File Make_Report"
methods = ["Pro clients", "Contracts", "Products"]
data_s = date.today()
data_e = date.today()
array_to_bd = []


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
    make_prod()
    columns = ("ID", "Name", "Cost of one copy", "Copies in stock", "Prise_sold")
    table_produkt = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_produkt.grid(row=1, column=1, sticky="nsew", rowspan=10)
    table_produkt.heading("ID", text="ID", anchor=Win.W)
    table_produkt.heading("Name", text="Name", anchor=Win.W)
    table_produkt.heading("Cost of one copy", text="Cost of one copy", anchor=Win.W)
    table_produkt.heading("Copies in stock", text="Copies in stock", anchor=Win.W)
    table_produkt.heading("Prise_sold", text="Prise_sold", anchor=Win.W)
    if len(array_to_bd) != 0:
        array_to_bd.clear()
    if flag == 0:
        array_to_bd.append(
            ["ID", "Name", "Cost of one copy", "Copies in stock", "Prise_sold"]
        )
        table_produkt.heading("Prise_sold", text="Copies in stock", anchor=Win.W)
        table_produkt.column("#1", stretch=Win.NO, width=50)
        Prod = produkts
        for i in range(len(Prod) - 1):
            for j in range(i + 1, len(Prod)):
                if Prod[j].zakazano > Prod[i].zakazano:
                    k = Prod[j]
                    Prod[j] = Prod[i]
                    Prod[i] = k
        for produkt in Prod:
            table_produkt.insert("", Win.END, values=produkt.get_all(flag))
            array_to_bd.append(produkt.get_all(flag))
    else:
        array_to_bd.append(
            ["ID", "Name", "Cost of one copy", "Copies in stock", "Sales amont"]
        )
        Prod = produkts
        for i in range(len(Prod) - 1):
            for j in range(i + 1, len(Prod)):
                if Prod[j].zakazano * Prod[j].mora > Prod[i].zakazano * Prod[i].mora:
                    k = Prod[j]
                    Prod[j] = Prod[i]
                    Prod[i] = k
        table_produkt.heading("Prise_sold", text="Sales amont", anchor=Win.W)
        table_produkt.column("#1", stretch=Win.NO, width=50)
        for produkt in Prod:
            table_produkt.insert("", Win.END, values=produkt.get_all(flag))
            array_to_bd.append(produkt.get_all(flag))

    scrollbar = Win.ttk.Scrollbar(
        frame, orient=Win.VERTICAL, command=table_produkt.yview
    )


def make_Table_contract(flag, frame):
    make_contr()
    if flag != 5:
        columns = (
            "ID",
            "Status",
            "Client",
            "Data of Start Contract",
            "Data of end Contract",
            "Mora",
        )
        table_contract = Win.ttk.Treeview(frame, columns=columns, show="headings")
        table_contract.grid(row=1, column=1, sticky="nsew", rowspan=10)
        table_contract.heading("ID", text="ID", anchor=Win.W)
        table_contract.heading("Status", text="Status", anchor=Win.W)
        table_contract.heading("Client", text="Client", anchor=Win.W)
        table_contract.heading(
            "Data of Start Contract", text="Data of Start Contract", anchor=Win.W
        )
        table_contract.heading(
            "Data of end Contract", text="Data of end Contract", anchor=Win.W
        )
        table_contract.heading("Mora", text="Mora", anchor=Win.W)
        table_contract.column("#1", stretch=Win.NO, width=50)
        if len(array_to_bd) != 0:
            array_to_bd.clear()
        array_to_bd.append(
            [
                "ID",
                "Status",
                "Client",
                "Data of Start Contract",
                "Data of end Contract",
                "Mora",
            ]
        )
        if flag == 1 or flag == 2 or flag == 3:
            for contract in contracts:
                if contract.get_status() == flag:
                    table_contract.insert("", Win.END, values=contract.get_all())
                    array_to_bd.append(contract.get_all())
        if flag == 4:
            for contract in contracts:
                if (
                    contract.get_rial_data_start() >= data_s
                    and contract.get_rial_data_start() <= data_e
                ):
                    table_contract.insert("", Win.END, values=contract.get_all())
                    array_to_bd.append(contract.get_all())

        scrollbar = Win.ttk.Scrollbar(
            frame, orient=Win.VERTICAL, command=table_contract.yview
        )
    if flag == 5:
        prib = 0
        ub = 0
        for contract in contracts:
            if (
                contract.get_rial_data_start() >= data_s
                and contract.get_rial_data_start() <= data_e
                and contract.get_ID() != 2
            ) or (contract.get_ID() == 3):
                prib += contract.get_mora()
            elif (
                contract.get_rial_data_end() >= data_s
                and contract.get_rial_data_end() <= data_e
                and contract.get_ID() == 2
            ):
                ub += contract.get_mora()
        Win.Label(
            frame,
            text="Profi: "
            + str(ub)
            + "\nloss: "
            + str(prib)
            + "\nFrom: "
            + str(data_s)
            + " to: "
            + str(data_e),
        ).grid(row=1, column=1, rowspan=5)


def make_Table_client(flag, frame):
    make_pro()
    columns = ("ID", "Name", "Mora", "Phone", "Mail", "Status", "Numbers contracts")
    table_new_Client = Win.ttk.Treeview(frame, columns=columns, show="headings")
    table_new_Client.grid(row=1, column=1, sticky="nsew", rowspan=10)
    table_new_Client.heading("ID", text="ID", anchor=Win.W)
    table_new_Client.heading("Name", text="Name", anchor=Win.W)
    table_new_Client.heading("Mora", text="Mora", anchor=Win.W)
    table_new_Client.heading("Phone", text="Phone", anchor=Win.W)
    table_new_Client.heading("Mail", text="Mail", anchor=Win.W)
    table_new_Client.heading("Status", text="Status", anchor=Win.W)
    table_new_Client.heading(
        "Numbers contracts", text="Numbers contracts", anchor=Win.W
    )
    table_new_Client.column("#1", stretch=Win.NO, width=50)

    if len(array_to_bd) != 0:
        array_to_bd.clear()
    array_to_bd.append(
        ["ID", "Name", "Mora", "Phone", "Mail", "Status", "Numbers contracts"]
    )
    if flag == 0:
        Cli = clients
        for i in range(len(Cli) - 1):
            for j in range(i + 1, len(Cli)):
                j_len = Cli[j].get_contract_id().split()
                i_len = Cli[i].get_contract_id().split()
                if len(j_len) > len(i_len):
                    k = Cli[j]
                    Cli[j] = Cli[i]
                    Cli[i] = k
        for Client in Cli:
            table_new_Client.insert("", Win.END, values=Client.get_all(flag))
            array_to_bd.append(Client.get_all(flag))
    if flag == 1:
        Cli = clients
        for i in range(len(Cli) - 1):
            for j in range(i + 1, len(Cli)):
                if Cli[j].get_mora() > Cli[i].get_mora():
                    k = Cli[j]
                    Cli[j] = Cli[i]
                    Cli[i] = k
        for Client in Cli:
            table_new_Client.insert("", Win.END, values=Client.get_all(flag))
            array_to_bd.append(Client.get_all(flag))
    scrollbar = Win.ttk.Scrollbar(
        frame, orient=Win.VERTICAL, command=table_new_Client.yview
    )


def make_othet(selected_option):
    try:
        if len(windows[5]) != 0:
            raise ErrorReport("This window is already open.")
        Logger.Logger.log_info(file_name, "Opening report window...")
        if selected_option == methods[0] or selected_option == methods[1]:
            new_window = Win.Window("Report", "1500x300")
        else:
            new_window = Win.Window("Report", "1100x300")
        new_window.make_protokol(lambda: Win.end(5))
        windows[5].append(new_window)
        frame = make_frame(new_window)
        make_front(frame, selected_option, new_window)
    except ErrorReport as e:
        Logger.Logger.log_error(file_name, "Error while opening window", str(e))


def enter_time(flag, frame_for):
    new_window = Win.Window("Report", "500x100")
    new_window.make_protokol(lambda: new_window.close_window(5))
    windows[5].append(new_window)
    frame = make_frame(new_window)
    text1 = Win.Label(frame, text="From")
    start = Win.Entry(
        frame,
    )
    text1.grid(row=1, column=1)
    start.grid(row=1, column=2, padx=5)
    end = Win.Entry(
        frame,
    )
    text2 = Win.Label(frame, text="to")
    text2.grid(row=1, column=3, padx=5)
    end.grid(row=1, column=4, padx=5)
    bat = Win.Button(
        frame,
        text="Do",
        command=lambda: (
            do(start.get(), end.get(), flag, frame_for),
            new_window.close_window(5),
        ),
    )
    bat.grid(row=2, column=3, pady=5)


def do(start, end, flag, frame_for):
    if chek_date(start, end):
        start = str(start).split("-")
        end = str(end).split("-")
        data_s = date(int(start[0]), int(start[1]), int(start[2].split()[0]))
        if flag == 5 and data_e > date(
            int(end[0]), int(end[1]), int(end[2].split()[0])
        ):
            deta_e = date(int(end[0]), int(end[1]), int(end[2].split()[0]))
        make_Table_contract(flag, frame_for)


def make_front(frame, selected_option, wind):
    frame.destroy()
    frame = make_frame(wind)
    but = Win.Button(frame, text="Make PDF", command=lambda: Make_Pdf(array_to_bd))
    but.grid(row=12, column=1, padx=5, pady=20)
    if selected_option == methods[2]:
        button_top_prise = Win.Button(
            frame, text="Sort of prise", command=lambda: make_Table_product(0, frame)
        )
        button_top_sales = Win.Button(
            frame, text="Sort of sale", command=lambda: make_Table_product(1, frame)
        )
        button_top_prise.grid(row=1, column=2, padx=5, pady=5)
        button_top_sales.grid(row=2, column=2, padx=5, pady=5)
    if selected_option == methods[1]:
        button_start = Win.Button(
            frame,
            text="Current contracts",
            command=lambda: make_Table_contract(1, frame),
        )
        button_end = Win.Button(
            frame,
            text="Completed contracts",
            command=lambda: make_Table_contract(2, frame),
        )
        button_luse = Win.Button(
            frame,
            text="Expired contracts",
            command=lambda: make_Table_contract(3, frame),
        )
        button_start.grid(row=1, column=2, padx=5, pady=5)
        button_end.grid(row=2, column=2, padx=5, pady=5)
        button_luse.grid(row=3, column=2, padx=5, pady=5)
        button_lise_time = Win.Button(
            frame, text="Report for the time", command=lambda: enter_time(4, frame)
        )
        button_lise_time.grid(row=4, column=2, padx=5, pady=5)
        button_prise_time = Win.Button(
            frame,
            text="Report for profit of time",
            command=lambda: enter_time(5, frame),
        )
        button_prise_time.grid(row=5, column=2, padx=5, pady=5)
    if selected_option == methods[0]:
        button_numbers = Win.Button(
            frame,
            text="Sort of numbers contrakt",
            command=lambda: make_Table_client(0, frame),
        )
        button_numbers.grid(row=1, column=2, padx=5, pady=5)
        button_sale = Win.Button(
            frame,
            text="Sort of sale contrakt",
            command=lambda: make_Table_client(1, frame),
        )
        button_sale.grid(row=2, column=2, padx=5, pady=5)


def Make_Pdf(array):
    try:
        if len(array) <= 1:
            message = "No elements to otchet"
            raise ErrorReport(message)
        if len(array) != 0:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_xy(1, 1)
            pdf.set_font("Times", size=10)
            s = []
            for elem in array:
                s.append([])
                for i in elem:
                    if str(i)[0].isalpha() or str(i)[0].isdigit():
                        s[-1].append(str(i))

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=8)

            col_width = pdf.w / (len(array[0]) + 1)
            row_height = pdf.font_size * 2
            spacing = 1
            for row in s:
                for item in row:
                    if len(item) * 1.5 > col_width:
                        item = item[: int(col_width / 1.5 - 1.5)] + "..."
                    pdf.cell(col_width, row_height * spacing, txt=item, border=1)
                pdf.ln(row_height * spacing)

            pdf.output("Otchet.pdf")

    except ErrorReport as e:
        Logger.Logger.log_error(file_name, "Error in report", str(e))
    finally:
        array_to_bd.clear()
