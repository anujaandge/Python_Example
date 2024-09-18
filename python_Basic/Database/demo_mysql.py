import mysql.connector
def databaseConnection():
    return mysql.connector.connect(
    host="localhost",
    user='yourusername',
    password='yourpassword',
    database='anuja'     #this can directly connected to the existed database
    )
    
mydb=databaseConnection()
#mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")  #creating data base
# mycursor.execute("SHOW DATABASES")  #for checking data base is exit or not
# for x in mycursor:
#     print(x)

#mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")  #creating table

# mycursor.execute("SHOW TABLES")    #checking for tables exit in database
# for x in mycursor:
#     print(x)

#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #adding new column to the existing database





    
