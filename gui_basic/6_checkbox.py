from tkinter import *

root = Tk()
root.title ("simple GUI")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text=" Don't see again today", variable=chkvar)
chkbox.pack()


chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text=" Don't see again week", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text ="Click", command = btncmd )
btn.pack()


root.mainloop()
