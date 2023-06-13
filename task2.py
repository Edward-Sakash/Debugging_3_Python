"""our task is to fix program non-working correctly.
The problem:

sum integers from 1 to 5 using while loop
calculate what result should be and what you get after running the program
Program with bug:

n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + 1
    number = number + 1
print("Sum =", sum)
Find the bug and fix it 😃

Your result could look like this:
Sum = 15"""

# Solution
n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number  # Fixed bug: Add the value of 'number' to 'sum'
    number = number + 1
print("Sum =", sum)
