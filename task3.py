"""Your task is to fix program non-working correctly.
The problem:

sum integers from 1 to 5 using range() function
calculate what result should be and what you get after running the program
Program with bug:

n = 5
sum = 0
for num in range(n):
    sum += num
print("Sum =", sum)
Find the bug and fix it 😃

Your result could look like this:
Sum = 15"""

# Solution
n = 5
sum = 0
for num in range(1, n+1):  # Modified the range to start from 1 and include n
    sum += num
print("Sum =", sum)
