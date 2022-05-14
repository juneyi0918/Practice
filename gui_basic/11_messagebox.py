import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title ("simple GUI")
root.geometry("640x480+700+200")

def info():
    msgbox.showinfo("Alarm","Your ticket is booked")

def warn():
    msgbox.showwarning("Warning","Ticket is Sold Out")

def error():
    msgbox.showerror("Error","Payment Error")


def okcancel():
    msgbox.askokcancel("ok/cancel","Do you want to buy ticket?")


def retrycancel():
    msgbox.askretrycancel("retry/cancel","Do you want to retry or cancel?")

def yesno():
    msgbox.askyesno("yes/no","should I study more?")

def yesnocancel():
    response=msgbox.askyesnocancel(title=None,message="work is not saved, want to save before close?")
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")


Button(root,command=info,text="Alarm").pack()
Button(root,command=warn,text="Warning").pack()
Button(root,command=error,text="Error").pack()

Button(root,command=okcancel,text="ok or canel").pack()
Button(root,command=retrycancel,text="retry or canel").pack()
Button(root,command=yesno,text="yes or no").pack()
Button(root,command=yesnocancel,text="yes or no or cancel").pack()




root.mainloop()
