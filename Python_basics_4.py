# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:08:13 2024

@author: mcing
Python's dictionaries allow us to connect pieces of related information.
The idea is to be able to access information from a dictionary.
We can store more information about a peson.
For example a persons: age, location,profession
"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


alien_0 = {'color': 'green', 'points': 5}
new_points =alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Now we can add new Key-Value Pairs.
#So we would need the name of the dictionary, followed by the new key
#In this case the name of the dictionary id alien_0

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

"""
Starting with an empty dictionary.
We need to then add new items into the empty dictionary
"""
alien_1 ={}
alien_1['color'] = "blue"
alien_1['points'] = 5

print(alien_1)
print("The alien is" + " "+alien_1['color']+".")

aliens =[]

#Make 30 green aliens.
for i in range(30):
    new_alien={'color':'green', 'points':5,'speed':'slow'}
    aliens.append(new_alien)

print(aliens)

#Showing the first 5 aliens:
for i in aliens[:5]:
    print(aliens)
print("...")

#Show how mant aleins have been created.
print("Total number of aliens:" + str(len(aliens)))

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (0,30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)
 
for alien in aliens[0:3]:
 if alien['color'] == 'green':
     alien['color'] = 'yellow'
     alien['speed'] = 'medium'
     alien['points'] = 10
 
# Show the first 5 aliens:
for alien in aliens[0:5]:
 print(alien)
print("...")

#A List in a Dictionary

pizza ={'crust': 'thick', 'toppings':['mushroom','extra cheese']}
#Summarise the order
print("You ordered a "+pizza['crust']+"-crust pizza"+ " "+ "with the following toppings:")
for i in pizza['toppings']:
    print("\t" + i)


#So to access the elements,
#of a dictionary this is the way I would go about to do it.
"""
variable[element]
"""
#having two dictionaries
users ={'ainstein':{
    'first': 'albert',
    'last': 'einstein',
    'location':'princeton'},
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location':'paris'},
    }


'''
the .tems() is used to return each item in a dictionary as tuples in a list.
At (1) we loop through the users dictionary. Python stores each key in the 
variable username, and the dictionary associated with each username goes 
into the variable user_info. Once inside the main dictionary loop, we print 
the username at (2)

At (3) we start accessing the inner dictionary. The variable user_info, 
which contains the dictionary of user information, has three keys: 'first', 
'last', and 'location'. We use each key to generate a neatly formatted full 
name and location for each person, and then print a summary of what we 
know about each user (4)
'''

for username, user_info in users.items(): # loop through the users dictionary. Stores the key into the varaible username.
 print("\nUsername: " + username)
 full_name = user_info['first'] + " " + user_info['last']
 location = user_info['location']
 print("\tFull name: " + full_name.title())
 print("\tLocation: " + location.title())


#

favorite_languages= {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskel']}

#Basically all the contents of the dictionary are assigned
# into the variables name and language.
#This code below works because there is a list attribute below in the values.
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
        
        
#The code below would work only if we do not have a list  attribute on our dictionary.
favorite_languages2 = { 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name,languages in favorite_languages2.items():
    print(name.title() + "'s favorite languages are:" + " "+ languages.title()+ ".")
#But if we want to get the values of the dictionary
# then the lop would be:
for language in set(favorite_languages.values()):
    print(language.title())    
#Exercise
#6-1.
friends={'first_name': 'jason',"last_name": 'moocle',
         'age':23,'city':'port elizabeth'}

print(friends)

#6-2
friends_2 = {'john': 7,
             'james':8,
             'mark': 10,
             'andrew':12,
             'peter':7}

for name,number in friends_2.items():
    print("\n"+ "My name is"+ " "+name.title()+ " ","this is my favorite number:" + "\t" +str(number))

friends_3={'john': [7,10],
             'james':[8],
             'mark': [10,12],
             'andrew':[12],
             'peter':[7]
    }
for name,numbers in friends_3.items():
    print("\n"+"My name is"+ " "+name.title()+ " this is my favourtie number:")
    for number in numbers:
        print("\t"+ str(number))
        
#If some of the values are not lists then this is how this would look like:
friends_4 = {'john': [7, 10],
             'james': 8,
             'mark': [10, 12],
             'andrew': 12,
             'peter': 7}

for name, numbers in friends_4.items():
    print("\nMy name is " + name.title() + " and this is my favourite number:")
    if not isinstance(numbers, list):
        numbers = [numbers]
    for number in numbers:
        print("\t" + str(number))
        
#6-3
#.items() returns a list of key-value pairs and puts them in the assigned variables.

favorite_languages3= {
    'john': ['python','ruby'],
    'sarah': ['c'],
    'james': ['ruby','go'],
    'phil': ['python','haskel']}

take_poll= ['ruth','ester','mary','john','james']
for i in take_poll:
    if i not in favorite_languages3.keys():
        print("\n"+ i.title()+ " "+"please choose your favortite language.")
    else:
        if (i in favorite_languages3.keys()):
            print("\n"+ i.title()+" "+",thank you for responding!")

#lets say I want to delete something if it it is already on the list how would I do that.
favorite_languages4= {
    'john': ['python','ruby'],
    'sarah': ['c'],
    'james': ['ruby','go'],
    'phil': ['python','haskel']}

take_poll2= ['ruth','ester','mary','john','james']
for i in take_poll2:
    if (i not in favorite_languages4.keys()):
        print("\n"+ i.title()+ " "+"please choose your favortite language.")
    else:
        if (i in favorite_languages4.keys()):
            del i   
print("Ananlysis complete")

# Dictionary within a dictionary.
#Nested dictionaries.











