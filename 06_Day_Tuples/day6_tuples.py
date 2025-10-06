#Day 6

#------------------------------ start of testing phase ------------------------------#

# #empty tumple
# exp_tuple = tuple()

# #with initial values
# fruits = ('banana', 'orange', 'mango', 'lemon')
# print(len(fruits)) #using len()

# #accessing tuple items
# first_item = fruits[0]
# second_item = fruits[1]
# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]

# #negative indexing
# first_item = fruits[-4]
# second_item = fruits[-3]
# last_fruit = fruits[-1]

# #range of positive indexes
# all_fruits = fruits[0:4]
# middle_fruits = fruits[1:3]

# #range of negative indexes
# negat_fruits = fruits[-4:]
# negative_middle = fruits[-3:-1]

# #changing tuples to lists
# print(fruits)
# fruits = list(fruits)
# print(fruits)
# fruits = tuple(fruits)
# print(fruits)

# #checking an item in a tuple
# print('orange' in fruits)
# print('apple' in fruits)

# #joining tuples
# vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
# joined_tpl = fruits + vegetables
# print(joined_tpl)

# #deleting tuples
# del fruits
# del vegetables
# print(fruits)
# print(vegetables)
# print(joined_tpl)

#------------------------------ end of testing phase ------------------------------#

#EXERCISE LEVEL 1

# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

brothers = ('Jericho', 'Lemuel', 'Jerome')
sisters = ('Jeremie', 'Jez', 'Louisa')
siblings = brothers + sisters

print(len(siblings))

print(siblings)
siblings = list(siblings)
print(siblings)

siblings.append('Cristina')
siblings.append('Marlon')
siblings = tuple(siblings)

family_members = siblings
print(family_members)

#EXERCISE LEVEL 2
# Unpack siblings and parents from family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely

*siblings, mother, father = family_members
print(siblings)
print(mother)
print(father)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

sliced_food = food_stuff_tp[4:-4]
print(sliced_food)

last_food_indexes = food_stuff_tp[-4:-1]
print(last_food_indexes)

food_stuff_tp = tuple(food_stuff_tp)
print(food_stuff_tp)

del food_stuff_tp
# print(food_stuff_tp) #the food_stuff_tp is not defined because it's already been deleted

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print(f'Estonia a nordic country is {'Estonia' in nordic_countries}')
print(f'Iceland a nordic country is {'Iceland' in nordic_countries}')
