"""Your task is to fix program non-working correctly.
The problem:

prompt two values and assign them to variables a and b
write the Python program to swap these two variables
calculate what result should be and what you get after running the program
Remark: don't use "fast" swapping available in Python:

a, b = b, a
Program with bugs:

a = int("First value: ")
b = int("Second value: ")

print("Before swapping: a =", a, " ,b = b")

temp = a
a = b

print("After swapping: a =", a, " ,b =, b")
Find the bug and fix it 😃

Your result could look like this:
First value: Hello 
Second value: DCI
Before swapping: a = Hello  b = DCI
After swapping: a = DCI  b = Hello"""

# Solution
a = input("First value: ")  # Removed int() since input values are not explicitly mentioned as integers
b = input("Second value: ")  # Removed int() since input values are not explicitly mentioned as integers

print("Before swapping: a =", a, ", b =", b)  # Fixed the print statement to display the variable values correctly

temp = a
a = b
b = temp  # Fixed the assignment to swap the values correctly

print("After swapping: a =", a, ", b =", b)  # Fixed the print statement to display the variable values correctly
