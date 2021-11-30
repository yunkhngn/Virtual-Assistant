# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of Tkinter Frame
win = Tk()

# Set the geometry
win.geometry("700x250")

# Define a function to check if a widget exists or not
def check_widget():
   exists = label.winfo_exists()
   if exists == 1:
      print("The widget exists.")
   else:
      print("The widget does not exist.")

# Create a Label widget
label = Label(win, text="Hey There! Howdy?", font=('Helvetica 18 bold'))
label.place(relx=.5, rely=.3, anchor=CENTER)

# We will define a button to check if a widget exists or not
button = ttk.Button(win, text="Check", command=check_widget)
button.place(relx=.5, rely=.5, anchor=CENTER)

win.mainloop()