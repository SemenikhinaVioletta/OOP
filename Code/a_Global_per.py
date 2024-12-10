import a_Window as Win

windows = [[], [], [], [], []]
database = "Code\DateBase\Pc.db"
client_statuses = []
contract_statuses = []


def create_combobox(current_status, row_index, parent_frame):
    available_methods = []
    for client in client_statuses:
        if client.get_status() != current_status:
            available_methods.append(str(client.get_ID()))
    combobox = Win.Combobox(
        parent_frame, values=available_methods, width=30, state="readonly"
    )
    combobox.grid(row=row_index, column=2, pady=5)
    combobox.set(current_status)
    return combobox
