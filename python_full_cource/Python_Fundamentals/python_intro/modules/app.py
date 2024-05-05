# Importing the entire 'converters' module
import converters

# Importing the 'kg_to_lbs' function directly from the 'converters' module
from converters import kg_to_lbs

# Using the 'kg_to_lbs' function from the imported 'converters' module to convert 50 kilograms to pounds
print(converters.kg_to_lbs(50))

# Using the 'kg_to_lbs' function directly (imported) to convert 72 kilograms to pounds
print(kg_to_lbs(72))

# Importing the 'find_max' function from a specific submodule
from Python_Fundamentals.python_intro.modules.converters import find_max

# Creating a list of numbers
numbers = [10, 2, 45, 5, 2]

# Using the 'find_max' function from the imported submodule to find the maximum value in the list 'numbers'
print(find_max(numbers))
