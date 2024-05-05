# Define a dictionary named 'customer'
customer = {
    "name": "bharath",
    "age": 22,
    "is_verified": True
}

# Access and print the value associated with the key 'name' in the dictionary
print(customer['name'])

# Access and print the value associated with the key 'dj', with a default value if the key is not found
print(customer.get("dj", "jan 22 2001"))

# Add a new key-value pair 'birthdate' to the dictionary
customer['birthdate'] = 'oct 22 2001'

# Access and print the value associated with the key 'birthdate'
print(customer['birthdate'])


# Example of using dictionary to map digits to words
phone = input("Phone: ")
output = ""
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

# Iterate through each character in the input 'phone' and map digits to words
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

# Print the mapped output
print(output)


# Example of replacing words with emojis using a dictionary
print("emojis replacing")
message = input(">")
words = message.split(' ')

emojis = {
    ":)": "😊",
    ":(": "😒"
}

output = ""
# Iterate through each word in the input 'message' and replace with emojis if found in the dictionary
for word in words:
    output += emojis.get(word, word) + ' '

# Print the output with replaced emojis
print(output)
