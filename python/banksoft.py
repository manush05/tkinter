import tkinter as tk
import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db = "atm"
    )

c = db.cursor()

# def new_user():
#     #root.destroy()

root = tk.Tk()
root.title('Banking Management System')
root.config(bg='grey')

main_label = tk.Label(root, text="Banking Management System", fg="Blue")
main_label.pack()

main_label.config(justify=tk.CENTER,pady=120)
new = tk.Button(root,text="New User",font='Arial 20',fg='black',command=lambda:new_user)
