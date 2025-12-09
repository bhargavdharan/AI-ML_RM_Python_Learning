# String to integer
age_str = "25"
age = int(age_str)

print("Age:", age, type(age))

# String to float
price_str = "99.5"
price = float(price_str)
print("Price:", price, type(price))

# Implicit conversion
total = 10 + 2.5
print("Total:", total, type(total))

# IMPlicit casting
a = 10
b = 2.5
print(a + b)   # 12.5

# EXPLICIT casting
age_str = "25"
age = int(age_str)
print(age + 1)  # 26

# float conversion
price = float("99.5")
print(price)

# boolean casting
print(bool(1), bool(0))
print(bool("hello"), bool(""))
print(bool([]), bool([1, 2, 3]))

