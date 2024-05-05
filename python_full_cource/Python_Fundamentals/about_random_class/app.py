import random  # Import the random module to generate random numbers

# Loop to print random numbers and a random integer within a range
for i in range(3):
    print(random.random())  # Print a random float between 0.0 and 1.0
    print('break')  # Print a separator for clarity
    print(random.randint(10, 50))  # Print a random integer between 10 and 50

members = ['a', 'b', 'c', 'd', 'e']  # List of members
leader = random.choice(members)  # Select a random member from the list
print(leader)  # Print the randomly chosen leader from the list

class Dice:
    def roll(self):
        # Method to simulate rolling a dice (two six-sided dice)
        first = random.randint(1, 6)  # Roll the first dice (random number between 1 and 6)
        second = random.randint(1, 6)  # Roll the second dice (random number between 1 and 6)
        return first, second  # Return a tuple representing the result of rolling two dice

# Create an instance of the Dice class
dice = Dice()

# Roll the dice and print the result (a tuple representing the outcome of two dice rolls)
print(dice.roll())
