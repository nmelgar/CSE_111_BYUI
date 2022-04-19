"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

#ask person's age
age = float(input("Please enter your age: "))

#perform the calculations
range = 220 - age
sixty_five_percent = (65 * range) / 100
eighty_five_percent = (85 * range) / 100

#print the result using an f-string
print(
    f"When you exercise to strengthen your heart, you should",
    f"keep your heart rate between {sixty_five_percent: .0f} and {eighty_five_percent: .0f} beats per minute."
)
