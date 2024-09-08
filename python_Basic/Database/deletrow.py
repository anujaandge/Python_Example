import mysql.connector
import demo_mysql
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()

sql="DELETE FROM customers where address='Nanded' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount ,"was deleted")