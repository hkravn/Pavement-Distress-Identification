############################################
# Authors Name: AKM (Avinash Kumar Mishra)
# Description: To serve as Wrapper Page and single program to load and run various Programs.
# Copyright License: GNU GPLv3
############################################

import svo_convertor as svocon
'''
import video_analysis as va
'''
import tkinter as tk
from  tkinter import Button, Grid, Label, filedialog

#Create a new Window
window = tk.Tk()

#Function for opening file explorer window
#Tutorial Used: https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
def browsefiles():
    global filename
    filename = filedialog.askopenfilename(
        initialdir='/',
        title="Select an svo file",
        filetypes=(("SVO files","*.svo"), ("all files","*.*"))
    )

    # label_file_explorer.configure(text = "File Opened: "+filename)

#Function for selecting dir for saving results
def setfolder():
    global filedir
    filedir = filedialog.askdirectory(
        initialdir='/'
    )

#Set Window Functions
window.title("AUTOMATED PAVEMENT DISTRESS IDENTIFICATION SYSTEM")
window.geometry("700x500")
window.config(background="white")

#Create file explorer Components
label_file_explorer = Label(
    window,
    text="SVO File for Conversion",
    width=80, height=5,
    fg="purple"
)
button_explore = Button(
    window,
    text="Select file",
    command=browsefiles
)
label_set_folder = Label(
    window,
    text="Select folder for saving Results",
    width=80, height=5,
    fg="purple"
)
button_set_folder = Button(
    window,
    text="Select Folder",
    command=setfolder
)
button_convert = Button(
    window,
    text="SVO to AVI Convert",
    command=lambda: svocon.videoconverter(filename, filedir)
)

# Grid Method is adopted
label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=2, row=1)
label_set_folder.grid(column=1, row=3)
button_set_folder.grid(column=2, row=3)
button_convert.grid(column=1, row=5)

#Create Display
window.mainloop()