import mysql.connector
import demo_mysql
    
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")  #creating data base
mycursor.execute("SHOW DATABASES")  #for checking data base is exit or not
for x in mycursor:
    print(x)