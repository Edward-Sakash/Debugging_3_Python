x = int(input("First number: "))  # Added int() to convert input to integers
y = int(input("Second number: "))  # Added int() to convert input to integers
z = int(input("Third number: "))  # Added int() to convert input to integers

if x == y or y == z or x == z:  # Fixed the comparison operators to '==' for equality check
    result = 0
else:
    result = x + y + z  # Changed 'sum' variable to 'result' to avoid shadowing the built-in function

print("Calculated sum is", result)
