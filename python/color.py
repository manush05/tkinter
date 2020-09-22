from tkinter import *

class App:
    def __init__(self, root):
        self.root = root
        self.var = StringVar() #creates StringVar to store contents of entry
        self.var.trace(mode="w", callback=self.command)
        #the above sets up a callback if the variable containing
        #the value of the entry gets updated
        self.entry = Entry(self.root, textvariable = self.var)
        self.entry.pack()
    def command(self, *args):
        try: #trys to update the background to the entry contents
            self.entry.config({"background": self.entry.get()})
        except: #if the above fails then it does the below
            self.entry.config({"background": "White"})

root = Tk()
App(root)
color = App(root)
color.command()
root.mainloop()