# Swap two numbers
a = 10
b = 20
a, b = b, a
print("After swap:", a, b)

# Even or odd
num = 7
print("Even" if num % 2 == 0 else "Odd")

# Simple Interest
p = 1000
r = 5
t = 2
si = (p * r * t) / 100
print("Simple Interest:", si)

# compound interest
ci = p * (1 + r / 100) ** t - p
print("Compound Interest:", ci)
