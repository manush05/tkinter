import pymysql

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "python_db"
)

mycursor = con.cursor()
    # INSERT INTO table name(para,para,para) VALUES('','','')
sql="""insert into student_detail(name,course,age) VALUES('saurav','worpress',18)"""
sql = "ALTER TABLE student_detail DROP age"
sql = "UPDATE student_detail SET course='python',name='saurav' where id=1"
sql = "DELETE FROM student_detail WHERE id=1"

# SELECT DATA FROM TABLE

sql = "SELECT * FROM student_detail"
mycursor.execute(sql)
print(mycursor.fetchall())
con.close()


try:
    mycursor.execute(sql)
    con.commit()
    print("Data Inserted")
except:
    con.rollback()
    print("Nothing Happened")
con.close()

