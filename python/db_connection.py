import mysql.connector

mydb = mysql.connector.connect(host="localhost",user ="root",passwd ="admin@123",database = "python")
mycursor = mydb.cursor()
# mycursor.execute("select * from student")
# mycursor.execute("select * from student where college  = 'Indore'")
# mycursor.execute("select * from student where college LIKE '%ore%'")

sql = "SELECT * FROM student WHERE college = %s"
adr = ("Indore", )
mycursor.execute(sql,adr)
result = mycursor.fetchall()
for i in result:
    print(i)




# Sql Queries
# select * from student
# select * from student where college  = 'Ignou'
# "SELECT * FROM customers WHERE address LIKE '%way%'"
