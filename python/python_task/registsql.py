from tkinter import *
import pymysql
from tkinter import messagebox as mb
import pymysql

root = Tk()
root.title("Registration Form")
root.geometry('500x500')
root.config(bg="azure")

name = StringVar()
course = StringVar()
phone = StringVar()
age = StringVar()

db = pymysql.connect(
    host="localhost",
    user = "root",
    passwd = "",
    db='registration'
)
mycursor = db.cursor()



def submitData():
    name1 = name.get()
    course1 = course.get()
    phone1 = phone.get()
    age1 = age.get()

    if(name1=="" or course1=="" or phone1=="" or age1==""):
        mb.showerror("Error","All Fields Are Required")

    if(name1!="" and course1!="" and phone1!="" and age1!=""):
        msg=mycursor.execute("INSERT INTO student_detail(name,course,phone,age) VALUES(%s,%s,%s,%s)",(name1,course1,phone1,age1))
        if msg==True:
            mb.showinfo("successfullly","Inserted Successfully")
        else:
            print("Nothing Happend")
        db.commit()

label_0 = Label(root,text="Registration Form",bg="azure",fg="#d77337",width=20,font=("bold",20))
label_0.place(x=70,y=53)

label_1 = Label(root,text="Name",width=20,bg="azure",font=("bold",10))
label_1.place(x=70,y=130)

entry1 = Entry(root,textvar=name)
entry1.place(x=240,y=130,width=200,height=35)

label_2 = Label(root,text="Course",bg="azure",width=20,font=("bold",10))
label_2.place(x=70,y=180)

entry2 = Entry(root,textvar=course)
entry2.place(x=240,y=180,width=200,height=35)

label_3 = Label(root,text="Phone No.",bg="azure",width=20,font=("bold",10))
label_3.place(x=70,y=230)

entry3 = Entry(root,textvar=phone)
entry3.place(x=240,y=230,width=200,height=35)

label_4 = Label(root,text="Age",bg="azure",width=20,font=("bold",10))
label_4.place(x=70,y=280)

entry4 = Entry(root,textvar=age)
entry4.place(x=240,y=280,width=200,height=35)

btn = Button(root,text="Submit",command=submitData,bg="lavender")
btn.place(x=150,y=330,width=100)

btn = Button(root,text="Delete",command=clearData,bg="lavender")
btn.place(x=300,y=330,width=100)

root.mainloop()
