#Day 3: 30 Days of Python Programming
#Operators

# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
# age: int = 24
# height: float = 1.67
# complex_num: complex = 3 + 4j

# Write a script that prompts the user to enter base and height 
# of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# base = int(input("Enter base: "))
# height = int(input("Enter height: "))
# area_of_triangle = 0.5 * base * height
# print("The area of the triangle is ", area_of_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).
# a = int(input("\nEnter side A: "))
# b = int(input("Enter side B: "))
# c = int(input("Enter side C: "))
# perimeter = a + b + c
# print("The perimeter of the triangle is ", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area 
# (area = length x width) and perimeter (perimeter = 2 x (length + width))
# length = int(input("\nLength: "))
# width = int(input("Width: "))

# #Area and Perimeter of rectangle
# area = length * width
# perimeter = 2 * (length + width)

# print("\nArea: ", area, "\nPerimeter", perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) 
# and circumference (c = 2 x pi x r) where pi = 3.14.
# pi = 3.14
# radius = int(input("Enter radius: "))
# area_of_circle = pi * radius * radius
# circum_of_circle = 2 * pi * radius
# print("\nArea of circle: ", area_of_circle, "\nCircumference of circle: ", circum_of_circle)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# x1 , y1 = 2, 2
# x2, y2 = 6, 10

# slope = (y2 - y1)/(x2 - x1)
# print("Slope: ", slope)

# distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# print("Squared Euclidean distance: ", distance)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values 
# and figure out at what x value y is going to be 0.
# for x in range(-6, 1):
#     y = 1 ** 2 + 6 * x + 9
#     print(f"x = {x}, y = {y}")

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in ('python' and 'dragon'))

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print(not('on' in ('python' and 'dragon')))

#Find the length of the text python and convert the value to float and convert it to string
text_len = float(len('python'))
print(type(text_len))
print("Text length converted into float: ", text_len)

string_txt = '{text_len}'
print(type(string_txt))
print("Text length converted from float into string: ", text_len)

#Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
# num = int(input("Enter a number: "))
# print("Remainder: ", num % 2)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print((7 // 3) == 2.7)

# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10
print(type('10') == type(10))
# print(int('9.8') == int(10)) invalid type int('9.8')

# Writ a script that prompts the user to enter hours 
# and rate per hour. Calculate pay of the person?
# hours = int(input("Enter hours of work: "))
# rate = float(input("Enter rate/hour: "))
# pay = hours * rate

# print("Your weekly earning is ", pay)

# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter no. of years you have lived: "))
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"You have lived for {int(seconds)} seconds.")

#Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print(f"{1} {1**0} {1**1} {1**2} {1**3} {1**4}")
print(f"{2} {2**0} {2**1} {2**2} {2**3} {2**4}")
print(f"{3} {3**0} {3**1} {3**2} {3**3} {3**4}")
print(f"{4} {4**0} {4**1} {4**2} {4**3} {4**4}")
print(f"{5} {5**0} {5**1} {5**2} {5**3} {5**4}")