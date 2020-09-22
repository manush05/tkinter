from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry('1000x600+100+50')
        self.root.resizable(False,False)
        #  BG Image
        self.bg = ImageTk.PhotoImage(file="images/church.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

    # Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        # title
        title = Label(Frame_login,text ='Login Here',font=("Impact",35,'bold'),fg="#d77337",bg="white").place(x=90,y=30)
        desc = Label(Frame_login,text ='Accountan Employee Login Area',font=("Goudy",12,'bold'),fg="#d77337",bg="white").place(x=80,y=90)

        # Username
        usernamelbl = Label(Frame_login,text ='Username',font=("Goudy",12,'bold'),fg="#d77337",bg="white").place(x=80,y=140)
        self.userEntry = Entry(Frame_login,font=("times new roman",15), bg="lightgray") 
        self.userEntry.place(x=90,y=170,width=350,height=35)

        # password
        passwordlbl = Label(Frame_login,text ='Password',font=("Goudy",12,'bold'),fg="#d77337",bg="white").place(x=80,y=220)
        self.passEntry = Entry(Frame_login,font=("times new roman",15), bg="lightgray") 
        self.passEntry.place(x=90,y=250,width=350,height=35)

        # Forget Password
        forgetlbl = Label(Frame_login,text="Forget Your Password?",fg="#d77337",bg="#ffffff",font=("times new roman",12)).place(x=90,y=290)

        #Submit Button 
        login = Button(self.root,command=self.login_function,text="Login",fg="#ffffff",bg="#d77337",font=("Goudy",12,'bold')).place(x=330,y=470,width=140,height=30)      

    def login_function(self):
        if self.userEntry.get() =="" or self.passEntry.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.userEntry.get() !="Manorma" or self.passEntry.get()!="1234" :
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"welcome {self.userEntry.get()} \n Your Password is {self.passEntry.get()}")    


root = Tk()
obj = Login(root)






root.mainloop()