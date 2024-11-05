

# Original string
text = "Hello, welcome to CS50. CS50 is great!"

# Split the string by spaces
split_text = text.split()

# Replace 'CS50' with 'CS50x' in the list
replaced_text = [word.replace('CS50', 'CS50x') for word in split_text]

# Join the list back into a string
result = ' '.join(replaced_text)

print(result)

