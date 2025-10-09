#Day 8

#EXERCISE DAY 8
# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# Get the length of the student dictionary
# Get the value of skills and check the data type, it should be a list
# Modify the skills values by adding one or two skills
# Get the dictionary keys as a list
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using items() method
# Delete one of the items in the dictionary
# Delete one of the dictionaries

dog = {
    'name': 'Choco', 
    'color': 'Brown', 
    'breed': 'Shih Tzu', 
    'legs': '4', 
    'age': '4'
}

student = {
    'first_name': 'Jourjet', 
    'last_name': 'Clemen', 
    'gender': 'Femail', 
    'age': '24', 
    'marital_status': 'Married',
    'skills': ['Leadership', 'Problem-solving'], 
    'country': 'Philippines', 
    'city': 'Quezon City', 
    'address': 'Blk 16 Lot 43 Planters Street, Sugartowne Homes, Batasan Hills'
}

print(f'Length of the student dictionary: {len(student)}')
print(student['skills'], type(student['skills']))

student['skills'].append('Teamwork')
student['skills'].append('Active Listening')
print(student['skills'])

print(student.keys())
print(student.values())

print(student.items())

del student['skills']
print(student)

# del dog
# print(dog)