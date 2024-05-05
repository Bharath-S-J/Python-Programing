# Strings in Python

# Using single quotes with apostrophe inside
course = "Python's course for Beginners"
print(course)  # Output: Python's course for Beginners

# Using single quotes with double quotes inside
course = 'Python course for "Beginners"'
print(course)  # Output: Python course for "Beginners"

# Using triple quotes for multi-line string
course = '''Hi Bharath,
Here is our first email to you.
Thank you,
Support Team
'''
print(course)  # Output: Multi-line string with line breaks

# Slicing strings
course = "Python course for Beginners"

print(course[1:])  # Output: ython course for Beginners (from index 1 to end)
print(course[:5])  # Output: Python (from start to index 4)

# Copying strings using slice
another = course[:]  # Create a copy of the entire string
print(another)  # Output: Python course for Beginners

# Slicing with negative indices
name = 'Bharath'
print(name[1:-1])  # Output: harat (from index 1 to second last character)

# Formatted strings
first = 'Bharath'
last = 'S J'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)  # Output: Bharath [S J] is a coder
print(msg)      # Output: Bharath [S J] is a coder

# String methods
course = 'Python for Beginners'

print(len(course))                          # Output: 20 (length of the string)
print(course.upper())                       # Output: PYTHON FOR BEGINNERS
print(course.lower())                       # Output: python for beginners
print(course.find('o'))                     # Output: 4 (index of the first 'o')
print(course.replace('Beginners', 'Absolute Beginners'))  # Output: Python for Absolute Beginners
print('Python' in course)                   # Output: True (check if 'Python' is present in the string)
