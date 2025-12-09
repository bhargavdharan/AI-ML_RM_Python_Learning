# Personal Info, Salary, EMI & Savings Report
# Uses only Python basics: variables, input, type casting, arithmetic, print

print("=== Personal Info & Salary Report ===")

# Collect user input
name = input("Enter your name: ")
age_str = input("Enter your age in years: ")
city = input("Enter your city: ")
monthly_salary_str = input("Enter your monthly salary: ")
emi_str = input("Enter your total monthly EMI amount: ")
savings_percent_str = input("Enter savings percentage from remaining salary (e.g., 20 for 20%): ")

# Type casting
age = int(age_str)
monthly_salary = float(monthly_salary_str)
emi_monthly = float(emi_str)
savings_percent = int(savings_percent_str)

# Basic calculations
age_in_months = age * 12
age_in_days = age * 365  # simple approximation

annual_salary = monthly_salary * 12

# EMI calculations
emi_yearly = emi_monthly * 12
salary_after_emi_monthly = monthly_salary - emi_monthly
salary_after_emi_yearly = salary_after_emi_monthly * 12

# Simple fixed tax assumption on gross annual salary
estimated_tax = annual_salary * 0.10  # 10%

# Savings based on salary after EMI
monthly_savings = salary_after_emi_monthly * (savings_percent / 100)
yearly_savings = monthly_savings * 12

# Output report
print("\n=== Generated Report ===")
print("Name          :", name)
print("City          :", city)
print("Age (years)   :", age)
print("Age (months)  :", age_in_months)
print("Age (days)    :", age_in_days)

print("\n--- Salary Details ---")
print("Gross Monthly Salary      :", monthly_salary)
print("Gross Annual Salary       :", annual_salary)
print("Estimated Yearly Tax (10%):", estimated_tax)

print("\n--- EMI Details ---")
print("Monthly EMI Amount        :", emi_monthly)
print("Yearly EMI Amount         :", emi_yearly)
print("Monthly Salary After EMI  :", salary_after_emi_monthly)
print("Yearly Salary After EMI   :", salary_after_emi_yearly)

print("\n--- Savings Plan (from salary after EMI) ---")
print("Savings Percentage        :", savings_percent, "%")
print("Monthly Savings           :", monthly_savings)
print("Yearly Savings            :", yearly_savings)

print("\nThank you for using the Personal Info, Salary, EMI & Savings Report Generator!")
