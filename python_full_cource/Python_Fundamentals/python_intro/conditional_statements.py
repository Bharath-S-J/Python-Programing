# Conditional Statements in Python

# Example 1: Simple if-elif-else statement
is_hot = False
is_cold = False

if is_hot:
    print('It\'s a hot day')
elif is_cold:
    print('It\'s a cold day')
else:
    print('It\'s a lovely day')

print('Enjoy your day')  # This line is outside the if-elif-else block and always executes

# Example 2: Using conditional expression to calculate down payment
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price  # 10% down payment for good credit
else:
    down_payment = 0.2 * price  # 20% down payment for bad credit

print(f"Down Payment: ${down_payment}")
