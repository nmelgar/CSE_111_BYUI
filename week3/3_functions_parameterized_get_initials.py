# this functions will return the first initial of a name
# you can specify a default value for parameters
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input("enter your first name: ")
# you can pass or not a parameter that has been specified
first_name_initial = get_initial(force_uppercase=False, name=first_name)

print(
    f"Your initial is: {first_name_initial}")
