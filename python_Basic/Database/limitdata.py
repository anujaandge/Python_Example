import mysql.connector
import demo_mysql
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()

#sql="SELECT * FROM customers LIMIT 4"
sql="SELECT * FROM customers LIMIT 5 OFFSET 2"
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result:
    print(x)