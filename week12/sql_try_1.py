import mysql.connector

# -----> STEP 1
# create the connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="joPM9Lm8*+C",
    # you can add the database name to specify you are working with it
    database="mydatabase"
)

# print(mydb)

mycursor = mydb.cursor()


# -----> STEP 2
# to create a new data base
# if it runs without error, it was created succesfully
# mycursor.execute("CREATE DATABASE mydatabase")


# -----> STEP 3
# Check if database exits
# mycursor.execute("SHOW DATABASES")

# this will print all the db created
# for x in mycursor:
#     print(x)


# -----> STEP 4
# creating a table
# if it runs without error, it was created succesfully
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# -----> STEP 5
# check if table exists
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)


# -------------------------------------------
# -----> NO NUMBER STEP
# DROP a table
# mycursor.execute("DROP TABLE customers")

# -----> NO NUMBER STEP
# alter existing table to add PRIMARY KEY
mycursor.execute(
    "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
