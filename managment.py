from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Managment System")
        self.root.geometry('1260x700+0+0')
        self.root.resizable(False,False)
        title = Label(self.root,text="Student Managment System",font=("Impact",35,'bold'),fg="#d77337",bg="white")
        title.pack(side=TOP,fill=X)

        #  BG Image
        # self.bg = ImageTk.PhotoImage(file="images/church.jpg")
        # self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.dob_var = StringVar()
        self.contact_var = StringVar()
        self.search_txt = StringVar()
        self.search_by = StringVar()


    # Manage Frame
        Manage_Frame = Frame(self.root, bg="white" ,bd=4 )
        Manage_Frame.place(x=10,y=100,height=600,width=450)
        
        m_title=Label(Manage_Frame,text="Manage Students",font=("Impact",30,'bold'),fg="#d77337",bg="white")
        m_title.grid(row=0,columnspan=2,pady=2)
        
        roll_lbl = Label(Manage_Frame,text="Roll No.",font=("Goudy",12,'bold'),fg="#d77337",bg="white")
        roll_lbl.grid(row=1,column=0,padx=10,pady=20,sticky="w")

        roll_txt = Entry(Manage_Frame,textvariable=self.roll_no_var,font=("times new roman",15), bg="lightgray")
        roll_txt.grid(row=1,column=1,padx=10,pady=20,sticky="w")

        name_lbl = Label(Manage_Frame,text="Name",font=("Goudy",12,'bold'),fg="#d77337",bg="white")
        name_lbl.grid(row=2,column=0,padx=10,pady=20,sticky="w")

        name_txt = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15), bg="lightgray")
        name_txt.grid(row=2,column=1,padx=10,pady=20,sticky="w")
        
        email_lbl = Label(Manage_Frame,text="Email",font=("Goudy",12,'bold'),fg="#d77337",bg="white")
        email_lbl.grid(row=3,column=0,padx=10,pady=20,sticky="w")

        email_txt = Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15), bg="lightgray")
        email_txt.grid(row=3,column=1,padx=10,pady=20,sticky="w")
        
        gender_lbl = Label(Manage_Frame,text="Gender",font=("Goudy",12,'bold'),fg="#d77337",bg="white")
        gender_lbl.grid(row=4,column=0,padx=10,pady=20,sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",15),state='read')
        combo_gender["values"] = ('Male', "Female","Other")
        combo_gender.grid(row=4,column=1,padx=10,pady=20,sticky="w")
 
        DOB_lbl = Label(Manage_Frame,text="DOB",font=("Goudy",12,'bold'),fg="#d77337",bg="white")
        DOB_lbl.grid(row=5,column=0,padx=10,pady=20,sticky="w")

        DOB_txt = Entry(Manage_Frame,font=("times new roman",15),textvariable=self.dob_var, bg="lightgray")
        DOB_txt.grid(row=5,column=1,padx=10,pady=20,sticky="w")

        contact_lbl = Label(Manage_Frame,text="Contact",font=("Goudy",12,'bold'),fg="#d77337",bg="white")
        contact_lbl.grid(row=6,column=0,padx=10,pady=20,sticky="w")

        contact_txt = Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15), bg="lightgray")
        contact_txt.grid(row=6,column=1,padx=10,pady=20,sticky="w")
        
        addr_lbl = Label(Manage_Frame,text="Address",font=("Goudy",12,'bold'),fg="#d77337",bg="white")
        addr_lbl.grid(row=7,column=0,padx=10,pady=20,sticky="w")

        self.addr_txt = Text(Manage_Frame,font=("times new roman",15),width=20,height=3, bg="lightgray")
        self.addr_txt.grid(row=7,column=1,padx=10,pady=20,sticky="w")
        
    # btn Frame

        btn_Frame = Frame(Manage_Frame,bd=4,bg="white")
        btn_Frame.place(x=10,y=550,width=500)

        addbtn=Button(btn_Frame,text="Add",command=self.add_students, width=10).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,command=self.update_students,text="update", width=10).grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(btn_Frame,command=self.delete_student,text="Delete", width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,command=self.clear,text="clear", width=10).grid(row=0,column=3,padx=10,pady=10)



    # Detail Frame 
        Detail_Frame = Frame(self.root, bg="white" ,bd=4 )
        Detail_Frame.place(x=490,y=100,height=600,width=800)

        search_by = Label(Detail_Frame,text="Search By",font=("Goudy",12,'bold'),fg="#d77337",bg="white")
        search_by.grid(row=0,column=0,padx=10,pady=20,sticky="w")
        
        combo_search = ttk.Combobox(Detail_Frame,textvar=self.search_by,font=("times new roman",15),state='read')
        combo_search["values"] = ('name', "roll_no","contact")
        combo_search.grid(row=0,column=1,padx=10,pady=20,sticky="w")
        
        search_txt = Entry(Detail_Frame,font=("times new roman",15),textvar=self.search_txt, bg="lightgray")
        search_txt.grid(row=0,column=2,padx=10,pady=20,sticky="w")
        
        searchbtn = Button(Detail_Frame,text="Search",command=self.search_data, width=10)
        searchbtn.grid(row=0,column=3,padx=10,pady=10)

        showbtn = Button(Detail_Frame,text="Show all", width=10)
        showbtn.grid(row=0,column=4,padx=10,pady=10)
    
    # Table Frame
        Table_Frame=Frame(Detail_Frame,bd=4,bg="white")
        Table_Frame.place(x=10,y=70, width=760,height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","dob","contact","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="dob")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("address",text="Address")
        self.student_table['show'] = 'headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("address",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        con = pymysql.connect(
            host="localhost",
            user = "root",
            passwd = "",
            db='student_management'
        )
        cur = con.cursor()
        msg = cur.execute("insert into student_details values(%s,%s,%s,%s,%s,%s,%s)",(
            self.roll_no_var.get(),
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.dob_var.get(),
            self.contact_var.get(),
            self.addr_txt.get("1.0",END)))
        if msg==True:
            messagebox.showinfo("successfullly","Inserted Successfully")
        else:
            print("Nothing Happend")
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    def fetch_data(self):
        con = pymysql.connect(
            host="localhost",
            user = "root",
            passwd = "",
            db='student_management'
        )
        cur = con.cursor()
        cur.execute("select * from student_details")
        rows=cur.fetchall()
        if len(rows) !=0 :
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.dob_var.set("")
        self.gender_var.set("")
        self.addr_txt.delete("1.0",END)
        self.contact_var.set("")

    def get_cursor(self,event):
        cursor_row = self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        print(row)
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.addr_txt.delete("1.0",END)
        self.addr_txt.insert(END,row[6])
        
    def update_students(self):
        con = pymysql.connect(
            host="localhost",
            user = "root",
            passwd = "",
            db='student_management'
        )
        cur = con.cursor()
        cur.execute("update student_details  set name=%s,email=%s,gender=%s,dob=%s,contact=%s,address=%s where roll_no=%s",(
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.dob_var.get(),
            self.contact_var.get(),
            self.addr_txt.get("1.0",END),
            self.roll_no_var.get()))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    def delete_student(self):
        con = pymysql.connect(
            host="localhost",
            user = "root",
            passwd = "",
            db='student_management'
        )
        cur = con.cursor()
        cur.execute("delete from student_details where roll_no=%s",self.roll_no_var.get())
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        
    def search_data(self):
        con = pymysql.connect(
            host="localhost",
            user = "root",
            passwd = "",
            db='student_management'
        )
        cur = con.cursor()
        cur.execute("select * from student_details where" +str(self.search_by.get()+" LIKE '%"+str(self.search_txt.get())+"%'"))
        rows=cur.fetchall()
        if len(rows) !=0 :
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

root = Tk()
obj = Student(root)
root.mainloop()