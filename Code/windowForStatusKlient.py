import xml.etree.ElementTree as ET
import tkinter
from tkinter import *
from tkinter import messagebox

from Error import ErrorStatus

from doc import do_doc

def chekbox(message):
    """
    This function checks if a given message contains only alphabetic characters.

    Parameters:
    message (str): The message to be checked.

    Returns:
    bool: True if the message contains only alphabetic characters, False otherwise.
    """
    flag = True
    for j in message:
        if not j.isalpha():
            flag = False
            break
    return flag


def add_stKl(message):
    """
    This function adds a new status to the 'Status_klient.xml' file.

    Parameters:
    message (str): The new status to be added.

    Returns:
    None. The function prints a message indicating that the status has been added to the file.
    """
    print("File windowForStatusKlient. Method add_stKl: Start add new status")
    with open("Status_klient.xml", "r") as f:
        s = list(map(str, f.readlines()))
    count = 0
    for i in s:
        if "field" in i:
            count += 1
    count_st = str(count // 2 + 1)
    start = ""
    str_first = ""
    str_second = ""
    end = ""

   # This block of code is iterating over each line in the list `s` and performing different operations based on the content of each line. Here is a breakdown of what each part of the code is doing:
    for i in s:
        if "field" in i and len(str_first) == 0:
            flag = True
            for j in range(len(i)):
                if flag:
                    str_first += i[j]
                    if i[j] == ">":
                        flag = False
                elif count_st != 0:
                    str_first += count_st
                    count_st = 0
                elif i[j] == "<":
                    str_first += i[j]
                    flag = True
            str_first += "\n"
        elif "field" in i and len(str_second) == 0:
            flag = True
            count_st = 1
            for j in range(len(i)):
                if flag:
                    str_second += i[j]
                    if i[j] == ">":
                        flag = False
                elif count_st != 0:
                    str_second += message
                    count_st = 0
                elif i[j] == "<":
                    str_second += i[j]
                    flag = True
            str_second += "\n"
        elif "<row>" in i:
            start = i
        elif "</row>" in i:
            end = i
            break
    count = 0
    # This block of code is responsible for updating the content of the "Status_klient.xml" file with a new status entry. Here is a breakdown of what each part of the code is doing:
    with open("Status_klient.xml", "w") as in_f:
        with open("docs.txt", "w") as f:
            for line in s:
                if "</resultset>" in line:
                    f.write("\n" + start + str_first + str_second + end)
                    in_f.write("\n" + start + str_first + str_second + end)
                f.write(line)
                in_f.write(line)
    print("File windowForStatusKlient. Method add_stKl:" + message + " in file!")


def save_stKl(enter_status):
    """
    This function validates and saves a new status to the 'Status_klient.xml' file.

    Parameters:
    enter_status (tkinter.Entry): The tkinter Entry widget containing the new status to be saved.

    Returns:
    None. The function prints a message indicating the outcome of the status validation and saving process.
    """
    status = enter_status.get()
    flag = True
    error = ErrorStatus("Error")

    print("File windowForStatusKlient. Method save_stKl: Start checking status:", status)
    if len(status) < 3:
        error.message = "ERROR, in format:\nStatus must contain at least 3 characters"
        flag = False
    else:
        # Validate status word count
        if status.count(" ") != 0:
            error.message = "ERROR, in format:\nstatus must contain exactly 1 world"
            flag = False
        # Validate status character type
        elif not chekbox(status):
            error.message = str(
                "ERROR, in format:\nStatus must contain only letters, can`t be: "
                + status
            )
            flag = False

    # Process the status based on validation result
    if flag:
        error.message = str("Not error in this: " + status + "!")
        messagebox.showinfo("status-error", error.message)
        add_stKl(status)
    else:
        messagebox.showerror("status-error", error.message)
    print("File windowForStatusKlient. Method save_stKl: Stop cheking... result:")
    print(error.message)


def read_stKl():
    """
    This function creates a graphical user interface (GUI) window to display the contents of the 'Status_klient.xml' file.

    The window displays the status entries in a tabular format with columns for '#' and 'status'.

    Parameters:
    None.

    Returns:
    None. The function prints a message indicating the start of the GUI window and destroys the window when the 'End' button is clicked.
    """
    print("File windowForStatusKlient. Method read_stKl: Start window with xml (Status Klient)")
    window_xml = Tk()
    window_xml.title("Read from xml file")
    window_xml.geometry("400x200")
    frame_xml = Frame(window_xml, padx=10, pady=10)
    frame_xml.pack(expand=True)
    
    def do():
        print("File windowForStatusKlient. Method add_stKl.do: Start make othet")
        do_doc()

    def end():
        """
        This inner function closes the GUI window when called.

        Parameters:
        None.

        Returns:
        None. The function prints a message indicating the end of the GUI window and destroys the window.
        """
        print("File windowForStatusKlient. Method add_stKl.end: End window with xml (Status Klient)")
        window_xml.destroy()

    # This block of code is responsible for reading the contents of the 'Status_klient.xml' file and displaying them in a graphical user interface (GUI) window. Here is a breakdown of what each part of the code is doing:
    tree = ET.parse("Status_klient.xml")
    root = tree.getroot()
    Label(
        frame_xml,
        text="#",
    ).grid(row=1, column=1)
    Label(
        frame_xml,
        text="status",
    ).grid(row=1, column=2)
    i = 2
    j = 1
    for elem in root.iter():
        if str(elem.text)[0].isalpha() or str(elem.text)[0].isdigit():
            Label(
                frame_xml,
                text=str(elem.text),
            ).grid(row=i, column=j)
            j += 1
            if j == 3:
                i += 1
                j = 1

    otchet_button = Button(
        frame_xml,
        text="Otchet",
        command=do,
    )
    otchet_button.grid(row=i, column=1)

   # The code snippet you provided is creating a button widget in a tkinter GUI window. Here is a breakdown of what each part of the code is doing:
    end_button = Button(
        frame_xml,
        text="End",
        command=end,
    )
    end_button.grid(row=i, column=2)