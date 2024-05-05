i = 1
while i <= 5:
    print('*' * i)  # Print '*' repeated 'i' times on each iteration
    i = i + 1       # Increment 'i' by 1 for the next iteration

print('done')       # Print 'done' after the loop completes


print('Number Guessing Game with while Loop')   
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the secret number: "))  # Prompt user to guess the number
    guess_count += 1                                 # Increment guess count after each attempt

    if guess == secret_number:  # Check if the guessed number matches the secret number
        print("You won!")      # Print 'You won!' if the guess is correct
        break                   # Exit the loop (game) if the guess is correct
else:
    print('You failed to guess the number.')  # Print 'You failed...' if guesses are exhausted



print('Simple Car Control Simulation with while Loop')
#Simple Car Control Simulation with while Loop
command = ""
status = ""

while True:
    command = input("> ").lower()  # Prompt user for a command and convert to lowercase

    if command == 'start':
        if status == command:
            print("Car is already started.")
        else:
            print('Car started.')
            status = command
    elif command == 'stop':
        if status == command:
            print("Car is already stopped.")
        else:
            print('Car stopped.')
            status = command
    elif command == 'help':
        print("""
              start -> to start the car
              stop -> to stop the car
              quit -> to quit
              """)
    elif command == 'quit':
        break  # Exit the loop if the user enters 'quit'
    else:
        print('I don\'t understand.')  # Print an error message for unrecognized commands
