import mysql.connector
import demo_mysql
    
mydb=demo_mysql.databaseConnection()
mycursor=mydb.cursor()

#inserting single value to database
sql="INSERT INTO customers (name, address) VALUES(%s, %s)"
# val=("Anuja","Nanded")
# mycursor.execute(sql, val)   #inserting values to the columns of database
# mydb.commit()     # it is rquired to make changes 
# print(mycursor.rowcount, "recorded successfully!!")

#inserting multiple values to database
# val=[
#     ("Nitin", 'Pune'),
#     ("Shyam", "Pune"),
#     ("Rohit", "Mumbai"),
#     ("Virat", "Delhi")
#     ]
# mycursor.executemany(sql, val)  #inserting many values to database
# mydb.commit()
# print(mycursor.rowcount, "recorded successfully!!!")

#getting last record id
val=("Vedant", "Mumbai")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted",mycursor.lastrowid)
