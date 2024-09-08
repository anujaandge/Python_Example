import mysql.connector
import demo_mysql
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()

sql="UPDATE customers SET address='Nanded' WHERE address='Mumbai' and id<5"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount," was affected")

sql1="SELECT * FROM customers"
mycursor.execute(sql1)
result=mycursor.fetchall()
for x in result:
    print(x)