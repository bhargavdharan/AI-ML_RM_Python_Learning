# =========================================
# LESSON 3 : MATH OPERATORS - LIVE EXAMPLES
# =========================================

print("\n" + "=" * 70)
print("LESSONE 3 : MATH OPERATORS")
print("=" * 70)

# Example 1: Basic Operations
print("\n---- Example 1 : Basic Operations ----")
print("Addition: 10 + 5 =", 10 + 5)
print("Subtraction: 10 - 5 =", 10 - 5)
print("Multiplication: 10 * 5 =", 10 * 5)
print("Division: 10 / 5 =", 10 / 5)

# Example 2: Floor Division, Modulus
print("\n---- Example 2 : Floor Division, Modulus ----")
print("Division: 10 / 3 =", 10 / 3) # Regular Division
print("Floor Division: 10 // 3 =", 10 // 3) # Floor Division (no decimal)
print("Modulus: 10 % 3 =", 10 % 3) # Remainder (no decimal)

print("\nPractical use:")
print(" 25 students, 4 per group")
total_students = 25
students_per_group = 4
print("Number of full groups formed:", total_students // students_per_group)
print("Students without a group:", total_students % students_per_group)

# Example 3: Exponentiation
print("\n---- Example 3 : Exponentiation ----")
print("2 ** 3 =", 2 ** 3) # 2 raised to the power of 3
print("5 ** 4 =", 5 ** 4) # 5 raised to the power of 4
print("9 ** 0.5 =", 9 ** 0.5) # Square root of 9

# Example 4: Order of Operations
print("\n---- Example 4 : Order of Operations ----")
result1 = 10 + 5 * 2
result2 = (10 + 5) * 2
print("10 + 5 * 2 =", result1) # Multiplication first (PAMDAS/BODMAS rule)
print("(10 + 5) * 2 =", result2) # Parentheses first (PAMDAS/BODMAS rule)

result3 = 10 + 5 * 2 ** 3 - 4 # Complex expression
print("10 + 5 * 2 ** 3 - 4 =", result3) # Follows order: Exponentiation, Multiplication, Addition, Subtraction

# Example 5: Using Variables with Operators
print("\n---- Example 5 : Using Variables with Operators ----")
price = 100
tax_rate = 0.08
tax = price * tax_rate
total = price + tax

print("Price:", price)
print("Tax Rate:", tax_rate)
print("Tax Amount:", tax)
print("Total Price:", total)

# Example 6: Compound Assignment Operators
print("\n---- Example 6 : Compound Assignment Operators ----")
count = 10
print("Initial Count:", count)

count += 5
print("After count += 5:", count)

count *= 2
print("After count *= 2:", count)

count -= 4
print("After count -= 4:", count)

count //= 3
print("After count //= 3:", count)

# Example 7: Real-world case
print("\n---- Example 7 : Real-world Case ----")
meal_cost = 80.50
tip_percentage = 0.20
tip = meal_cost * tip_percentage
total_bill = meal_cost + tip

print("Meal Cost: (Rs)", meal_cost)
print(f"Tip Percentage: {tip_percentage * 100}%")
print("Tip Amount: (Rs)", tip)
print("Total Bill: (Rs)", total_bill)

# Example 8: Temperature Conversion
print("\n---- Example 8 : Temperature Conversion ----")
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"Celsius: {celsius} C", f"fahrenheit: {fahrenheit} F")

# Example 9: Circle Calculations
print("\n---- Example 9 : Circle Calculations ----")
radius = 7
pi = 3.14159

area = pi * (radius ** 2)
circumference = 2 * pi * radius

print("Radius:", radius)
print("Area:", area)
print("Circumference:", circumference)

# Example 10: Average Calculation
print("\n---- Example 10 : Average Calculation ----")
test1 = 85
test2 = 90
test3 = 78
test4 = 92

average = (test1 + test2 + test3 + test4) / 4
print("Test Scores:", test1, test2, test3, test4)
print("Average Score:", average)

# Example 11: Checking Even or Odd
print("\n---- Example 11 : Checking Even or Odd ----")
number1 = 10
number2 = 7

print(number1, "% 2 =", number1 % 2, "->, \"Even\" (remainder is 0)")
print(number2, "% 2 =", number2 % 2, "->, \"Odd\" (remainder is 1)")

# =======================================================
# Part 2 : Comparison and Logical Operators
# =======================================================

print("\n" + "=" * 70)
print("Part 2 : Comparison and Logical Operators Examples")
print("=" * 70)

# Example 1: Comparison Operators
print("\n---- Example 1 : Comparison Operators ----")
print("5 == 5 :", 5 == 5)   # Equal to, returns True
print("5 == 3 :", 5 == 3)   # Equal to, returns False

print("10 != 5 :", 10 != 5) # Not equal to, returns True
print("10 != 10 :", 10 != 10) # Not equal to, returns False

print("7 > 3 :", 7 > 3)     # Greater than, returns True
print("3 > 7 :", 3 > 7)     # Greater than, returns False
print("4 < 6 :", 4 < 6)     # Less than, returns True
print("6 < 4 :", 6 < 4)     # Less than, returns False
print("8 >= 8 :", 8 >= 8)   # Greater than or equal to, returns True
print("5 <= 2 :", 5 <= 2)   # Less than or equal to, returns False

# Example 2 : Comparing Variables
print("\n---- Example 2 : Comparing Variables ----")
age = 14
required_age = 18

print("Age:", age)
print("Required Age:", required_age)
print(f"Is eligible to vote? : {age >= required_age}")

score = 85
passing_score = 50
print("Score:", score)
print("Passing Score:", passing_score)
print(f"Has passed the exam? : {score >= passing_score}")

# Example 3 : String comparisons
print("\n---- Example 3 : String Comparisons ----")
password = "python123"
user_input = "python123"

print("Password:", password)
print("User Input:", user_input)
print(f"Is password correct? : {password == user_input}")

name1 = "Alice"
name2 = "Bob"
print("Name 1:", name1)
print("Name 2:", name2)
print(f"Are names same? : {name1 == name2}")
print(f"Are names different? : {name1 != name2}")

# Example 4 : Logical Operators
print("\n---- Example 4 : Logical Operators ----")

print("And Operator:")
age = 20
has_license = True
print(f"Is eligible to drive? : {age >= 18 and has_license}")

print("\nOr Operator:")
temperature = 30
is_raining = False
print(f"Is it a good day for a walk? : {temperature >= 20 or not is_raining}")

print("\nNot Operator:")
is_sunny = True
print(f"Is it not sunny? : {not is_sunny}")

# Example 5 : Combining multiple conditions
print("\n---- Example 5 : Combining Multiple Conditions ----")
age = 25
income = 50000
credit_score = 720

print("Age:", age)
print("Income:", income)
print("Credit Score:", credit_score)
eligible = (age >= 18) and (income >= 30000) and (credit_score >= 700)
print(f"Is eligible for loan? : {eligible}")

# Example 6 : Real-world case
print("\n---- Example 6 : Real-world Case ----")
correct_username = "admin"
corrrect_password = "pass123"

username = "admin"
password = "pass123"

login_success = (username == correct_username) and (password == corrrect_password)

print("Username:", username)
print("Password:", password)
print(f"Login Successful? : {login_success}")

# Example 7 : AI Model Evaluation
print("\n---- Example 7 : AI Model Evaluation ----")
accuracy = 92
precision = 88
recall = 85

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

good_model = (accuracy >= 90) and (precision >= 85) and (recall >= 80)
print(f"Is the AI model good? : {good_model}")

excellent_model = (accuracy >= 95) and (precision >= 95) and (recall >= 95)
print(f"Is the AI model excellent? : {excellent_model}")

# Example 8 : Grade Checker
print("\n---- Example 8 : Grade Checker ----")
score = 75
print("Score:", score)
print("Failed? :", score < 50)
print("Passed? :", score >= 50 and score < 75)
print("Distinction? :", score >= 75 and score <=90)
print("Excellent? :", score >= 90)


print("=" * 70)
print("Math Operators Examples Completed Successfully!")
print("=" * 70)


a = 10
b = 3

# Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

'''
/ → Division (True Division)

What it does
Divides two numbers
ALWAYS returns a float
Keeps the decimal part

📌 Rule to remember

/ = normal mathematical division → output is always decimal
'''

print("Division:", a / b)

'''
// → Floor Division

What it does
Divides two numbers
Removes the decimal part
Returns the quotient only

📌 Rule to remember

// = how many full times b fits into a (floor value)
'''
print("Floor Division:", a // b)

'''
% → Modulus (Remainder)

What it does

Returns the remainder after division

📌 Rule to remember

% = what’s left after dividing
'''
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison operators
print("a > b:", a > b)
print("a == b:", a == b)
print("a != b:", a != b)

# Logical operators
x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)


print("=" * 70)
print("Practise Exercises | Lessons 2")
print("=" * 70)
print()
print()
print("=" * 70)

# =========================================
# EXERCISE 2 : MATH OPERATIONS
# =========================================

print("\n" + "=" * 70)
print("EXERCISE 2 : SHOPPING CALCULATOR")
print("=" * 70)
print("""
TASK:
      You're buying items at a store:
      - Item 1 : 25 Rs
      - Item 2 : 40 Rs
      - Item 3 : 15 Rs

      Calculate:
        1. Total cost of items
        2. If you have 100 Rs, how much change will you get ?
        3. If there's a 10% discount on total cost, what will be the new total ?
        4. How much did you save with the discount ? 
""")

print("=" * 70)
print("-"*5, "SOLUTION", "-"*5)
print("=" * 70)

item1 = 25
item2 = 40
item3 = 15

total = item1 + item2 + item3
money_have = 100
change = money_have - total
discount_percent = 10
discount_amount = total * discount_percent / 100
final_price = total - discount_amount
savings = discount_amount
Rem_money_have = money_have - final_price

print(f"Item 1: {item1} Rs")
print(f"Item 2: {item2} Rs")
print(f"Item 3: {item3} Rs")
print(f"Total: {total} Rs")
print(f"Total Money I have: {money_have} Rs")
print(f"Change: {change} Rs")
print(f"Discount Percent: {discount_percent} %")
print(f"Discount Amount: {discount_amount} Rs")
print(f"Final Price after discount: {final_price} Rs")
print(f"Savings: {savings} Rs")
print(f"Remaining Money I have: {Rem_money_have} Rs")