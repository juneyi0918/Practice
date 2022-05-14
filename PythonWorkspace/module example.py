# # glob : search for folder and file list
# import glob
# print(glob.glob("*.py"))


# OS : basic function for operating system

# import os
# print(os.getcwd()) # show present dir

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("This folder is already exist")
#     os.rmdir(folder)
#     print(folder, "folder is deleted")
# else:
#     os.makedirs(folder) # make folder
#     print(folder, "folder is created")


# time : time related function
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))