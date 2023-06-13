"""Your task is to fix program non-working correctly.
The problem:

there are 4 short programs with loops, that should print some numbers, but they don't work at all!
Program no. 1 with the bug:

for x in range(3)
    print(x)
Find the bug and fix it 😃

Your result could look like this:
0
1
2"""

# Solution for programm 1
for x in range(3):  # Added a colon at the end of the line
    print(x)

# Solution for programm 2
for j in range(5):
    print("This is loop number", j)  # Added comma after the string and removed f-string formatting

print("______________________________________________")
for j in range(5):
    print(f"This is loop number {j}")  # Used f-string formatting to interpolate j

# Solution for 3
x = 10  # Moved the variable initialization before the while loop

while x > 0:
    print(x)
    x -= 1

print("______________________________________________")

# Solution for 4

countdown = 5  # Set countdown to the desired starting value

while countdown > 0:  # Modified the while condition to countdown > 0
    print(countdown)
    countdown -= 1
else:
    print("Start!")

