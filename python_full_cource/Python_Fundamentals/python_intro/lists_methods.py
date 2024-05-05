# List of numbers
numbers = [5, 2, 1, 71, 1, 4]

# Append the number 20 to the end of the list
numbers.append(20)
print(numbers)

# Insert the number 78236 at index 0
numbers.insert(0, 78236)
print(numbers)

# Remove the first occurrence of the number 5 from the list
numbers.remove(5)
print(numbers)

# Remove the last element from the list
numbers.pop()
print(numbers)

# Find the index of the number 71 in the list
print(numbers.index(71))

# Count the occurrences of the number 1 in the list
print(numbers.count(1))

# Check if the number 7 is in the list
print(7 in numbers)

# Sort the list in ascending order
numbers.sort()
print(numbers)

# Reverse the order of elements in the list
numbers.reverse()
print(numbers)

# Create a copy of the list 'numbers'
numbers2 = numbers.copy()

# Append the number 10 to the original list
numbers.append(10)

# Print both the modified list and the copied list
print(numbers)
print(numbers2)

# Clear all elements from the list 'numbers'
numbers.clear()
print(numbers)

# List of numbers with duplicates
numbers = [2, 2, 4, 6, 3, 4, 6, 1]

# Create a new list 'uniques' containing only unique elements from 'numbers'
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

# Print the list of unique elements
print(uniques)
