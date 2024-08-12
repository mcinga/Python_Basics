# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:48:59 2024

@author: mcinga
Classes

"""

"""
Creating and Using a Class
You can model almost anything using classes. Let’s start by writing a simple 
class, Dog, that represents a dog—not one dog in particular, but any dog. 
What do we know about most pet dogs? Well, they all have a name and age. 
We also know that most dogs sit and roll over. Those two pieces of information (name and age) and those two behaviors (sit and roll over) will go 
in our Dog class because they’re common to most dogs. This class will tell 
Python how to make an object representing a dog. After our class is written, 
we’ll use it to make individual instances, each of which represents one specific dog
"""

# Creating the Dog Class
#Each instance created from the Dog class will store a name and an age, and 
#we’ll give each dog the ability to sit() and roll_over()

#By convention, capitalized names refer to classes in Python. 
#The parenthesis are empty because the class is being created from scratch.

class Dog():
    """A simple attempt to model a dog"""
    def __init__(self,name,age): #3 (this one has 3 parameters. the self parameter is a must come first in the _int_)
        """Initialize name and age attributes"""
        self.name=name #4
        self.age=age
        
    def sit(self): #5
        """Simulate a dog sitting in response toa command"""
        print(self.name.title()+" "+"is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title()+" "+"rolled over!")
        
        
my_dog =Dog('willie',6)        
print("My dog's name is"+" "+my_dog.name.title()+".")        
print("My dog is"+ " "+str(my_dog.age)+ " "+"years old")        
        
my_dog.sit()
my_dog.roll_over()        
        
#Exercise        
        
"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods
"""        

        
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        # It's better to return the string rather than printing it
        return f"{self.restaurant_name.title()}\n{self.cuisine_type.title()}"

    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is open.")        
        
eatery = Restaurant("Ballitos", "portuguese chicken")
# Now you can print the returned string and its title
print(f"My favorite restaurant is {eatery.describe_restaurant()} and my favorite food is {eatery.cuisine_type.title()}.")
        
print(f"{eatery.open_restaurant()}")        
        
        
"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user.

"""       

class User():
    def __init__(self, first_name, last_name, color='', home_town=''):
        self.first_name = first_name
        self.last_name = last_name
        self.color = color
        self.home_town = home_town
        
    def describe_user(self):
        print(f"\n-----Summary of user------\n{self.first_name}\n{self.last_name}\n{self.color}\n{self.home_town}")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

current_user = User("Billy", "Downer", color="blue")
print("Hi " + str(current_user))
print("Hi I am " + current_user.describe_user())


"""
Working with Classes and Instances
Once you write 
a class, you’ll spend most of your time working with instances created from 
that class. One of the first tasks you’ll want to do is modify the attributes 
associated with a particular instance. You can modify the attributes of an 
instance directly or write methods that update attributes in specific ways.
"""
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def get_descriptive_name(self):
        long_name=str(self.year)+ ' '+self.make+' '+self.model
        return long_name.title()
    
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())



























































































































       
        