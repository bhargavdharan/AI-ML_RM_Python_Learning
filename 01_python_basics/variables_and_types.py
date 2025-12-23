# =========================================
# PRACTICE EXERCISES - LESSONS 1, 2
# =========================================

print("=" * 70)
print("Practise Exercises | Lessons 1, 2")
print("=" * 70)
print()
print()
# print("=" * 70)

# =========================================
# LESSON 1 : PRINT FUNCTION - LIVE EXAMPLES
# =========================================

print("\n" + "=" * 70)
print("LESSONE 1 : PRINT FUNCTION")
print("=" * 70)

# Example 1: Print simple text
print("\n---- Example 1 : Basic Text ----")
print("Hello, World!")
print("Welcome to python!")

# Example 2: Print numbers
print("\n---- Example 2 : Print Numbers ----")
print(42)
print(3.14)
print(-7)
print(2026)

# Example 3: Print multiple items (separated by commas)
print("\n---- Example 3 : Multiple Items ----")
print("My name is", "Dharan", "and I am", 25, "years old.")
print("python", "is", "awesome!")

# Example 4: Print empty line
print("\n---- Example 4 : Empty Line ----")
print("Line 1")
print()
print("Line 3")

# Example 5: Special Characters
print("\n---- Example 5 : Special Characters ----")
print("This is a line with a newline character.\nSee?") # \n for newline
print("This is a line with a tab character.\tSee?")     # \t for tab
print("He said, \"Hello!\"")                             # \" for double quote
print('It\'s a beautiful day!')                           # \' for single quote

# Example 6: Print with custom separator
print("\n---- Example 6 : Custom Separator ----")
print("apple", "banana", "cherry") # Default separator is space
print("apple", "banana", "cherry", sep=", ") # Custom separator ",")
print("2024", "06", "15", sep="-")  # Date format YYYY-MM-DD

# Example 7: Print without new line
print("\n---- Example 7 : Print without New Line ----")
print("Hello, ", end="")
print("World!")  # This will continue on the same line
print("Python ", end="***")
print("Rocks!")  # This will also continue on the same line

# Example 8: Formatted Printing
print("\n---- Example 8 : Formatted Printing ----")
name = "Dharan"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")  # f-string method

# Example 9: Repeat Printing
print("\n---- Example 9 : Repeat Printing ----")
print("Python! " * 3)  # Repeat the string 3 times
print("-" * 10)     # Print a line of 10 dashes

# Example 10: Real-world use
print("\n---- Example 10 : Real-world Use ----")
print("=================================")
print("="*50)
print("\t\t Welcome to AI Learning! Python Programming")
print("="*50)

print("="*50)
print("Student Name:\tDharan")
print("Course:\t\tPython for AI")
print("="*50)

print("Lesson 1 Examples Completed Successfully!")

# =========================================
# LESSON 2 : VARIABLES - LIVE EXAMPLES
# =========================================

print("\n" + "=" * 70)
print("LESSONE 2 : VARIABLES")
print("=" * 70)

# Example 1: Creating Variables
print("\n---- Example 1 : Creating Variables ----")
title = "Python"
version = 3.10
is_fun = True
year = 2024

# Example 2: Printing Variables
print("\n---- Example 2 : Printing Variables ----")
print("Title:", title)
print("Version:", version)
print("Is Fun:", is_fun)
print("Year:", year)

# Example 3: Using variables in calculations
print("\n---- Example 3 : Using Variables in Calculations ----")
price = 100
quantity = 5
total = price * quantity # Total cost
print("Price per item:", price)
print("Quantity:", quantity)
print("Total cost:", total)

# Example 4: Changine Variable names
print("\n---- Example 4 : Changing Variable names ----")
score = 10
print("Initial Score:", score)
score = 20 # Changing the value of score
print("Updated Score:", score)
score = score + 30 # Incrementing score
print("Final Score:", score)

# Example 5: Multple varaibles at once
print("\n---- Example 5 : Multiple Variables at Once ----")

a1, b1, c1 = 1, 2.5, "Hello"
print("a1:", a1)
print("b1:", b1)
print("c1:", c1)

print("\n---- Example 5 : Same Variables at Once ----")
a=b=c=100
print("a:", a)
print("b:", b)
print("c:", c)

# Example 6: Combining Variables and Print
print("\n---- Example 6 : Combining Variables and Print ----")
first_name = "Dharan"
last_name = "Kumar"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Example 7: Variables from other variables
print("\n---- Example 7 : Variables from Other Variables ----")
length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)
print("Length:", length)
print("Width:", width)
print("Area:", area)
print("Perimeter:", perimeter)

# Example 8: Real-world use
print("\n---- Example 8 : Real-world Use ----")
training_samples = 1000
testing_samples = 200
total_samples = training_samples + testing_samples
accuracy = (testing_samples / total_samples) * 100

print("Training Samples:", training_samples)
print("Testing Samples:", testing_samples)
print("Total Samples:", total_samples)
print(f"Accuracy: {accuracy}%")

# Example 9: Variable Types
print("\n---- Example 9 : Variable Types ----")
student_name = "Dharan"   # string
student_age = 25          # integer
student_gpa = 8.8      # float
is_graduated = True    # boolean

print("Name:", student_name, type(student_name))
print("Age:", student_age, type(student_age))
print("GPA:", student_gpa, type(student_gpa))
print("Graduated:", is_graduated, type(is_graduated))

# Example 10: Swapping Variables
print("\n---- Example 10 : Swapping Variables ----")
x = 5
y = 10
print("Before Swapping: x =", x, ", y =", y)
# Swapping
x, y = y, x
print("After Swapping: x =", x, ", y =", y)

print("="*50)
print("Lesson 2 Examples Completed Successfully!")
print("="*50)

# =========================================
# EXERCISE 1 : VARAIBLES & PRINT
# =========================================

print("\n" + "=" * 70)
print("EXERCISE 1 : VARAIBLES & PRINT")
print("=" * 70)
print("""
TASK:
      Create varaibles for your personal information and print them nicely formatted with their data types.
      - Your Name
      - Your Age
      - Your Favourite color
      - Your City

      Print them in a formatted card like this:
      =================================
      PERSONAL INFO
      =================================
      Name: [Your Name] (type: <class 'str'>)
      Age: [Your Age] (type: <class 'int'>)
      Favourite Color: [Your Favourite color] (type: <class 'str'>)
      City: [Your City] (type: <class 'str'>)
""")

print("=" * 70)
print("-"*5, "SOLUTION", "-"*5)
print("=" * 70)

# Variables
name = "Dharan"
age = 25
favorite_color = "blue"
height = 5.9
city = "bengaluru"
is_active = True
result = None

# Printing values and their types
print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Favourite Color:", favorite_color, type(favorite_color))
print(f"color: {favorite_color}, type: {type(favorite_color)}")
print("City:", city, type(city))
print("Active:", is_active, type(is_active))
print("Result:", result, type(result))
