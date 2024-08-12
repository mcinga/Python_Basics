# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:45:19 2024

@author: mcinga
"""
#Using Arbitrary Keyword Arguments.
"""
Sometimes you’ll want to accept an arbitrary number of arguments, but you 
won’t know ahead of time what kind of information will be passed to the 
function. In this case, you can write functions that accept as many key-value 
pairs as the calling statement provides.

The function build_profile() in the 
Functions 153
following example always takes in a first and last name, but it accepts an 
arbitrary number of keyword arguments as well:
"""
def build_profile(first,last,**user_info):
    profile ={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile=build_profile('albert', 'einstein',
                           location='princeton',
                           field='physics')
print(user_profile)

#====================
"""
""" 
items=['ham','mayo','avocado','egg'] 
ordered_sandwiches = []
def sandwiches(items):
    while items:
        current_order=items.pop()
        ordered_sandwiches.append(current_order)
       
sandwiches(items)
def sandwiches2(ordered_sandwiches):
    print("\nThese are the ordered sandwiches:")
    for i in ordered_sandwiches:
        print("\n"+i.title())
    
sandwiches2(items)   


def make_car(manufactor,model,color='',tow_package=''):
    car={'manufactor':manufactor,'model':model}
    if color:
        car['color']=color
    if tow_package:
        car['tow_package']=tow_package
    return car
        
make=make_car("Toyota", "Fortuna",color="blue",tow_package="True")                
print(make)    


#Importing an Entire Module
def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print("\nMaking a " + str(size) +
 "-inch pizza with the following toppings:")
 for topping in toppings:
     print("- " + topping)























































































































    