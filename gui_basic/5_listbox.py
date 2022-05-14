from tkinter import *

root = Tk()
root.title ("simple GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode = "extended", height= 0)
listbox.insert(0, " APPLE ")
listbox.insert(1, " STRAWBERRY ")
listbox.insert(2, " BANANA ")
listbox.insert(END, " WATERMELON ")
listbox.insert(END, " GRAPE ")
listbox.pack()

def btncmd():
    # listbox.delete(END)  # Delete Last in listbox
    # listbox.delete(0)   # Delete FIRST in listbox

    # print("There are {0} fruit/s in Listbox".format(listbox.size()))
    # print("There are",listbox.size(), "fruits in listbox")

    print("First to Third List are : ", listbox.get(0,2))


    print("selected fruits :", listbox.curselection())

btn = Button(root, text ="Click", command = btncmd )
btn.pack()


root.mainloop()
