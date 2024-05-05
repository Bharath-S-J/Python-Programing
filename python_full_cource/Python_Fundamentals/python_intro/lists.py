# List of names
names = ['john', 'bob', 'mosh', 'sarah', 'mona']

# Slicing and printing elements from index 2 to 3 (4 is exclusive)
print(names[2:4])

# Slicing and printing elements from index 2 to end of the list
print(names[2:])

# Accessing and printing the second last element in the list
print(names[-2])

# Printing the entire list of names
print(names)

# Modifying the first element of the list
names[0] = 'bharath'
print(names)

# List of numbers
numbers = [3, 4, 100, 6, 8, 31]

# Finding the maximum number in the list using a loop
max_number = numbers[0]  # Assume the first element is the maximum
for item in numbers:
    if max_number < item:
        max_number = item  # Update max_number if a larger number is found

# Printing the maximum number found in the list
print(f"max number in list is: {max_number}")
