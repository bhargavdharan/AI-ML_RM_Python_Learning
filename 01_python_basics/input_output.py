name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
checkmarried = bool(int(input("Are you married? (1 for Yes, 0 for No): ")))

print("Hello,", name)
print("Next year you will be", age + 1)
print("Your salary after a 10% raise will be:", salary * 1.10)
print("Married status:", checkmarried)
