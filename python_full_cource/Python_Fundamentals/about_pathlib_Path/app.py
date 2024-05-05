from pathlib import Path  # Import the Path class from the pathlib module

# Create a Path object representing the 'ecommerce' directory
path = Path('ecommerce')

# Check if the 'ecommerce' directory exists
print(path.exists())  # Output: True or False depending on whether the directory exists

# Create a Path object representing the 'email' directory
path = Path('email')

# Create the 'email' directory (if it doesn't exist)
path.mkdir()

# Remove the 'email' directory (if it exists)
path.rmdir()

# Create a Path object representing the current directory ('.')
path = Path()

# Iterate over all '.py' files in the current directory
for file in path.glob('*.py'):
    print(file)  # Output: Path objects representing each '.py' file found in the directory
