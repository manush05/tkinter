# Importing tkinter module 
from tkinter import * 
from tkinter.ttk import *
  
# creating Tk window 
window = Tk() 
  
# setting geometry of tk window 
window.geometry("200x200") 

my_frame = Frame(window, width=300, height=300) 
my_frame.pack() # Note the parentheses added here


button2 = Button(my_frame, text="I am at (0 x 0)")
button2.place(x=0, y=0, width=100, height=50)

button1 = Button(my_frame, text="I am at (100x150)")
button1.place(x=100, y=150)





# Text Widget
# textwdgt = Text(window, height = 5, width = 52).grid(row=0,column=0)  
# label widget 
  
# button widget 
 
# infinite loop which is required to 
# run tkinter program infinitely 
# until an interrupt occurs 
mainloop() 
