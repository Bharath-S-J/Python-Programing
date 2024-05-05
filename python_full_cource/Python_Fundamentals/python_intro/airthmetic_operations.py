# Arithmetic Operations in Python

# Addition
print(10 + 10)  # Output: 20

# Integer Division (floor division)
print(10 // 3)  # Output: 3 (result is the quotient without the remainder)

# Floating-point Division
print(10 / 3)   # Output: 3.3333333333333335 (result is a float)

# Modulus (remainder of the division)
print(10 % 3)   # Output: 1 (remainder when 10 is divided by 3)

# Exponentiation (power)
print(10 ** 3)  # Output: 1000 (10 raised to the power of 3)

# Operator Precedence and Associativity
# Parentheses > Exponentiation > Multiplication/Division > Addition/Subtraction

x = 10
x = x + 3       # Addition: x = 10 + 3 -> x = 13
x += 3          # Shortened Addition: x = x + 3 -> x = 13 + 3 -> x = 16
print(x)        # Output: 16

x = 10 + 3 * 2   # Multiplication before Addition: x = 10 + (3 * 2) -> x = 10 + 6 -> x = 16
print(x)         # Output: 16

x = 10 + 3 * 2 ** 2   # Exponentiation before Multiplication: x = 10 + (3 * (2 ** 2)) -> x = 10 + (3 * 4) -> x = 10 + 12 -> x = 22
print(x)              # Output: 22

x = (10 + 3) * 2 ** 2  # Parentheses before Exponentiation and Multiplication: x = (13) * (2 ** 2) -> x = 13 * 4 -> x = 52
print(x)               # Output: 52

x = (2 + 3) * 10 - 3    # Parentheses evaluated first: x = (5) * 10 - 3 -> x = 50 - 3 -> x = 47
print(x)                # Output: 47
