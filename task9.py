"""Your task is to fix program non-working correctly.
The problem:

prompt value from the user and assign it to some variable
if given value is 0 (zero) convert it to False and if given value is 1 convert it to True
display results
Program with bugs:

x = input("Type your value: )

if x = 0:
    x = false
elif x = 1:
    x = true
else:
pass

print("Your entered value is now ", x)
Find the bug and fix it 😃

Your result could look like this:
Type your value: 0
Your entered value is now  False

Type your value: 1
Your entered value is now  True

Type your value: hi!
Your entered value is now  hi!"""

# Solution
x = input("Type your value: ")  # Added closing parenthesis to complete the input function call

if x == '0':  # Fixed the comparison operator to '==' for equality check
    x = False  # Changed 'false' to False to assign the boolean value
elif x == '1':  # Fixed the comparison operator to '==' for equality check
    x = True  # Changed 'true' to True to assign the boolean value
else:
    pass  # Added a placeholder pass statement to avoid an indentation error

print("Your entered value is now", x)
