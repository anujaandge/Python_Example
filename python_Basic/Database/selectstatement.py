import mysql.connector
import demo_mysql
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM customers")
# myresult=mycursor.fetchall()  #fetchall() method, which fetches all rows from the last executed statement.
# for x in myresult:
#     print(x)
myreult=mycursor.fetchone()  #fetching single row it will fetch first row
print(myreult)
    
# mycursor.execute("SELECT name FROM customers")    #for fetching specific column
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)


 