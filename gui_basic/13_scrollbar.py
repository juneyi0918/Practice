from tkinter import *

root = Tk()
root.title ("simple GUI")
root.geometry("640x480+700+200")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill=Y)

listbox = Listbox(frame, selectmode= "extended", height =10, yscrollcommand=scrollbar.set)

for i in range(1,32):
    listbox.insert(END, str(i) + "day")
listbox.pack()

scrollbar.config(command=listbox.yview)

root.mainloop()
