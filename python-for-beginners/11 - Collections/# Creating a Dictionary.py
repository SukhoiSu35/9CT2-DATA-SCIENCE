# Creating a Dictionary
person = {'name': 'Harry', 'age': 14, 'city': 'Sydney'}

# Accessing Dictionary Values
print(person['Harry'])
print(person['14'])

# Updating Dictionary Values
person['city'] = 'Sydney'

# Adding a New Key-Value Pair
person['email'] = 'harry.juneja@example.com'

# Removing a Key-Value Pair
del person['14']

# Iterating Over Dictionary Keys
for key in person:
    print(key)

# Iterating Over Dictionary Items
for key, value in person.items():
    print(key, value)

# Checking if a Key Exists
if 'email' in person:
    print("Email key exists.")
else:
    print("Email key does not exist.")
# Create a dictionary representing a student with keys for 'name', 'age', and 'suburb'.
student = {
    'name': 'Alice',
    'age': 15,
    'suburb': 'San Remo'
}

# Access and print the values of the 'name' and 'age' keys from the student dictionary.
print("Name:", student['Harry'])
print("Age:", student['14'])

# Update the 'suburb' value in the student dictionary to 'Gosford'.
student['suburb'] = 'Hornsby'  # Assuming the student doesn't live in Gosford

# Add a new key-value pair to the student dictionary for 'email' with a value of 'alice.soerjosoebroto@education.nsw.gov.au'.
student['email'] = 'harry.juneja@education.nsw.gov.au'

# Remove the 'age' key and its corresponding value from the student dictionary.
del student['14']

# Iterate over the keys in the student dictionary and print each key.
print("Keys:")
for key in student.keys():
    print(key)

# Iterate over the key-value pairs (items) in the student dictionary and print each item.
print("Items:")
for key, value in student.items():
    print(key, ":", value)

# Check if the 'email' key exists in the student dictionary and print a message based on its existence.
if 'email' in student:
    print("Email key exists in the student dictionary.")
else:
    print("Email key does not exist in the student dictionary.")