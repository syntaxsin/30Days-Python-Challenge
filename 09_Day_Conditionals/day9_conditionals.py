#Day 9

#Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

age = int(input('Enter your age: '))

if age < 18:
    print(f'You need {18 - age} more years to learn to drive.')
else:
    print('You are old enough to drive.')

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

my_age = 24
your_age = int(input('Enter your age: '))

if your_age % my_age == 1:
    print(f'You are 1 year older than me.')
elif my_age % your_age == 1:
    print(f'You are 1 year younger than me.')
elif your_age > my_age:
    print(f'You are {your_age - my_age} years are older than me.')
elif your_age < my_age:
    print(f'You are {my_age - your_age} years are younger than me.')
else:
    print("Ayo! We're the same age!")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b.

inputA = int(input('Enter first number: '))
inputB = int(input('Enter second number: '))

if inputA > inputB:
    print(f'{inputA} is greater than {inputB}')
if inputA < inputB:
    print(f'{inputA} is smaller than {inputB}')
else:
    print(f'{inputA} is equal to {inputB}')