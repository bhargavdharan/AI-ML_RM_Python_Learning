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

The **print()** Function

The print() function displays text or numbers on the screen

Syntax:
```python
print("your message")
```

- Use quotes for text: "Hello" or 'Hello'
- No quotes for numbers: 42 or 3.15
- Parenthesis () are required

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

What are Variables ?

Variables are **containers** that store data. Think of them as labeled boxes where you keep information.

(or)

A variable is a named storage location that holds a value in memory.

Why we use variables ?
- Stores data for later use
- Make code reusable
- Make calculations easier

Creating Variables

Syntax:

```python
varaible_name = value
```

Rules for naming varaibles:
- Must start with a letter or underscore: name, _age
- can contain letters, numbers, underscores: user1, my_store
- case-sensitive: Name != name
- No spaces: use my_name not my name
- Can't use python keywords: print, if, for

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

### Basic Data Types

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

### Comments

Comments are lines in the code that are ignored by the Python interpreter. They are used to explain the code for human readers.

```python
# This is a single-line comment
pi = 3.14  # A common constant
```

Comments should explain why the code exists, not just what the code does.

## Lesson 3: Operators (Math Operations)

What are Math Operations ?

Python can perfomr calculations just like a calculator. These operations are essential for AI - calculating accuracy, loss, weight, etc.

Basic Math Operators

| Operator  |Name                |Example | Result |
|:---------:|:------------------:|:------:|:------:|
| +         | Addition           | 5+3    | 8      |
| -         | Subtraction        | 10-4   | 6      |
| *         | Multiplication     | 6*7    | 42     |
| /         | Division           | 15/3   | 5.0    |
| //        | Floor Division     | 17//5  | 3      |
| %         | Modulus(Remainder) | 17%5   | 2      |
| **        | Power(Exponent)    | 2**3   | 8      |

Order of Operations (PEMDAS)
Python follows math rules:
1. **P**arenthesis ()
2. **E**xponents **
3. **M**ultiplications & **D**ivisions *, /
4. **A**ddition & **S**ubtraction +, -

Compound Assignment Operators

Shorcuts for updating variables:
- x += 5 --> same as x = x + 5
- x -= 5 --> same as x = x - 5
- x *= 5 --> same as x = x * 5
- x /= 5 --> same as x = x / 5

Comparison Operators

| Operator   |Name                 |Example    | Result |
|:----------:|:-------------------:|:---------:|:------:|
| ==         | Equal to            | 5 == 5    | True   |
| !=         | Not equal to        | 5 != 3    | True   |
| >          | Greater than        | 10 > 5    | True   |
| <          | Less than           | 3 < 7     | True   |
| >=         | Greater or equal    | 5 >= 5    | True   |
| <=         | Less or equal       | 4 <= 3    | False  |

**Important**: = assigns, == compares!

Logical Operators

| Operator   |Name                     |Example                          |
|:----------:|:-----------------------:|:-------------------------------:|
| and        | Both must be true       | (5 > 3) and (10 < 20) --> True  |
| or         | At least 1 must be true | (5 > 10) and (3 < 5) --> True  |
| not        | opposite                |  not (5 > 3) --> False          |

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

## Lesson 4: Strings

What are Strings ?

Strings are text data - any sequence of data enclosed in quotes.

Creating strigns:
```python
name = "python" # Double quotes
city = 'bengaluru' # single quotes
message = """    
"""             # Triple quotes
```

Why String Matter for AI ?
- Processing text data (NLP - Natural Language Processing)
- Reading/Writing files
- User input/output
- Data cleaning and preprocessing

String Operation
- **Concatenation** - Combining strings with +
- **Repetion** - Repeating strings with *
- **Indexing** - Accessing individual characters
- **Slicing** - Extracting parts of strings
- **Methods** - Built-in functions to manipulate strings

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