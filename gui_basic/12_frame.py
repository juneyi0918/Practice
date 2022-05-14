from tkinter import *

root = Tk()
root.title ("simple GUI")
root.geometry("640x480+700+200")

Label(root, text="Please Select Menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")

# menu frame
frame_burger = LabelFrame(root, text="Burger")
frame_burger.pack(side="left", fill="both", expand=True)

burger_var = StringVar()
btn_burger1 = Radiobutton(frame_burger, text ="Hamburger", value= "Hamburger", variable=burger_var)
btn_burger2 = Radiobutton(frame_burger, text ="Cheeseburger", value= "Cheeseburger", variable=burger_var)
btn_burger3 = Radiobutton(frame_burger, text ="Chickenburger", value= "Chickenburger", variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


# drink frame
frame_drink = LabelFrame(root, text= "Drink")
frame_drink.pack(side="right", fill="both", expand=True)

drink_var = StringVar()
btn_drink1 = Radiobutton (frame_drink, text= "Coke", value="Coke", variable=drink_var)
btn_drink2 = Radiobutton (frame_drink, text= "Sprite", value="Sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()




root.mainloop()
