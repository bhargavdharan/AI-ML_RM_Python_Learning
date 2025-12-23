# ===============================================
# LESSON 4 : STRINGS - LIVE EXAMPLES
# ===============================================

print("\n" + "=" * 70)
print("LESSON 4 : WORKING WITH STRINGS")
print("=" * 70)

# Example 1: Creating Strings
print("\n---- Example 1 : Creating Strings ----")
name = "Dharan"
city = 'bengaluru'
message = """This is a
multi line string
"""

print("Name:", name)
print("City:", city)
print("Message:", message)

# Example 2: String Concatenation (combining strings)
print("\n---- Example 2 : String Concatenation ----")
first_name = "Dharan"
last_name = "Bera"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

greetings = "Hello, " + "World!"
print("Greetings:" , greetings) 

# Example 3: String Repetition
print("\n---- Example 3 : String Repetition ----")
print("Ha" * 5) # Repeat 'Ha' 5 times
print("Python! " * 3) # Repeat 'Python! ' 3 times
print("-" * 40)

# Example 4: String length
print("\n---- Example 4 : String Length - Len() ----")
text = "Python"
print("Text: ", text)
print("Length of the text: ", len(text))  # Using len() to get length of string

password = "mypass123"
print("\n Password:", password)
print("Length of the password: ", len(password))

# Example 5: Indexing (accessing characters by position)
print("\n---- Example 5 : String Indexing ----")
word = "PYTHON"
print("word:", word)
print("Index 0: ", word[0])   # First character
print("Index 1: ", word[1])   # Second character
print("Index -1: ", word[-1]) # Last character (negative index)
print("Index -2: ", word[-2]) # Second last character (negative index)

# Example 6: Slicing (extracting parts)
print("\n---- Example 6 : String Slicing ----")
text = "Hello, AI World!"
print("Text :", text)
print("First 5 characters: ", text[0:5])    # Characters from index 0 to 4
print("Characters from 6-10", text[6:10]) # Characters from index 6 to 10
print("From 6 to end:", text[6:])        # From index 6 to end
print("Up to index 5:", text[:5])        # From start to index 4
print("Last 5:", text[-5:])         # Characters from index 5 to end
print("Full string:", text[:])            # Full string

# Example 7: String methods - Case Conversion
print("\n---- Example 7 : String Methods - Case Conversion ----")
message = "I love Python"
print("Orginal Message:", message)
print("Uppercase:", message.upper())  # Convert to uppercase
print("Lowercase:", message.lower())  # Convert to lowercase
print("Title Case:", message.title())  # Convert to title case
print("Swap Case:", message.swapcase())  # Swap case (lower to upper and vice versa)
print("Capitalized:", message.capitalize())  # Capitalize first letter

# Example 8: String methods - Stripping and Replacing
print("\n---- Example 8 : String Methods - Stripping and Replacing ----")
text = "    Hello Python    "
print("Orginial: '" + text + "'")
print("Strip: '", text.strip(), "'") #Remove leading and trailing whitespace
print("Left strip: '", text.lstrip(), "'")  # Remove leading whitespace
print("Right strip: '", text.rstrip(), "'") # Remove trailing whitespace

text2 = "I love Java!"
print("\nOriginal Text2:", text2)
print("Replace 'Java' with 'Python':", text2.replace("Java", "Python")) # Replace substring

# Example 9: Split (converting string to list)
print("\n---- Example 9 : String Methods - Split ----")
sentence = "Python is great for AI and ML"
print("Sentence:", sentence)
words = sentence.split()  # Split by whitespace
print("Words List:", words)
print("Also can be listed in this way as well (explicitly):", sentence.split(" ")) # Split by space explicitly

csv_data = "apple,banana,cherry,date"
print("\nCSV Data:", csv_data)
print("Items List: ", csv_data.split(","))  # Split by comma

# Example 10: Join (Combining list to string)
print("\n---- Example 10 : String Methods - Join ----")
words = ["Python", "is", "awesome"] # List of words
print("Fruits List:", words)
sentence = " ".join(words)  # Join with space separator
print("Joined Sentence:", sentence)


items = ["apple", "banana", "cherry"]
print("\nItems List:", items)
result = " \n".join(items)  # Join with newline separator
print("Joined Items with Newline:\n", result)

# Example 11: Finding Substrings
print("\n---- Example 11 : String Methods - Finding Substrings ----")
text = "Welcome to AI Learning with Python"
print("Text:", text)
print("Index of 'AI':", text.find("AI"))  # Find index of substring
print("Index of 'Python':", text.find("Python"))  # Find index of substring
print("Index of 'Java':", text.find("Java"))  # Substring not found returns -1
print("Count of 'a':", text.count("a"))  # Count occurrences of substring
print("Count of 'AI':", text.count("AI"))  # Count occurrences of substring

# Example 12: Checking contents
print("\n---- Example 12 : String Methods - Checking Contents ----")
text = "Python 3.8 is awesome!"
print("Text:", text)
print("Is alphanumeric?:", text.isalnum())  # Check if all characters are alphanumeric
print("Is alphabetic?:", text.isalpha())    # Check if all characters are alphabetic
print("Is digit?:", text.isdigit())          # Check if all characters are digits

print("Contains 'Python':", "Python" in text)  # Check if substring exists
print("Contains 'Java':", "Java" in text)      # Check if substring exists
print("Starts with 'Py': ", text.startswith("Py"))  # Check if starts with substring
print("Ends with 'awesome!': ", text.endswith("awesome!"))  # Check if ends with substring

# Example 13: String formatting with f-strings
print("\n---- Example 13 : String Formatting with f-strings ----")
name = "Dharan"
age = 25
print(f"My name is {name} and I am {age} years old.")  # f-string method
height = 5.9
print(f"{name} is {height} feet tall.")  # f-string with float

# Example 14: Checking string type
print("\n---- Example 14 : Checking String Type ----")
text1 = "12345"
text2 = "Hello"
text3 = "Hello123"

print(f"Is '{text1}' numeric?:", text1.isnumeric())  # Check if numeric
print(f"Is '{text2}' numeric?:", text2.isnumeric())  # Check if numeric
print(f"Is '{text2}' alphabetic?:", text2.isalpha())  # Check if alphabetic
print(f"Is '{text3}' alphanumeric?:", text3.isalnum())  # Check if alphanumeric

# Example 15: Count Occurences
text = "Python is fun. Python is easy to learn. Python is powerful."
print("\n---- Example 15 : Count Occurrences ----")
print("Text:", text)
print("Count of 'Python':", text.count("Python"))  # Count occurrences of 'Python'
print("Count of 'is':", text.count("is"))          # Count occurrences of 'is'
print("Count of 'fun':", text.count("fun"))        # Count occurrences of 'fun'
print("Find 'Fun':", text.find("Fun"))          # Find 'Fun' (case-sensitive), returns -1 if not found
print("Find 'fun':", text.find("fun"))          # Find 'fun' (case-sensitive)
print("Find 'python':", text.find("python"))      # Find 'python' (case-sensitive), returns -1 if not found

# Example 16: Real-world use - Email Validation
print("\n---- Example 16 : Real-world Use - Email Validation ----")
email = "bhargavdharan20@gmail.com"
print("Email:", email)

print("Contains '@':", "@" in email) # Check if email contains '@'
print("Conatains '.':", "." in email) # check if email contains '.'

# Example 17: Real-world use - File Extension Check
print("\n---- Example 17 : Real-world Use - File Extension Check ----")
filename = "report.pdf"
print("Filename:", filename)
print("Is PDF file?:", filename.endswith(".pdf"))  # Check if file is a PDF
print("Is TXT file?:", filename.endswith(".txt"))  # Check if file is a TXT

# Example 18: AI/ML - Text Preprocessing
print("\n---- Example 18 : AI/ML Use - Text Preprocessing ----")
raw_text = "   Machine Learning is AMAZAING!   "

print("Raw Text:'" + raw_text + "'")

# clean the text
cleaned = raw_text.strip().lower()
print("Cleaned: ", cleaned)

# remove punctuation
cleaned = cleaned.replace("!","")
print("Without Punctuation:", cleaned)

# word correction (simple example)
corrected = cleaned.replace("amazaing", "amazing")
print("Corrected Text:", corrected)

# Example 19: Real-world use - Generating a Report Header
print("\n---- Example 19 : Real-world Use - Report Header ----")
title = "AI Learning Report"
author = "Dharan Bera"
date = "2024-06-15"
header = f"{title}\nAuthor: {author}\nDate: {date}\n" + "="*40
print(header)

# Example 20: Escaping Characters
print("\n---- Example 20 : Escaping Characters ----")
print("He said, \"Hello, World!\"")  # Using \" to include double quotes
print('It\'s a beautiful day!')        # Using \' to include single quote
print("This is a backslash: \\")       # Using \\ to include a backslash
print("First Line\nSecond Line")       # Using \n for newline
print("Column1\tColumn2\tColumn3")    # Using \t for tab spacing
print("C:\\Users\\Dharan\\Documents") # File path with backslashes

print("\n" + "=" * 70)
print("Lesson 4 Examples Completed Successfully!")
print("=" * 70)