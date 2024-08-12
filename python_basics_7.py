# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 13:03:18 2024

@author: mcinga
FUNCTIONS
Learning how to write functions whose primary job is to display information and other functions.
Learn how to store functions in seperate files called modules to help organize the main program
"""
"""
In the preceding greet_user() function, we defined greet_user() to require a 
value for the variable username. Once we called the function and gave it the 
information (a person’s name), it printed the right greeting. 
The variable username in the definition of greet_user() is an example of a 
parameter, a piece of information the function needs to do its job. The value 
'jesse' in greet_user('jesse') is an example of an argument. An argument 
is a piece of information that is passed from a function call to a function. 
When we call the function, we place the value we want the function to work 
with in parentheses. In this case the argument 'jesse' was passed to the 
function greet_user(), and the value was stored in the parameter username.
"""
def greet_user(username):
    """Display a simple greeting"""
    print("Hello!"+ " "+username.title()+"!")

greet_user('jesse')

#Exercise
"""
Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the 
function, and make sure the message displays correctly.
"""
def display_message(username):
    print("Hello"+ " "+ username.title()+ " "+ "is  learning functions in this chapter!")
    
display_message("jesse")

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one 
parameter, title. The function should print a message, such as One of my 
favorite books is Alice in Wonderland. Call the function, making sure to 
include a book title as an argument in the function call.
"""
def favorite_book(title):
    print("One of my favourite books is"+ " "+title.title()+".")
    
favorite_book('Cinderella')    

#Passing arguments
"""
You can pass arguments to your functions 
in a number of ways. You can use positional arguments, which need to be in 
136 Chapter 8
the same order the parameters were written; keyword arguments, where each 
argument consists of a variable name and a value; and lists and dictionaries 
of values. Let’s look at each of these in turn
"""
#Positional Arguments
def describe_pet(animal_type, pet_name):
    '''Display information about a pet'''
    print("\nI have a"+ " "+animal_type+".")
    print("My"+" "+animal_type+"'s name is"+ " "+pet_name.title()+".")

describe_pet('dog', 'tyson')

def make_shirt(size,text):
    print("\nThe size of the shirt is"+ " "+ str(size)+".")
    print("\nThe message printed on the shirt is:"+ " "+ text.title())
    
make_shirt(32, "SpongeBob Square Pants")    

#
def make_shirt2(size,text):
    if (size == 40):
        print("\nMy size is"+" "+str(size)+" "+"and"+" "+text+ " "+" I love Python.")
    elif size == 34:
        print("\nMy size is"+" "+str(size)+" "+"and"+" "+text+ " "+"I love Python.")
    elif size <=32:
        print("\nMy size is"+" "+str(size)+" "+"and"+" "+text+ " "+"I love BioPython.")

make_shirt2(26, "my shirt reads,")

def describe_city(city_name,country):
    print(city_name.title()+ " "+ "is in"+ " "+country.title())
    
describe_city("Monti", "South Africa") 

#Return Values
"""
A function doesnt always have to display its output directly.
Instead, it can process data and then return a valur or set of values.
"""
def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted"""
    full_name=first_name+" "+last_name #function combines these two names, and adds a space
    return full_name.title() #The title of fullname is converted into Capital letters.

musician=get_formatted_name("jimi", "hendrix")
print(musician)

"""
When you call a function that returns a value, you need a variable
that will store the return value.
In this case the return value is stored in musician
"""
#But if we want to create a functionthat is flexible and can take more options,
#We can use conditional statements.

def formatted_name(first_name,last_name,middle_name=""):
    if middle_name:
        full_name=first_name+" "+middle_name+" "+last_name
    else:
        full_name=first_name+" "+last_name
    return full_name.title()

artist=formatted_name("jason","balboa")
print(artist)

rapper=formatted_name("kelly", "duarte","lee")
print(rapper)


#Returning a function on lists and dictionaries.

def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendrix')
print(musician)

def build_person2(first_name,last_name,age):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
artist2=build_person2('jimi', 'mcinga', age=27)
print(artist2)

#Using a Function with a while loop.
def get_formatted_name(first_name,last_name):
    full_name=first_name+" "+last_name
    return full_name
#So the function is created

active=True
while active:
    print("\nplease tell me your name:")
    print("\(enter 'q' at any time to quit)")
    f_name=input("First name:")
    if f_name =='q':
        break #this where we exit the loop if the condition is met.
    l_name=input("Last name:")
    if l_name =='q':
        break
    #Below is when we call in the function:
    formatted_name=get_formatted_name(f_name, l_name)
    print("\nhello,"+ " "+formatted_name+"!")



responses ={}

polling_active =True
while polling_active:
    name =input("\nWhat is your name?")
    response=input("\nWhich mountain would you like to climb someday?")
    #Store the response into a dictionary.
    responses[name]=response
    repeat=input("\nWould you like to let another person respond? (yes/no)")
    if (repeat == 'no'):
        break
print("\n----Poll Results-----")
for name,response in responses.items():
    print(name + " "+ "would like to climb"+ " "+response+".")
    
#Exercise
def city_country(city,country):
    places=city+","+" "+country
    return places
travel=city_country("London", "United Kingdom")
print(travel)    

#Write a function called make_album() that builds a dictionary 
#describing a music album. The function should take in an artist name and an 
#album title, and it should return a dictionary containing these two pieces of 
#information 
   
#===================
def make_albumn2(name,title):
    information= name+ " "+title
    return information

info={}
active = True
while active:
    name=input("\nWho is your favorite artist?")
    title=input("\nWhat is your favourite albumn?")
    #Store this into a dictionary
    info[name]=title
    response=input("\nWould you like to allow someone else to respond? (yes/no)")
    if (response == 'yes'):
        continue
    else:
        break
    f=make_albumn2(name, title)
print("\n----Poll Results-----")
for name,title in info.items():
    print(name + "'s"+" "+ "favourite albumn is"+ " "+title+".\n")
    
"""
Passing a List
"""
def greet_user(names):
    for i in names:
        msg="Hello, "+i.title()+"!"
        print(msg)

usernames =['hannah','ty','margot']
greet_user(usernames)

#================
"""
Modifying a List in a Function.
Consider a company that creates 3D printed models of designs that 
users submit. Designs that need to be printed are stored in a list, and after 
being printed they’re moved to a separate list.
"""
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models =[]

while unprinted_designs:
    current_design=unprinted_designs.pop()
    print("\nPrinting model:" + current_design)
    completed_models.append(current_design)
    
#Display all completed models.
print("\nThe following models have been printed:")
for i in completed_models:
    print(i)    

#======================================
"""
Simulate printing each design, until none are left.
Move each design to completed_models after printing.
"""
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for i in completed_models:
        print(i)
        
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Exercise
"""
Make a list of magician’s names. Pass the list to a function 
called show_magicians(), which prints the name of each magician in the list.
"""
magicians=['bobby','wiro','notebook','marlin']
def show_magicians(magicians):
        print("\nThese are the magicians that will perform this evening:")
        for i in magicians:
            print("\n"+i.title())
        
show_magicians(magicians)    

"""
Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to 
see that the list has actually been modified
"""
def make_great(magicians):
    for i in magicians:
        print("\nthe Great"+" "+ i.title()+"!")
    
make_great(magicians)

"""
Unchanged Magicians: Start with your work from Exercise 8-10. Call the 
function make_great() with a copy of the list of magicians’ names. Because the 
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to ea
"""
magicians=['bobby','wiro','notebook','marlin']
new_magicians=[]

def print_magicians(magicians, new_magicians):
    while magicians:
        current= magicians.pop()
        #Simulate creating a 3D print from the design.
        print("\nPrinting magician: " + current_design)
        new_magicians.append(current)

print_magicians(magicians, new_magicians)
def show_magicians(magicians):
        print("\nThese are the magicians that will perform this evening:")
        for i in magicians:
            print("\n"+i.title())        
show_magicians(new_magicians)






































































































































