try:
    # Attempt to get user input for 'age' and convert it to an integer
    age = int(input("Age: "))
    
    # Assume income value
    income = 2000
    
    # Calculate 'risk' by dividing income by age
    risk = income / age
    
    # Print the age if successful
    print(age)

except ValueError:
    # Handle the ValueError if the input cannot be converted to an integer
    print("Invalid value. Please enter a valid integer for age.")

except ZeroDivisionError:
    # Handle the ZeroDivisionError if 'age' is zero (cannot divide by zero)
    print("Age cannot be zero. Please enter a non-zero value for age.")
