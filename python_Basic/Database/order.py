import mysql.connector
import demo_mysql
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()

sql="SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
    
    
print("order by desending order")
sql1="SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql1)
myresult1=mycursor.fetchall()
for x in myresult1:
    print(x)    