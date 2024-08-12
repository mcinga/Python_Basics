# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:01:17 2024

@author: mcing

Practising how to code in python
"""
message = "Hello python"
print(message)

"""
A string is a series of characters.
"""
#Changing Case in a String with MEthods
name="ada lovelace"
print(name.title())
#So the above title function chan
print(name.upper())
print(name.lower())

#Combining or Concatenating Strings.
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
#So python uses the plus symbol (+) to combine strings.
print("Hello," + full_name.title() + "!")

#Removing the Whitespaces in the string.
#For example "python" and "python "
#Removing the whitespaces in a string using .rstrip()
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language

#Removing a white space from the left side of the 
favorite_language = ' python '
favorite_language = favorite_language.rstrip() # removing the white space on the right
favorite_language
favorite_language = favorite_language.lstrip() #removing the white space on the left
favorite_language
favorite_language.strip() #removing the white space from both side.

#Introducing Lists
# A list is a collection of items in a partivular oder.
#For example, in R the list would look like b<-list(1,2,3,4)
#In python the lists are shown using square brackets [].

b = ["trek","cannondale","redline","specialised"]
print(b)

#Accessing Elements in a List
print(b[0]) 
print(b[0].title())

#Indexing positions
#Here we want to get the last element of the list 
print(b[-1])

#Using individual values from a list.
#So then 
message = "My first bicycle was a"+" "+b[0].title() + "."
print(message)

#You can also combine tabs and newlines in a single string. The string 
#"\n\t" tells Python to move to a new line, and start the next line with a tab.
print("Languages:\nPython\nC\nJavaScript")

#You can do this by wrapping the variable in the 
#str() function, which tells Python to represent non-string values as strings
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
"""
Exercise 3-1
1. Store the names of a few of your friends in a list called names. Print 
each person’s name by accessing each element in the list, one at a time.
2. Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
person’s name.
3. Think of your favorite mode of transportation, such as a 
motorcycle or a car, and make a list that stores several examples. Use your list 
to print a series of statements about these items, such as “I would like to own a 
Honda motorcycle.” 
"""
#1
names=["kuhle","bulela","mlibo","nosipho","tshidi","pheziwe","sisipho"]
print(names[0])
print(names[0:3])

#2
green ="hello" + " "+ names[0] + " "+ "lets us go buy coffee."
print(green)

#3

#Changing, Adding and Removing Elements.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Modifying elements in an existing list.
#So when I placed [2], it replaced the suzuki
motorcycles[2] ="ducati"
print(motorcycles)

motorcycles[0] ="bmw"
print(motorcycles)

#Adding elements to  a list.
#The simplets way to add elements into an empty list is to use the append function.

motorcycles2 = ['honda', 'yamaha', 'suzuki']
print(motorcycles2)
motorcycles2.append('ducati')
print(motorcycles)

#But now if we have an empty list, we can add things onto that empty list,
motorcycles3 = [] 
motorcycles3.append('honda') 
motorcycles3.append('yamaha') 
motorcycles3.append('suzuki') 
print(motorcycles3)

#Inserting elements into a list
motorcycles3.insert(3,"ducti")
print(motorcycles3)

#Removing an item using the DEL statement
del motorcycles3[1] 
print(motorcycles3)

#The pop() method removes the last item in a list, but it lets you work 
#with that item after removing it.
motorcycles4 = ['honda', 'yamaha', 'suzuki']
print(motorcycles4)
popped_motorcycle = motorcycles4.pop() 
print(motorcycles4)
print(popped_motorcycle)

"""
1. Guest List: Make a list that includes at least three people you’d like to 
invite to dinner. Then use your list to print a message to each person, inviting 
them to dinner.

2. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the 
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still 
in your list.

3. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a 
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.

"""
#1
guests = ["kuhle","bulela","mlibo"]
time=18
print(guests[0].title() + " "+"Would you like to join me for dinner at" + " "+str(time)+ ".")
print(guests[1].title() + " "+"Would you like to join me for dinner at" + " "+str(time)+ ".")
print(guests[2].title() + " "+"Would you like to join me for dinner at" + " "+str(time)+ ".")

for i in guests:
    print(i+ " "+"Would you like to join me for dinner at" + " "+str(time)+ ".")

#2
guests = ["kuhle","bulela","mlibo"]
time=18
print(guests[0].title() + " "+"Would you like to join me for dinner at" + " "+str(time)+ ".")
print(guests[1].title() + " "+"Would you like to join me for dinner at" + " "+str(time)+ ".")
print(guests[2].title() + " "+"won't make it for dinner at" + " "+str(time)+ ".")

#3
guests[2]="ngisa"
print(guests[2].title() + " "+"will join me for dinner at" + " "+str(time)+ ".")
print(guests[1].title() + " "+"Would you like to join me for dinner at" + " "+str(time)+ ".")
print(guests[0].title() + " "+"Would you like to join me for dinner at" + " "+str(time)+ ".")

#4
#The insert() function allows me to add elements into my list into a specified position.
guests = ["kuhle","bulela","mlibo"]
guests.insert(0,"lumko")
guests.insert(4,"tata")
guests.append(("dixon"))
print(guests)

#5
print("I can only invite only two people")
removed_guests = guests.pop()
removed_guests2 = guests.pop()
print("Unfortunately I cannot invite you for dinner" + " "+removed_guests+".")
print("Unfortunately I cannot invite you for dinner" + " "+removed_guests2+".")

print(guests)


#Sorting a List permanently with the sort() function.
#This will be in ascending order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Now if we want to sort it out in reverse form, in ascending order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)    

#printing a List in reverse order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#When one wants to have a reverse of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Finding the length of a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)




















