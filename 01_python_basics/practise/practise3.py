# Level 3

# Expression evaluation

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))
result = a + b * c
print("Result of a + b * c:", result)

result1 = (a + b) * c
print("Result of (a + b) * c:", result1)

# order of operations: ( ) --> * / // % --> + - --> << >> --> & --> ^ --> | --> ~ --> comparison operators --> equality operators --> assignment operators --> logical operators 
# parentheses have the highest precedence
# parentheses -> multiplication -> addition -> assignment -> logical operators -> print -> end of expression -> end of program


# End of the code