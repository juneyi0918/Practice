import tkinter.messagebox as msgbox
import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title ("simple GUI")

def add_file():
    files= filedialog.askopenfilenames(title="Please choose images",
        filetypes=(("PNG file","*.png"),("All files","*.*")), 
        initialdir=r"C:\Users\june's PC\Desktop\CODING") # r makes whole next thing as str
    
    for file in files:
        list_file.insert(END, file)


def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def browe_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)    

def merge_image():
    images = [Image.open(x) for x in list_file.get(0,END)]
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]
    widths, heights= zip(*(x.size for x in images))


    # get result picture size
    max_width, total_height = max(widths), sum(heights)
    
    # result size 
    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
    y_offset = 0 

    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx+1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), "June's image.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("Alarm","Merge picture is finised")


def start():
    print("width: ", cmb_width.get())
    print("space: ", cmb_space.get())
    print("format: ", cmb_format.get())

    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add image file")
        return

    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Please select save directory")
        return

    merge_image()


# File Frame( File add, File delete )
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="File Add", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="File Delete", command=del_file)
btn_del_file.pack(side="right")

#List Frame (Where can you see the files)
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill = "both", expand= True)
scrollbar.config(command=list_file.yview)


#Save Direction Frame
path_frame= LabelFrame(root, text="Save Directory")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="Browse..",width=10, command=browe_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


#Option Frame
option_frame = LabelFrame(root, text="Option")
option_frame.pack(padx=5, pady=5, ipady=5)

# 1. Width option

#label
lbl_width = Label(option_frame, text= "width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

#combo
opt_width = ["same as original", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values = opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. seperation option

#label
lbl_space = Label(option_frame, text= "space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

#combo
opt_space = ["none", "short", "normal", "long"]
cmb_space = ttk.Combobox(option_frame, state="readonly", values = opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)


# 3. file format option 

#label
lbl_format = Label(option_frame, text= "format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

#combo
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", values = opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5, ipady=5)


# Progress Bar frame
progress_frame = LabelFrame(root, text="Progress")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5, ipady=5)

# Run frame 
run_frame= Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(run_frame, padx=5, pady=5, text="Run", width=12,command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False,False)
root.mainloop()
