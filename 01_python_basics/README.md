# 🐍 Python Basics – From Zero









This module introduces Python programming from the absolute beginning.  
No prior programming knowledge is required.

By the end of this module, you will be able to:
- Understand how Python programs work
- Write basic Python code confidently
- Move comfortably to control flow and data structures

## 📌 Lesson 0: What is Python?

Python is a high-level, interpreted programming language.  
- **High-level**: easy to read and write (closer to human language).  
- **Interpreted**: executed line by line, which makes debugging easier.  
- **General-purpose**: used for web development, data science, AI, automation, and more.  

Python emphasizes readability and simplicity through a clean syntax.

## Lesson 1: Running Your First Python Program

A Python program is written in a file that typically ends with the `.py` extension.  

**Example:** `hello_python.py`  

```python
print("Hello, Python")
```

Run using the command line:

```bash
python hello_python.py
```

If the output Hello, Python appears, your Python environment is working correctly.

## Lesson 2: Variables (Storing Data)

A variable is a named storage location that holds a value in memory.

```python
name = "Dharan"
age = 25
```

The = sign is the assignment operator (it assigns the value on the right to the variable on the left).

Variables can be reassigned to a new value:

```python
# Initial assignment
age = 25

# Reassignment
age = 26
```

Python automatically determines the data type of the value stored.

## Lesson 3: Basic Data Types

Python provides several essential built-in data types:

| Type  | Example          | Description                              |
|-------|------------------|------------------------------------------|
| `int` | `10`, `-5`       | Whole numbers (integers)                 |
| `float` | `3.14`, `0.01` | Decimal numbers                          |
| `str` | `"hello"`, `'Python'` | Text (sequence of characters)       |
| `bool`| `True` / `False` | Logical values (must be capitalized)     |
| `None`| `None`           | Represents no value or the absence of a value |

You can check a variable's type using the built-in function type():

```python
type(10)      # <class 'int'>
type("hello") # <class 'str'>
```

## Lesson 4: Comments

Comments are lines in the code that are ignored by the Python interpreter. They are used to explain the code for human readers.

```python
# This is a single-line comment
pi = 3.14  # A common constant
```

Comments should explain why the code exists, not just what the code does.

## Lesson 5: Operators
Operators perform operations on values and variables.

**Arithmetic Operators**

Used for mathematical calculations:

```python
+  # Addition
-  # Subtraction
*  # Multiplication
/  # Division (always returns a float)
// # Floor Division (returns an integer quotient)
%  # Modulus (returns the remainder)
** # Exponentiation (power)
```

Example:

```python
10 // 3   # 3 (Integer part of the division)
10 % 3    # 1 (Remainder of 10 divided by 3)
```

**Comparison Operators**
Used to compare two values. They always return a Boolean value (True or False).

```python
== # Equal to
!= # Not equal to
>  # Greater than
<  # Less than
>= # Greater than or equal to
<= # Less than or equal to
```

Example:

```python
10 > 5              # True
"apple" == "Apple"  # False (case-sensitive)
```

**Logical Operators**

Used to combine conditions:

```python
and  # True if BOTH conditions are True
or   # True if AT LEAST ONE condition is True
not  # Inverts the Boolean value (True becomes False, and vice-versa)
```

## Lesson 6: Type Casting
Type casting (or type conversion) converts a value from one data type to another.

```python
# age is a string
age = "25"

# Cast age to an integer
age = int(age)  # age is now the integer 25
```

Common Conversion Functions:

int(): Converts to integer.
float(): Converts to decimal/float.
str(): Converts to text/string.
bool(): Converts to boolean.

Important: Python does not automatically convert strings to numbers. You must explicitly use int() or float() when needed.

## Lesson 7: Taking Input from User
The input() function prompts the user and reads a line of text from the console.

```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

Key point: input() always returns a string.

Convert when required: To use the input as a number, you must cast it:

```python
age = int(input("Enter age: "))
# You can now safely perform calculations with the 'age' variable.
```

## Lesson 8: Printing Output

The print() function displays output to the console.

```python
name = "Dharan"
print("Hello", name, "!")
```

Features of print():

It automatically adds a space between the values passed to it (like "Hello" and "Dharan").
It ends with a newline character by default (each print starts on a new line).
It is crucial for interaction and debugging.

## Lesson 9: Expressions & Evaluation

An expression is a combination of values, variables, and operators that the Python interpreter evaluates to produce a result.

Python evaluates expressions based on operator precedence (e.g., multiplication before addition).

```python
x = 10 + 5 * 2   # The result is 20, not 30.
# 1. 5 * 2 = 10 (Multiplication/Division)
# 2. 10 + 10 = 20 (Addition/Subtraction)
```

## Lesson 10: Simple Programs

Swap Two Numbers
This is the standard, clean Python way to swap values:

```python
a = 10
b = 20
a, b = b, a  # a is now 20, b is now 10
```

Check Even or Odd
Using the Modulus operator (%) and a simple Conditional Expression:

```python
num = 7
print("Even" if num % 2 == 0 else "Odd")
```

Simple Interest Calculation
A basic formula implementation:

```python
p = 1000  # Principal
r = 5     # Rate
t = 2     # Time
si = (p * r * t) / 100
print(f"Simple Interest: {si}")
```

## Lesson 11: Common Beginner Mistakes

- Using a single equal sign = (assignment) instead of the double equal sign == (comparison).
- Forgetting to perform type conversion (int(), float()) for numerical values taken from input().
- Mixing string and number types in operations without casting (e.g., "10" + 5).
- Ignoring indentation. Python is strict about indentation; it defines code blocks (like those used later for loops and functions).