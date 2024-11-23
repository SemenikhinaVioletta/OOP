import xml.etree.ElementTree as ET
import tkinter
from tkinter import *
from tkinter import messagebox

print("File Python: Start")
window = Tk()
window.title("PC for management")
window.geometry("600x400")
frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

def save():
    print("File Python. Method save: Attampt of save new status")



def start():
    print("File Python. Method start: Open window")
    window.mainloop()

def end():
    print("File Python. Method end: End")
    window.destroy()
    print("Clouse window")

text_status = Label(
    frame,
    text='Enter name in formate "Status":',
)
text_status.grid(row=1, column=1)

enter_status = Entry(
    frame,
)
enter_status.grid(row=1, column=2, pady=5)

save_stat = Button(
    frame,
    text="Enter new Status",
    command=save,
)
save_stat.grid(row=1, column=3)

read = Button(
    frame,
    text="Read xml",
)
read.grid(row=3, column=1)

end_button = Button(
    frame,
    text="End",
    command=end,
)
end_button.grid(row=5, column=1)

start()