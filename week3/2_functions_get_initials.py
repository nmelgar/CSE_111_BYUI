# this functions will return the first initial of a name
def get_initial(name):
    initial = name[0:1].upper()
    return initial


first_name = input("enter your first name: ")
# first_name_initial = first_name[0:1]
first_name_initial = get_initial(first_name)

middle_name = input("enter your middle name: ")
# middle_name_initial = middle_name[0:1]
middle_name_initial = get_initial(middle_name)


last_name = input("enter your last name: ")
# last_name_initial = last_name[0:1]
last_name_initial = get_initial(last_name)


print(
    f"Your initials are {first_name_initial}{middle_name_initial}{last_name_initial}")
