"""Your task is to fix program non-working correctly.
The problem:

prompt three float numbers and determine the largest and the smallest one
calculate what result should be and what you get after running the program
Program with bugs:

x == input("First number: ")
y == input("Second number: ")
z == input("Third number: ")

print("The maximum value is ", (x, y ,z))
print("The minimum value is ", abs(x, y ,z))
Find the bug and fix it 😃

Your result could look like this:
First number: 6
Second number: 7
Third number: 7

The maximum value is  7.0
The minimum value is  6.0"""

# Solution
x = float(input("First number: "))  # Changed '==' to '=' to assign the value to x
y = float(input("Second number: "))  # Changed '==' to '=' to assign the value to y
z = float(input("Third number: "))  # Changed '==' to '=' to assign the value to z

max_value = max(x, y, z)  # Used the max() function to determine the maximum value
min_value = min(x, y, z)  # Used the min() function to determine the minimum value

print("The maximum value is", max_value)
print("The minimum value is", min_value)
