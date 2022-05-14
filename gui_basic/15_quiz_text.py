import os
from tkinter import *

root = Tk()
root.title ("Untitled - Notepad")
root.geometry("640x480+700+200")

menu= Menu(root)

filename = "mynote.txt"

def cmd_open():
    if os.path.isfile(filename):
        with open(filename,"r") as file:
            txt.delete("1.0",END)
            txt.insert(END, file.read())


def cmd_save():
    with open(filename, "w") as file:
        file.write(txt.get("1.0",END))

    

# menu_File
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=cmd_open)
menu_file.add_command(label="Save", command=cmd_save)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# menu_Edit
menu.add_cascade(label="Edit")

# menu_Format
menu.add_cascade(label="Format")

# menu_View
menu.add_cascade(label="View")

# menu_Help
menu.add_cascade(label="Help")

scrollbar= Scrollbar(root)
scrollbar.pack(side="right",fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()
