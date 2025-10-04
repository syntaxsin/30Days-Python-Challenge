#Day 4: 30 Days of Python Programming

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(str))

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str = ['Coding', 'For', 'All']
print(' '.join(str))

# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
company = 'Coding For All'
print(len(company))

# Change all the characters to uppercase letters using upper() method
# Change all the characters to lowercase letters using lower() method.
print(company.upper())
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
f_str = 'coding for all'
print(f_str.capitalize())
print(f_str.title())
print(f_str.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(f_str[0:6])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.rfind('Coding'))

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#Split the string 'Coding For All' using space as the separator (split()).
print(company.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
socials =  'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(socials.split(', '))

# What is the character at index 0 in the string Coding For All.
print("The character at index 0 is", company[0])

#What is the last index of the string Coding For All.
last_index = company[-1]
print("The last index of the string \"Code For All\" is", last_index)

#What character is at index 10 in "Coding For All" string.
print(f"The character at index 10 is \"{company[10]}\"")

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
sample_str = 'Python For Everyone'
abbr = sample_str.split()
# print(abbr)
a, b, c = abbr
print(f"The abbreviation is {a[0]}{b[0]}{c[0]}")

#Create an acronym or an abbreviation for the name 'Coding For All'.
sample_str2 = 'Coding For All'
abbr2 = sample_str2.split()
# print(abbr2)
a, b, c = abbr2
print(f"The abbreviation is {a[0]}{b[0]}{c[0]}")

#Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
print("The position of the first occurence is index", sample_str2.index('C'))
print("The position of the last occurence is index", sample_str2.rindex('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
find_str = 'Coding For All People'
print("The position of the first occurence is index", sample_str2.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
conj = 'You cannot end a sentence with because because because is a conjunction'
print(f"The position of the first occurrence of \"because\" is at index ", conj.index('because'))

#find the position of the last occurrence of the word because
print(f"The position of the last occurrence of \"because\" is at index ", conj.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
conj_split = conj.split()
print(f"\'{conj_split[6]} {conj_split[7]} {conj_split[8]}\' is already sliced out.")

#Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(f"The first occurence of the word \'because\' is at index [{conj.find('because')}]")

# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
sub1 ='\'Coding For All'
sub2 = 'Coding For All'
print(f"The first string starting with a substring \'Coding\' is {sub1.startswith('Coding')}")
print(f"The secind string ending with a substring \'Coding\' is {sub2.endswith('coding')}")

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
sub3 = '   Coding For All      '
strip_str = sub3.strip(' ')
print(f"{strip_str}")

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
idf = '30DaysOfPython'
idf2 = 'thirty_days_of_python'
print(f"The variable name \'{idf}\' is {idf.isidentifier()}")
print(f"The variable name \'{idf2}\' is {idf2.isidentifier()}")

#The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
tech = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(tech))

#Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

#Use a tab escape sequence to write the following lines.
tab_str = 'Name\tAge\tCountry\t\tCity'
tab_str2 = 'Jerome\t24\tPhilippines\tQuezon City'
print(tab_str)
print(tab_str2)

#Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
radius = 10
pi = 3.14
area = pi * radius ** 2

print('radius = {}'.format(radius))
print('area = {} * {} ** 2'.format(pi, radius))
print('The area of a circle with radius {} is {} meters square'.format(radius, int(area)))

#Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

op1 = 8 + 6
op2 = 8 - 6
op3 = 8 * 6
op4 = 8 / 6
op5 = 8 % 6
op6 = 8 // 6
op7 = 8 ** 6

print('8 + 6 = {}'. format(op1))
print('8 - 6 = {}'. format(op2))
print('8 * 6 = {}'. format(op3))
print('8 / 6 = {:.2f}'. format(op4))
print('8 % 6 = {}'. format(op5))
print('8 // 6 = {}'. format(op6))
print('8 ** 6 = {}'. format(op7))