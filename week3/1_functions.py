# datetime library call the datetime object call the now function
# print(datetime.datetime.now())

from datetime import datetime

# first_name = "nefi"
# print("task completed")
# print(datetime.datetime.now())
# print("")

# for x in range(0, 10):
#     print(x)
# print("task completed")
# print(datetime.datetime.now())
# print("")

# function to print current date and time


def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print("")


first_name = "nefi"
print_time("printed first name")

for x in range(0, 10):
    print(x)
print_time("completed for loop")
