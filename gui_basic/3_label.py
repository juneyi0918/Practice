from tkinter import *

root = Tk()
root.title ("simple GUI")
root.geometry("640x480+600+150")

label1 = Label(root, text= " HELLO")
label1.pack()

photo = PhotoImage(file ="gui_basic/image.png" )
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text="See you Again")
    
    global photo2
    photo2 = PhotoImage(file= "gui_basic/image2.png")
    label2.config(image=photo2)



btn =Button (root, text= "Click", command=change)
btn.pack()

root.mainloop()
