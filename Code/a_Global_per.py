import a_Window as Win

windows = [[], [], [], [], []]
basadate = "Code\DateBase\Pc.db"
status_klient = []
status_kontrakt = []
pro_klient = []

def make_combox(now, row_i, frame_for):
    method = []
    for i in status_klient:
        if i.get_status() != now:
            method.append(str(i.get_ID()))
    combobox = Win.Combobox(frame_for, values=method, width=30, state="readonly")
    combobox.grid(row=row_i, column=2, pady=5)
    combobox.set(now)
    return combobox