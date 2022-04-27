# get datetime function from datetime library
from datetime import datetime

today = datetime.now()
# print("Today is: " + str(today))
# print("Day: " + str(today.day))
# print("Month: " + str(today.month))
# print("Year: " + str(today.year))

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
# day_of_week = today.weekday()

# Print the day of the week for the user to see.
# 0 is for Mondays an so on
# print(day_of_week)

day_of_week = 3


subtotal = float(input("Please enter the subtotal: "))

if subtotal >= 50 and (day_of_week == 2 or day_of_week == 3):
    disccount_amount = subtotal * 0.1
    subtotal -= disccount_amount
    tax = subtotal * 0.06
    tax = round(tax, 2)
    total = subtotal + tax

    print(f"Disccount amount: {disccount_amount:.2f}")
    print(f"Sales tax amount: {tax:.2f}")
    print(f"Total: {total:.2f}")

else:
    tax = subtotal * 0.06
    tax = round(tax, 2)
    total = subtotal + tax

    print(f"Sales tax amount: {tax:.2f}")
    print(f"Total: {total:.2f}")
