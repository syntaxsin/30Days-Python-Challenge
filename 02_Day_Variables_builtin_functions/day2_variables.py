#Day 2: 30 Days of Python Programming

#first name
first_name = input("enter first name: ")
#last name
last_name = input("enter last name: ")
#full name
full_name = print("full name: ", first_name, " ", last_name)
#country
country = input("enter country: ")
#city
city = input("enter city: ")
#age
age = int(input("enter age: "))
#year
year = int(input("enter year: "))

# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it
# Declare a variable is_light_on and assign a value to it
#declare multiple variable on one line
is_married, is_true, is_light_on = False, False, False

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Using the len() built-in function, find the length of your first name
print("first name: ", first_name)
print("first name's length: ", len(first_name))

#Compare the length of your first name and your last name
print("last name: ", last_name)
print("last name's length: ", len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print("\ntotal: ", int(total))

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
print("difference: ", int(diff))

#Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print("product: ", int(product))

#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print("division: ", int(division))

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print("remainder: ", remainder)

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_two ** num_one
print("exponent: ", exp)

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("floor division: ", floor_division)

#Calculate the area of a circle and assign the value to a variable name of area_of_circle
#Take radius as user input and calculate the area.
radius = int(input("\nEnter circle's radius: "))
area_of_circle = 3.14 * (radius ** 2)
print("the area of the circle is ", area_of_circle)

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * radius
print("and the circumference is ", circum_of_circle)