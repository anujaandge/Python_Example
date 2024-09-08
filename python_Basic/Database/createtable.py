import mysql.connector
import demo_mysql
    
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")  #creating table

# mycursor.execute("SHOW TABLES")    #checking for tables exit in database
# for x in mycursor:
#     print(x)

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #adding new column to the existing database
