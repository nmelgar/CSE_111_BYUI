from multiprocessing.sharedctypes import Value
import mysql.connector

# create the connection with db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="joPM9Lm8*+C",
    database="tasks"
)
mycursor = mydb.cursor()

# create a new db
# mycursor.execute("CREATE DATABASE tasks")

# creating a table with the tasks
# mycursor.execute(
#     "CREATE TABLE tasks (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255))")


def main():
    print("|----------------------------------------------|")
    print("|------------------TO-DO List------------------|")
    print("|----------------------------------------------|")
    print("\n")
    displayMenu()
    user_choice = int(input("What you want to do?"))
    if user_choice == 1:
        addTask()


def displayMenu():
    menu_items = ["Add Task", "Delete Task", "Exit"]
    counter = 1
    for item in menu_items:

        print(f"{counter}. {item}")
        counter += 1


def addTask():
    print("\n")
    new_task = input("What are you planning to do? ")
    importance_text = ("Level of importance?",
                       "H=High | M=Medium | L=Low")
    importance_level = input(importance_text)
    # insert into table using INSERT INTO statement

    sql = "INSERT INTO tasks (task, importance) VALUES (%s, %s)"

    values_to_insert = (new_task, importance_level)

    mycursor.execute(sql, values_to_insert)

    mydb.commit()

# def deleteTask():
#     DELETE FROM `tasks` WHERE `tasks`.`id` = 6;


if __name__ == "__main__":
    main()
