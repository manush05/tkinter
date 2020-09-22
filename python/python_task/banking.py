import tkinter as tk
import pymysql


con = pymysql.connect(host="localhost",user="root",passwd="",db="atm")
c = con.cursor()

def submit1():
    pass

def new_user():
    print("new User")   
    root.destroy()
    root1=tk.Tk()
    root1.title("Registration Page")
    root1.minsize(1100,550)
    root1.config(bg="white")

    tk.Label(root1,text="Welcome to the Registration Page", font = "Arial 30",justify= tk.CENTER).grid()
    tk.Label(root1,text="Enter Your Name", font= "Arial 20", pady=15).grid(row=5,column=0)
    name = tk.Entry(root1)
    name.grid(row=5,column=1)
    name_error = tk.Label(root1,font='10',fg='red')
    name_error.grid(row=6,column=1)

    tk.Label(root1,text="Enter Your Password", font= "Arial 20", pady=15).grid(row=7,column=0)
    password1 = tk.Entry(root1,show="*")
    password1.grid(row=7,column=1)

    
    tk.Label(root1,text="Re Enter Your Password", font= "Arial 20", pady=15).grid(row=9,column=0)
    password2 = tk.Entry(root1,show="*")
    password2.grid(row=9,column=1)
    password_error = tk.Label(root1,font="10",fg='red')
    password_error.grid(row=10,column=1)

    tk.Button(root1,text="Submit",font="Arial 25" , fg='white',bg="black",justify=tk.CENTER,command=lambda :submit1()).grid(row=12)

    def submit1():
        flag=0
        if(name.get==""):
            name_error.config(text="Username Cannot be Empty") 
            if(password1.get() != ""):
                password_error.config(text="")
        
        if(password1.get()==""):
            password_error.config(text="Please Fill Password")
            if(name.get() !=""):
                name_error.config(text="")
        
        elif(name.get()!="") and (password1.get()!=""):
            name_error.config(text="")
            password_error.config(text="")

            c.execute('select *from details')
            data = c.fetchall()
            for row in data:
                if name.get == row[0]:
                    flag=1
                    break   
                if flag ==1:
                    name_error.config(text="Username Already Exist")
                elif flag ==0:
                    if(password1.get() != password2.get()):
                        password_error.config(text="Password not match")
                    else:
                        root9 = tk.Tk()
                        root9.title("Money Deposit")
                        root9.minsize(600,300)
                        root.config(bg="grey")

                        tk.Label(root9,text="would you like to add monry",font="Arial 20",justify=tk.CENTER).grid(row=0)
                        tk.Button(root9,text= "Yes" ,font="Arial 15",justify=tk.CENTER, command=lambda:yes()).grid(row=1,column=0) 
                        tk.Button(root9,text= "No" ,font="Arial 15",justify=tk.CENTER, command=lambda:no()).grid(row=1,column=1)                            

                        def yes():
                            root9.distroy()
                            root10 = tk.Tk()
                            root10.title("Money Deposit")
                            root10.minsize(300,200)

                            root10.config(bg="grey")
                            tk.Label(root10,text="Enter Your Amount: ",font="Arial 20").grid(row=0,column=0)
                            amount=tk.Entry(root10).grid(row=0,column=1)
                            tk.Button(root10,text="Done",font="Arial 15",command=lambda:done()).grid(row=2)
                            def done():
                                try:
                                    c.execute('insert into dtails values(%s,%s,%s)',(name.get(),password2.get(),amount.get()))
                                    con.commit
                                    # main(name,password2,amount)

                                except:
                                    con.rollback()
                                    tk.Label(root10,"Some Unknown Error Occured",bg='red').grid(row=1,column=1)
                                root10.mainloop()
                        def no():
                            try:
                                c.execute('insert into details values(%s,%s,%s)',(name.get(),password2.get(),0))
                                con.commit()
                                # main(name,password2)
                            except:
                                con.rollback(
                                    tk.Label(root9,text="Some Unklnow Error Occur")
                                )
                        root9.mainloop()
    root1.mainloop()
def old_user():
    root.distroy()
    root2=tk.Tk()
    root2.title("Login")
    root2.minsize(1000,500)
    root2.config(bg='grey')

    tk.Label(root2,text="Welcome to Login Page",font='Arial 30',justify=tk.CENTER,pady=10).grid()
    tk.Label(root2,text="Enter Your Name",font="Arial 20").grid(row=5,column=0)
    name = tk.Entry(root2)
    name.grid(row=5,column=1)
    name_error = tk.Label(root2,font='10',fg='red')
    name_error.grid(row=6,column=1)

    tk.Label(root2,text="Enter Your Password", font= "Arial 20", pady=15).grid(row=7,column=0)
    password1 = tk.Entry(root2,show="*")
    password1.grid(row=7,column=1)
    password_error = tk.Label(root2,fg='red',font='10')
    password_error.grid(row=8,column=1)

    tk.Label(root2).grid(row=9)

    tk.Button(root2,text="Login",justify=tk.CENTER,command=lambda:login()).grid(row=10)
    def login():
        flag=0
        if (name.get == ""):
            name_error.config(text="Username Canont empty")
            if (password1.get !=""):
                password_error.config(text="")
        if(password1.get() == ""):
            password_error.config(text="Password Canont empty")
            if(name.get()!= ""):
                name_error.config(text="")
        elif(name.get()!="") and (password1.get()!=""):
            name_error.config(text="")
            password_error.config(text="")

            c.execute('select * from details')
            data = c.fetchall()
            for row in data:
                if name.get == row[0]:
                    flag=1
                    break   
                if flag==0:
                    name_error.config(text="Username cannot Exist")
                elif flag==1:
                    c.execute('select password from details where name=(%s)',name.get())
                    pwd= c.fetch()
                    if(password1.get()!=pwd[0]):
                        password_error.config(text="Incorrect Password")
                    else:
                        main(name,password1)
    root2.mainloop()
def main(name,password1):
    c.execute("select balance from details where namer=(%s)",name.get())
    bal= c.fetchone()
    balance = bal[0]


    root3 = tk.Tk()
    root3.title('Main Page')
    root3.minsize(1100,550)
    root3.config(bg="orange")


    tk.Button(root3,text="Check Balance", font="Arial 20")
    tk.Label()

    root3.mainloop()





root = tk.Tk()
root.title("Banking Software System")
root.config(bg='white')


main_label = tk.Label(root, text="Banking Management System", fg="Blue", font="Century 40")
main_label.pack()
main_label.config(justify=tk.CENTER,pady=120)

new = tk.Button(root,text='new user',font="Arial 20",fg="black",command=lambda:new_user())
new.pack()
new.config(justify=tk.CENTER,width=30)

old = tk.Button(root,text="Registered User",font= "Arial 20", fg='black' ,command=lambda:old_user())
old.pack()
old.config(justify=tk.CENTER,width=30)

root.mainloop()