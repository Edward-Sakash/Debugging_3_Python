"""Your task is to fix program non-working correctly.
The problem:

sum the two prompted integers
however, if the sum is between 15 to 20 (both numbers included) it should be calculated to 20
calculate what result should be and what you get after running the program
Program with bugs:

x = input("First number: ")
y = input("Second number: ")

result = x + y

if result > 15 or result < 20:
    sum = 20
print("Calculated sum is ", ressult)
Find the bug and fix it 😃"""

# Solution
x = int(input("First number: "))  # Added int() to convert input to integers
y = int(input("Second number: "))  # Added int() to convert input to integers

result = x + y

if 15 <= result <= 20:  # Fixed the condition to check if the result is between 15 and 20 (inclusive)
    result = 20  # Changed 'sum' variable to 'result' to avoid shadowing the built-in function

print("Calculated sum is", result)
