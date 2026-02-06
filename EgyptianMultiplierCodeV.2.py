"""
Project II:  An implementation of the so-called "Russian Peasant" or "Ancient
             Egyptian" method for multiplication.

File Name:   multiplier.py
Name:        ?
Course:      CPTR 141
Code Review:
"""
import math

# user input, a is left side being doubled, b is right side being cut in half
a = 0
b = 0

# ensures program does not continue until integer is inputted
while True:  
    try:
        a = int(input("First integer: "))
        b = int(input("Second integer: "))
        break
    except ValueError:
        print("Please put in an integer ")




# copies original values for final print statement
x = a
y = b

# answer for verification
print(a * b)
print("")

# if statements to fix things with negative numbers
if b < 0 and a > 0:
    a *= -1
    b = int(math.fabs(b))
if b < 0 and a < 0:
    a = int(math.fabs(a))
    b = int(math.fabs(b))

# Loop to run numbers through, repeatedly multipliying one number and dividing the other
sum_List = []


# arbitrary for loop range to ensure complete multiplication
for i in range(1000000):

    # checks if algorithm has completed
    if b == 1 or b == -1:
        sum_List.append(a)
        print(f"{a:12.0f} : {b}")
        break

    # checks for odd values in b variable and stores corresponding a value
    if b % 2 == 1:
        sum_List.append(a)

    # computational section, outputs old a and b into "table", then updates values for next iteration
    print(f"{a:12.0f} : {b}")
    a *= 2
    
    b = b // 2
    

# prints answer
print("")
print(f"{x} * {y} is equal to {int(math.fsum(sum_List))}")
print(sum_List)
