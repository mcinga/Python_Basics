# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:15:02 2024

@author: mcing
If statements
"""

cars = ['audi', 'bmw', 'subaru', 'toyota']
for i in cars:
    if i =="bmw":
        print(i.upper())
    else:
        print(i.title())

#Operators to be used.
# =
# == equal to
# != not equal to
# < greater than
# <= equal and smaller than.
# >=equal and greater than

#Checking multiple conditions
age_0 =22
age_1 = 18
age_0 >= 21 and age_1 >=21 # this will return FALSE

"""
Checking whether a Vlaue is in a list.
We use the no in if we want to check if something is not in a list.
"""
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(user.title() + ", you can post a response if you wish.")

#Exercise
"""
-1. Conditional Tests: Write a series of conditional tests. Print a statement 
describing each test and your prediction for the results of each test. Your code 
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•	 Look closely at your results, and make sure you understand why each line 
evaluates to True or False.
•	 Create at least 10 tests. Have at least 5 tests evaluate to True and another 
5 tests evaluate to False.
"""
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#IF STATEMENTS
"""
if conditional_test:
 do something
"""
age =19
if age >= 18:
    print("You are old enough to vote")

age = 17
if age >=18:
    print("you are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
#But if we have more than 2 conditions, then we will use elif statement.
age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 5
else:
 price = 10
print("Your admission cost is $" + str(price) + ".")

#More conditions.
age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 5
elif age < 65:
 price = 10
elif age >= 65:
 price = 5
print("Your admission cost is $" + str(price) + ".")

#More conditions:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")
 
print("\nFinished making your pizza!")    

#Exercises
"""
 Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•	 Write an if statement to test whether the alien’s color is green. If it is, print 
a message that the player just earned 5 points.
•	 Write one version of this program that passes the if test and another that 
fails. (The version that fails will have no output.)

"""
alien_color =['green','yellow','red']
for i in alien_color:
    if (i =='green'):
        print("You just earned 5 points")
    else:
        print("You failed the task")


alien_color =['green','yellow','red']
for i in alien_color:
    if (i=='green'):
        print("You just earned 5 points")
    else:
        if (i != 'green'):
            print("You just earned 10 points")

#We have more than 2 conditions            
alien_color =['green','yellow','red']
for i in alien_color:
    if(i =='green'):
        print("you just earened 5 points")
    elif i == 'yellow':
            print("you just earned 10 points")
    else:
        if(i =='red'):
            print("You just earned 15 points.")
            
#Set up 
        
persons =[]
for i in persons:
    if (i < 2):
        print("That person is a baby.")
    elif i >= 2 & i < 4:
        print("That person is a toddler")
    elif i >= 4 & i<13:
        print("Print the person is a kid")
    elif i >=13 & i<20:
        print("That person is a teenager")
    elif i>=20 & i<65:
        print("That person is an adult")
    else:
        if(i>=65):
            print("That person is an elder.")


#Other examples include the following:
"""

"""    
usernames=["admin","kuhle","darren","ali","toko","amanda"]
for i in usernames:
    if (i =='admin'):
        print('\nHello,'+ i.title() + " "+ "would you like to see a status report?")
    else:
        if(i !='admin'):
            print("\nHello," + i.title() +" "+"thank you for longing in again.")


"""
Craete a program that simulates
how websites ensure that everyone has a unique username.
See if each new username has been used already, and if it has
"enter a new username, or username is available."
So basically this is a comparison
"""
current_users=["admin","kuhle","darren","ali","toko","amanda"]
new_users=["athi","bulumko","lufefe","lutho","ali"]

for i in new_users:
    if (i in current_users):
        print("\nThis username already exists, please create a new one.")
    else:
        if(i not in current_users):
            print("\nThis username is available.")


"""
Ordinal numbers
Store numbers 1 to 9 in a list.
Loop through the list
Use if-elif-else chain to print the proper ordinal for each number.
Each result be on a seperate line.
"""
numbers = list(range(1, 10))
print(numbers)
for i in numbers:
    if (i == 1):
        print("\n1st")
    elif i == 2:
        print("\n2nd")
    elif i == 3:
        print("\n3rd")
    elif i == 4:
        print("\n4th")
    elif i == 5:
        print("\n5th")
    elif i == 6:
        print("\n6th")
    elif i == 7:
        print("\n7th")
    elif i == 8:
        print("\n8th")
    else:
        if(i==9):
            print("\n9th")
        
        














