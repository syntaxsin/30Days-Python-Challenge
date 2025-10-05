#Day 5

#------------------------------ testing phase ------------------------------#

# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# print(f'Fruits: {fruits}')
# print(f'Number of fruits: {len(fruits)}')
# print(f'Vegetables: {vegetables}')
# print(f'Number of vegetables: {len(vegetables)}')
# print(f'Animal Products: {animal_products}')
# print(f'Number of animal products: {len(animal_products)}')
# print(f'Web Techs: {web_techs}')
# print(f'Number of web techs: {len(web_techs)}')
# print(f'Countries: {countries}')
# print(f'Number of countries: {len(countries)}')

#reversed list
# reverse = fruits[::-1]
# print("Reversed list:", reverse)

#copying and joining a list
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
# copy = countries.copy() + web_techs.copy()
# print('\n{}\n{}\n{}'.format(countries, web_techs, copy))

#using a extend() method
# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']

# fruits.extend(vegetables + animal_products)
# print(f'Extended list of fruits: {fruits}')

#using extend() and copy() at once
# fruits.extend(vegetables.copy() + animal_products.copy())
# print(f'Extended list of fruits: {fruits}')

# reversing a list using reverse() methond
# fruits.reverse()
# print(fruits)

#using a sort() or sorted() method
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

#sorted() method returns a sorted list without modifying the original list
# print(web_techs)
# web_techs = sorted(web_techs)
# print(web_techs)
# web_techs_r = sorted(web_techs, reverse=True)
# print(web_techs_r)

#------------------------------ end of testing phase ------------------------------#

#Exercise Level 1

# Declare an empty list
# Declare a list with more than 5 items
empty_list = [
    'React',
    'Angular',
    'Node.js',
    'JavaScript',
    'Tailwind'
]

#Find the length of your list
print(f'The length of the list is {len(empty_list)}')

#Get the first item, the middle item and the last item of the list
print('{} {} {}'.format(empty_list[0], empty_list[3], empty_list[-1]))

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = [{
    'name': 'Jerome',
    'age': 24,
    'height': 167,
    'marital_status': 'single',
    'address': 'Quezon City, Metro Manila, Philippines'
}]

print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = [
    'Facebook',
    'Google',
    'Microsoft',
    'Apple',
    'IBM',
    'Oracle',
    'Amazon'
]

#Print the list using print()
print(it_companies)
#Print the number of companies in the list
print(f'The number of companies in the list is {len(it_companies)}')

#Print the first, middle and last company
print('{} {} {}'.format(it_companies[0], it_companies[3], it_companies[-1]))

#Print the list after modifying one of the companies
it_companies[0] = 'Instagram'
print(f'Modified list: {it_companies}')

#Add an IT company to it_companies
it_companies.append('RELX')
print(f'Modified list: {it_companies}')

#Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Accenture')
print(f'Modified list: {it_companies}')

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[-2] = 'AMAZON'
print(f'Modified list: {it_companies}')

# Join the it_companies with a string '#;  '
joined_companies = '#; '.join(it_companies)
print(f'Joined companies: {joined_companies}')

#Check if a certain company exists in the it_companies list.
checker = 'Facebook' in it_companies
print('Facebook being on the list of IT companies is {}'.format(checker))

#Sort the list using sort() method
it_companies.sort()
print(f'Sorted list of companies:\n{it_companies}')
#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(f'Sorted list of companies (Reversed):\n{it_companies}')

#Slice out the first 3 companies from the list
sliced_index = it_companies[:3]
print(f'Sliced out first indexes: {sliced_index}')
#Slice out the last 3 companies from the list
sliced_last_index = it_companies[-3:]
print(f'Sliced out last indexes: {sliced_last_index}')
# Slice out the middle IT company or companies from the list
middle_index = it_companies[3:-3]
print(f'Sliced out middle indexes: {middle_index}')

#Remove the first IT company from the list
del it_companies[0]
print(f'Updated IT companies (Removed 1st Company): {it_companies}')
# Remove the middle IT company or companies from the list
del it_companies[3:-3]
print(f'Updated IT companies (Removed Middle Company/Companies): {it_companies}')
#Remove the last IT company from the list
del it_companies[-1]
print(f'Updated IT companies (Removed Last Company): {it_companies}')
# Remove all IT companies from the list
it_companies.clear()
print(f'IT Companies: {it_companies}')
#Destroy the IT companies list
# del it_companies
# print(f'List: {it_companies}') #returned error as the list is already been destroyed

#EXERCISE LEVEL 1
#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#After joining the lists in question 26. Copy the joined list and 
#assign it to a variable full_stack, then insert Python and SQL after Redux.
joined_stacks = list()
joined_stacks.extend(front_end + back_end)
print(f'Joined stacks: {joined_stacks}')

full_stack = list()
full_stack.extend(joined_stacks.copy())
print(f'Full stack: {full_stack}')

full_stack.insert(5,'Python')
print(f'Updated full stack: {full_stack}')

#EXERCISE LEVEL 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
ages.sort()
print(ages)
min_pop, max_pop = ages.pop(0), ages.pop(-1)
print(f'Min: {min_pop}\t\tMax: {max_pop}')
print(ages)

ages.append(min_pop)
ages.append(max_pop)
ages.sort()
print(ages)

median = (ages[4] + ages[-4]) / 2
print(f'The median age is {int(median)}')

avr_age = (sum(ages) / len(ages))
print(f'The average age is {avr_age}')

min_age = min(ages)
max_age = max(ages)
# print(f'The range of ages are from {min_age} to {max_age}')
print(f'The range of ages is {max_age - min_age}')

print(f'{abs(min_age - avr_age)}\n{abs(max_age - avr_age)}')

#Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
cn, rs, us, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(f'First 3 (three) countries: {cn}, {rs}, and {us}')
print(f'Scandic countries: {scandic}')