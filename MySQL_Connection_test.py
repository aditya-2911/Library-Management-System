import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mysql@123"
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdatabase")

db1= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mysql@123",
    database="testdatabase"
)

mycursor1 = db1.cursor()
mycursor1.execute("CREATE TABLE Person(name VARCHAR(25), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

mycursor1.execute("DESCRIBE Person")

for x in mycursor1:
    print(x)