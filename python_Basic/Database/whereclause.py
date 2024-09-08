import mysql.connector
import demo_mysql
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()
#sql="SELECT * FROM customers WHERE address='pune'"  
sql="SELECT * FROM customers WHERE address=%s"
adr=('pune',)
mycursor.execute(sql, adr)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
    
#select the records that starts, includes, or ends with a given letter or phrase.
sql1="SELECT * FROM customers WHERE address like '%N%'"
mycursor.execute(sql1)
myresult1=mycursor.fetchall()
for x in myresult1:
    print(x)