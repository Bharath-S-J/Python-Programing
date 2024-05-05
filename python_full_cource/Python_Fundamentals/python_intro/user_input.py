# Getting user input for name and favorite color
name = input('What is your name? ')        # Prompt user for their name
fav_color = input('What is your color? ')   # Prompt user for their favorite color
print(name + ' likes ' + fav_color)         # Display a message indicating the user's name and favorite color

# Calculating age based on birth year
birth_year = int(input('Birth year: '))    # Prompt user for their birth year and convert input to an integer
age = 2023 - birth_year                     # Calculate age by subtracting birth year from current year
print('Your age is:', age)                  # Display the calculated age
print('Age data type:', type(age))          # Display the data type of the 'age' variable

# Converting weight from pounds to kilograms
weight_lbs = input('Weight (lbs): ')        # Prompt user for weight in pounds
weight_kg = int(weight_lbs) * 0.45           # Convert weight from pounds to kilograms (assuming 1 lb = 0.45 kg)
print('Weight in kilograms:', weight_kg)    # Display the weight in kilograms
