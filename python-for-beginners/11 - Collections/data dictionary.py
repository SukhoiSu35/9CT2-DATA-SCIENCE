# Student Dictionary Activities
student = {'name': 'Harry', 'age': 14, 'suburb': 'Sydney'}
print(student['name'])  # Output: Harry
print(student['age'])   # Output: 14
student['suburb'] = 'Gosford'
student['email'] = 'harry.juneja@education.nsw.gov.au'
del student['age']

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)

if 'email' in student:
    print("Email key exists.")
else:
    print("Email key does not exist.")

# Nested Dictionaries and Additional Tasks
student = {
    'name': 'Harry',
    'age': 14,
    'suburb': 'Sydney',
    'email': 'harry.juneja@education.nsw.gov.au',
    'education': {
        'major': 'Maths',
        'School': 'Gosford High School'
    },
    'hobbies': ['Tennis', 'swimming', 'soccer']
}

School = student['education']['School']
print(School)  # Output: Gosford High School

School = student.get('education').get('School')
print(School)  # Output: Gosford High School

student['hobbies'].append('Tennis')
student['age'] = 14
student['education']['major'] = 'Maths'

# Challenge 1: Create a Dictionary
name = input("Enter the student's name: ")
age = input("Enter the student's age: ")
favorite_subject = input("Enter the student's favorite subject: ")

student_info = {
    'name': name,
    'age': age,
    'favorite_subject': favorite_subject
}

print("Student Information:")
print(f"Name: {student_info['name']}")
print(f"Age: {student_info['age']}")
print(f"Favorite Subject: {student_info['favorite_subject']}")
