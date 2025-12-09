# Level 4

# Age Calculator
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

afteryears = int(input("Enter number of years to see your age after that period: "))
age += afteryears

print(f"You will be {age} years old after {afteryears} years.")

# Simple Interest Calculator
Total_Amount = float(input("Enter the total amount (Principal): "))
Rate_of_Interest = float(input("Enter the rate of interest (in %): "))
Time_Period = float(input("Enter the time period (in years): "))
Simple_Interest = (Total_Amount * Rate_of_Interest * Time_Period) / 100

print(f"The Simple Interest is: {Simple_Interest}")
print(f"The Total Amount after {Time_Period} years will be (SI): {Total_Amount + Simple_Interest}")

# Compound Interest Calculator
Comound_Interest = Total_Amount * ( (1 + Rate_of_Interest / 100) ** Time_Period ) - Total_Amount
print(f"The Compound Interest is: {Comound_Interest}")
print(f"The Total Amount after {Time_Period} years will be (CI): {Total_Amount + Comound_Interest}")

# Temperature Calculator
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} C is equal to {fahrenheit} F")
'''
if celcius 0-100 then it is normal temperature we dont need to wear jacket
if celcius >100 then it is high temperature we need to wear light clothes
if celcius <0 then it is low temperature we need to wear heavy clothes
'''