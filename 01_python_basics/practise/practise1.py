# Variables and Data Types in Python
name = "Dharan"
age = 25
height = 5.9
areyou_student = False

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Are you a student?:", areyou_student, type(areyou_student))

# Reassigning values to variables
x = 10
print("Value of x:", x)
x = 20
print("After reassignment, value of x:", x)

# Arithmetic Operations
a = 20
b = 15

print("Addition:", a + b, type(a + b))
print("subtraction:", a - b, type(a - b))
print("multiplication:", a * b, type(a * b))
print("division:", a / b, type(a / b))
print("floor division:", a // b, type(a // b))
print("modulus:", a % b, type(a % b))
print("exponent:", a ** b, type(a **b))

# Type Casting
tc = "Hello, Mike!"
print("before casting:", tc, type(tc))

# Throws an error due to string cannot be converted to int, float (value error)
# value error occurs when the data type conversion is not possible
'''
tc1 = int(tc)
print("after casting to int:", tc1, type(tc1))
'''

'''
tc2 = float(tc)
print("after casting to float:", tc2, type(tc2))
'''

tc_ = 25
print("before casting:", tc_, type(tc_))

tc1_ = str(tc_)
print("after casting to str:", tc1_, type(tc1_))

# str --> int (possible only if the string contains numeric characters)
tc2_ = "100"
print("before casting:", tc2_, type(tc2_))

tc3_ = int(tc2_)
print("after casting to int:", tc3_, type(tc3_))

tc_bool = 10
print("before casting:", tc_bool, type(tc_bool))
tc4_ = bool(tc_bool)
print("after casting to bool:", tc4_, type(tc4_))

tc_bool = 0
print("before casting:", tc_bool, type(tc_bool))
tc5_ = bool(tc_bool)
print("after casting to bool:", tc5_, type(tc5_))


# End of the code
