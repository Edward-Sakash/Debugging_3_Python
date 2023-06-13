"""three_mul = 'fizz  # Missing closing quotation mark

five_mul = 'buzz'  # Missing closing quotation mark

num1 = 3  # Correct

num2 = 4  # Correct

max_num = 100  # Variable name mismatch (max_number instead of max_num)

for i in range(1, max_number):  # Undefined variable (max_number instead of max_num)

    if i % num1 = 0:  # Syntax error, should use == for equality comparison instead of =
        print(i, three_mul)

    elif i % num2 == 0:  # Correct
        print(i, five_mul)

    elif i % num1 == 0 and i % num2 == 0:  # Correct indentation but logic error, this condition will never be true
    print(i, three_mul+five_mul)  # Incorrect indentation, should be aligned with the if statement
"""

three_mul = 'fizz'  # Added closing quotation mark

five_mul = 'buzz'  # Added closing quotation mark

num1 = 3  # Correct

num2 = 5  # Correct

max_num = 100  # Variable name mismatch (max_number instead of max_num)

for i in range(1, max_num+1):  # Fixed variable name to max_num and adjusted range end value

    # % or modulo division gives you the remainder 
    
    if i % num1 == 0 and i % num2 == 0:  # Check if divisible by both num1 and num2 first
        print(i, three_mul + five_mul)

    elif i % num1 == 0:  # Check if divisible by num1
        print(i, three_mul)

    elif i % num2 == 0:  # Check if divisible by num2
        print(i, five_mul)

    else:  # If not divisible by num1 or num2, print the number itself
        print(i)
