"""Your task is to fix program non-working correctly.
The problem:

accept (prompt) two integers values from the user
check whether a first number is divisible by second number and vice versa
display results
Program with bugs:

x = input("First number: ")
y = input("Second number: ")

if x %% y >= 0:
    print("First number is divisible by second number, result =", x // y)
elif y %% y != 0:
    print("Second number is divisible by first number, result =", y // x)
else:
    print("Numbers are non-divisable!")
Find the bug and fix it 😃

Your result could look like this:
First number: 5
Second number: 55
Second number is divisible by first number, result = 11.0

First number: 3
Second number: 5
Numbers are non-divisable!"""

# Solution
x = int(input("First number: "))  # Convert the input to an integer using int()
y = int(input("Second number: "))  # Convert the input to an integer using int()

if x % y == 0:  # Changed '%%' to '%' for the modulo operator and corrected the condition
    print("First number is divisible by second number, result =", x // y)  # Used '//' for integer division
elif y % x == 0:  # Changed '%%' to '%' for the modulo operator and corrected the condition
    print("Second number is divisible by first number, result =", y // x)  # Used '//' for integer division
else:
    print("Numbers are non-divisible!")  # Corrected the spelling of "non-divisible"
