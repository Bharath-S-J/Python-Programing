#Iterating Over Lists and Ranges with for Loop
print('Iterating Over Lists and Ranges with for Loop')
# Iterating over a list of numbers
for item in [1, 2, 3, 4]:
    print(item)
print("break")

# Iterating over a list of characters
for item in ['A', 'B', 'C']:
    print(item)
print("break")

# Iterating over a range of numbers (default start at 0)
for item in range(10):
    print(item)
print("break")

# Iterating over a range of numbers (specified start and end)
for item in range(5, 10):
    print(item)
print("break")

# Iterating over a range of numbers with a step (start, end, step)
for item in range(5, 10, 2):
    print(item)
print("break")


#Calculating Total Prices with for Loop
print("Calculating Total Prices with for Loop")
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print(f"Total: {total}")



#Nested Loops for Pattern Printing
print('Nested Loops for Pattern Printing')
# Nested loops to print coordinates
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# Nested loop for pattern printing using list of numbers
numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)

#or 
numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print("*" * item)