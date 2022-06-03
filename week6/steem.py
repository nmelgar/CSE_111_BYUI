intro_message = """
This program is an implementation of the Rosenberg Self-Esteem Scale.
This program will show you ten statements that you could possibly apply to yourself.
Please rate how much you agree with each of the statements by responding with one of these four letters:
"""

options = """
D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
"""

print(intro_message)
print(options)

statement_1 = input(
    "\n1. I feel that I am a person of worth, at least on an equal plane with others. ")
statement_2 = input("\n2. I feel that I have a number of good qualities. ")
statement_3 = input(
    "\n3. All in all, I am inclined to feel that I am a failure. ")
statement_4 = input(
    "\n4. I am able to do things as well as most other people. ")
statement_5 = input("\n5. I feel I do not have much to be proud of. ")
statement_6 = input("\n6. I take a positive attitude toward myself. ")
statement_7 = input("\n7. On the whole, I am satisfied with myself. ")
statement_8 = input("\n8. I wish I could have more respect for myself. ")
statement_9 = input("\n9. I certainly feel useless at times. ")
statement_10 = input("\n10. At times I think I am no good at all. ")
