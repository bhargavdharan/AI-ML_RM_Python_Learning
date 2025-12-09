# Level 2

# Input + Casting
number = input("Enter a number: ")

# Attempting to perform arithmetic operation on string input throws an error (TypeError)
# Type error occurs when an operation is performed on incompatible data types
# print("Square of the number (as string):", number * number)  # This will cause an error

# Correct way: Cast the input to integer
number_int = int(number)
print("Square of the number (as integer):", number_int * number_int)
print("Square of the number (as integer) using exponentiation:", number_int ** 2)
print("Cube of the number (as integer):", number_int ** 3)

# Even or Odd
if number_int % 2 == 0:
    print(f"{number_int} is an Even number.")
else:
    print(f"{number_int} is an Odd number.")

# Division, Floor Division, and Modulus with another input
num1 = int(input("Enter first number for division: "))
num2 = int(input("Enter second number for division: "))

print("Division (num1 / num2):", num1 / num2)
print("Floor Division (num1 // num2):", num1 // num2)
print("Modulus (num1 % num2):", num1 % num2)