# ==================================================
# PYTHON STRINGS - QUICK REVISION & METHODS GUIDE
# ==================================================

# --------------------------------------------------
# 1. CREATING STRINGS
# --------------------------------------------------

# Single quotes
s1 = 'My name is Ganesh'
print(s1)

# Double quotes (best when string has an apostrophe)
s2 = "My name is Ganesh"
s3 = "It's a beautiful day"
print(s2)
print(s3)

# Triple quotes (multiline strings)
s4 = '''My name is Ganesh
I am learning Python.'''
print(s4)

# Empty string and boolean value
empty = ""
print(bool(empty))          # False (empty string is falsy)
print(bool("Python"))       # True  (non-empty string is truthy)


# --------------------------------------------------
# 2. IMMUTABILITY & MEMORY (is vs ==)
# --------------------------------------------------

# Immutability: modifying a string creates a new object
s = "Hello"
print(s, id(s))
s = s + " World"
print(s, id(s))             # id changes because strings cannot be modified in place

# String interning: Python reuses memory for identical literals
str_a = "Python"
str_b = "Python"
print(str_a == str_b)       # True (compares values)
print(str_a is str_b)       # True (compares memory addresses)

# Difference with mutable lists
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]
print(list_a is list_b)     # True  (same reference)
print(list_a is list_c)     # False (different objects in memory)
print(list_a == list_c)     # True  (same values)


# --------------------------------------------------
# 3. INDEXING & SLICING: str[start : stop : step]
# --------------------------------------------------

# Index:   P   y   t   h   o   n
# Pos:     0   1   2   3   4   5
# Neg:    -6  -5  -4  -3  -2  -1

word = "Python"
print(word[0])              # 'P'
print(word[-1])             # 'n'

# Slicing
text = "KodNest Python"
print(text[0:7])            # 'KodNest' (stop index is excluded)
print(text[:7])             # 'KodNest' (start defaults to 0)
print(text[8:])             # 'Python'  (runs till the end)
print(text[::2])            # 'Kde yhn' (step of 2)
print(text[::-1])           # 'nohtyP tseNdoK' (reverse string)


# --------------------------------------------------
# 4. BASIC OPERATORS & FUNCTIONS
# --------------------------------------------------

a = "Maheedhar "
b = "Ganesh"
print(a + b)                # 'Maheedhar Ganesh' (concatenation)
print("Python! " * 3)       # repetition
print("Ganesh" in a + b)    # True (membership check)

print(len("Python"))        # 6 (length)
print(min("python"))        # 'h' (smallest ASCII character)
print(max("python"))        # 'y' (largest ASCII character)
print(ord('A'))             # 65 (ASCII value)
print(chr(65))              # 'A' (character from ASCII)


# --------------------------------------------------
# 5. STRING FORMATTING
# --------------------------------------------------

name = "Ganesh"
score = 98.5

# f-strings (recommended)
print(f"Name: {name}, Score: {score}")

# format() method
print("Name: {}, Score: {}".format(name, score))

# % formatting
print("Name: %s, Score: %.1f" % (name, score))


# --------------------------------------------------
# 6. ALL STRING METHODS
# --------------------------------------------------

# --- A. Case Conversion Methods ---
msg = "hello, WORld!"
print(msg.upper())          # 'HELLO, WORLD!'
print(msg.lower())          # 'hello, world!'
print(msg.capitalize())     # 'Hello, world!' (only 1st letter)
print(msg.title())          # 'Hello, World!' (every word capitalized)
print(msg.swapcase())       # 'HELLO, worLD!' (swaps upper <-> lower)
print("Straße".casefold())   # 'strasse'       (strong lowercase)

# --- B. Character Checking Methods (Return True or False) ---
s = "Python3"
print(s.startswith("Py"))    # True
print(s.endswith("3"))       # True
print(s.isalpha())           # False (contains '3')
print("Python".isalpha())    # True
print(s.isalnum())           # True  (alphabets + digits)
print("12345".isdigit())     # True
print("12345".isdecimal())   # True
print("12345".isnumeric())   # True
print("   \t".isspace())     # True  (only spaces/tabs/newlines)
print("my_var".isidentifier())# True (valid Python variable name)
print("hello".islower())     # True
print("HELLO".isupper())     # True
print("Title Case".istitle())# True
print("Hello".isprintable()) # True
print("Python".isascii())    # True

# --- C. Searching & Counting Methods ---
sample = "banana banana"
print(sample.count("an"))    # 4  (number of occurrences)
print(sample.find("na"))     # 2  (first index; returns -1 if not found)
print(sample.rfind("na"))    # 11 (last index; returns -1 if not found)
print(sample.index("na"))    # 2  (first index; raises ValueError if not found)
print(sample.rindex("na"))   # 11 (last index; raises ValueError if not found)

# --- D. Stripping / Trimming Methods ---
padded = "   Hello World   "
print(padded.strip())        # 'Hello World' (removes leading & trailing spaces)
print(padded.lstrip())       # 'Hello World   ' (removes left spaces)
print(padded.rstrip())       # '   Hello World' (removes right spaces)
print("***Hi***".strip("*")) # 'Hi'

filename = "report_2026.pdf"
print(filename.removeprefix("report_")) # '2026.pdf'
print(filename.removesuffix(".pdf"))    # 'report_2026'

# --- E. Splitting & Joining Methods ---
fruits = "apple,banana,mango,orange"
print(fruits.split(","))     # ['apple', 'banana', 'mango', 'orange']
print(fruits.split(",", 2))  # ['apple', 'banana', 'mango,orange']
print(fruits.rsplit(",", 1)) # ['apple,banana,mango', 'orange']

lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())    # ['Line 1', 'Line 2', 'Line 3']

words = ["Python", "is", "awesome"]
print(" ".join(words))       # 'Python is awesome'
print("-".join(words))       # 'Python-is-awesome'

email = "user@example.com"
print(email.partition("@"))  # ('user', '@', 'example.com')

# --- F. Replacing & Translation Methods ---
lang = "Java is cool. Java is fast."
print(lang.replace("Java", "Python"))    # 'Python is cool. Python is fast.'
print(lang.replace("Java", "Python", 1)) # replaces only the 1st occurrence

# Translation table (character mapping)
table = str.maketrans("aeiou", "12345")
print("hello".translate(table))          # 'h2ll4'

# --- G. Alignment & Padding Methods ---
title = "Python"
print(title.center(20, "-")) # '-------Python-------'
print(title.ljust(15, "."))  # 'Python.........'
print(title.rjust(15, "."))  # '.........Python'
print("42".zfill(5))         # '00042'
print("-42".zfill(5))        # '-0042'
print("A\tB\tC".expandtabs(4)) # tab expansion

# --- H. Encoding & Decoding ---
text_val = "Hello"
encoded = text_val.encode("utf-8")
print(encoded)               # b'Hello' (bytes)
print(encoded.decode("utf-8"))# 'Hello' (back to string)
