from tkinter import *
from tkinter import filedialog


def save_file():
    open_file = filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def clear():
    entry.delete(1.0,END)

def load():
    file=filedialog.askopenfile(mode="r",filetype=[('text files','*.txt')])
    if file is not None:
        content= file.read()
        entry.insert(INSERT,content)


root = Tk()
root.geometry("500x600")
root.title("Text Editor")
root.config(bg="SkyBlue2")
root.resizable(False,False)

savebtn = Button(root,text="Save file",command=lambda:save_file(),bg="RoyalBlue1" )
savebtn.place(x=10,y=10,width="120")

clearbtn = Button(root,text="Clear",command=lambda:clear(),bg="RoyalBlue1")
clearbtn.place(x=150,y=10,width="120")


loadbtn = Button(root,text="Load File",command=lambda:load(),bg="RoyalBlue1")
loadbtn.place(x=290,y=10 ,width="120")

entry = Text(root,height=33,width=58,wrap=WORD)
entry.place(x=10, y=50)

root.mainloop()