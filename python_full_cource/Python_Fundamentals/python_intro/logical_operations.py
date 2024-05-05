# Logical Operations and Conditional Statements in Python

# Example 1: Using logical operations to check loan eligibility
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')

# Alternatively, using explicit comparison for clarity
if has_good_credit and has_criminal_record != True:
    print('Eligible for loan')

# Example 2: Validating name length
name = 'Bfgh'

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name must be a maximum of 50 characters')
else:
    print('Name looks good')

# Example 3: Weight conversions based on user input
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
