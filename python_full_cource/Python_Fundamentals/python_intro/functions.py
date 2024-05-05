# Example of a basic function without parameters
def greet_user():
    print("hi There!")
    print("welcome")

print('start')
greet_user()  # Call the function 'greet_user'
print("finish")


# Example of a function with a parameter (name)
def greet_user(name):
    print(f"hi {name}")
    print("welcome")

print('start')
greet_user("bharath")  # Call the function 'greet_user' with 'name' parameter
greet_user("baba")  # Call the function again with a different name
print("finish")


# Example of a function with keyword arguments
def greet_user(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome")

print('start')
greet_user("bharath", last_name="S J")  # Call the function using positional and keyword arguments
print("finish")


# Example of a function with a return statement
def square(number):
    return number * number  # Calculate and return the square of the 'number'

print(square(5))  # Call the function 'square' and print the returned value


# Example of creating a reusable function to convert words to emojis
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output  # Return the converted message with emojis

message = input('>')
print(emoji_converter(message))  # Call the function 'emoji_converter' and print the converted message
