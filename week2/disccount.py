"""
You work for a retail store that wants to increase sales on 
Tuesday and Wednesday, which are the store's slowest 
sales days. On Tuesday and Wednesday, if a customer's 
subtotal is $50 or greater, the store will discount 
the customer's subtotal by 10%.
"""

#get datetime function from datetime library
from datetime import datetime

today = datetime.now()
print("Today is: " + str(today))
print("Day: " + str(today.day))
print("Month: " + str(today.month))
print("Year: " + str(today.year))

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = today.weekday()

# Print the day of the week for the user to see.
#0 is for Mondays an so on
print(day_of_week)