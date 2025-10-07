#Day 7

#------------------------------ start of testing phase ----------------------------#

#------------------------------ end of testing phase ------------------------------#

#EXERCISE LEVEL 1
# Find the length of the set it_companies
# Add 'Twitter' to it_companies
# Insert multiple IT companies at once to the set it_companies
# Remove one of the companies from the set it_companies
# What is the difference between remove and discard

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(f'Number of IT Companies inside the set is {len(it_companies)}')

it_companies.add('Twitter')
print(it_companies)

multi_companies = ('Accenture', 'RELX', 'Convey')
it_companies.update(multi_companies)
print(it_companies)

it_companies.remove('Accenture')
print(f'Updated IT Companies in the set: {it_companies}')

#The difference of remove() and discard()
#remove() : when an item is not found in the using this method, it will prompt an error.
#discard(): no error prompts even when the item is not found.
it_companies.discard('Accenture')

#---------------------------------------------------------------------------------#

#EXERCISE LEVEL 2
# Join A and B
# Find A intersection B
# Is A subset of B
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely

setA = {19, 22, 24, 20, 25, 26}
setB = {19, 22, 20, 25, 26, 24, 28, 27}

setA.update(setB)
print(f'Joined sets: {setA}')

setA = {19, 22, 24, 20, 25, 26}
setB = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'The intersection of A and B is {setB.intersection(setA)}')

print(f'Is A subset of B: {setA.issubset(setB)}')

print(f'Are A and B disjoint sets: {setA.isdisjoint(setB)}')

setA.union(setB)
print(f'Join A with B: {setA}')
setB.union(setA)
print(f'Join B with A: {setB}')

print(f'The symmetrical difference between A and B is {setA.symmetric_difference(setB)}')

#EXERCISE LEVEL 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f'Length of ages (List): {len(age)}')
age = set(age)
print(f'Length of ages (Set): {len(age)}')

#String: combination of characters
#List: ordered and mutable collection of items (can store duplicated items)
#Tuple: tuple an immutable and ordered collection (can store duplicated items)
#Set: unordered and mutable type of list (no duplicated items) 

unique_words = 'I am a teacher and I love to inspire and teach people'
unique_words.split()
unique_set = set(unique_words)
print(f'Unique words using split and set: {unique_set}')