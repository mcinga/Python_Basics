# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:50:49 2024

@author: mcing
USERS INPUT AND WHILE LOOPS
Programs are writtn to solve an end user's pronlem.'
To do that they need to get information fromthe end user.
For example :
    if we want to find out if someone is eligible to vote or not
    we would have to get an input from the voter.
    so this is wher we would use the input() function.
"""
#The input() function pauses your program and waits for the user to enter some text.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Writing clear prompts

name = input("Please enter your name: ")
print("Hello, " + name + "!")

"""
You can store your prompt in a variable and pass that variable to the input()
function. This allows you to build your prompt over several lines, then write 
a clean input() statement
"""
# += is a way of adding value to an already existing variable.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

"""
If we want to accept a numerical input then we use the int() function
"""

age =input("How old are you? ")
print("\nI am ", age)


height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
 print("\nYou're tall enough to ride!")
else:
 print("\nYou'll be able to ride when you're a little older.")


#The Modulo Operator
#This devides one number by another number and returns the remainder
# 4%3 = 1
# 5%3 = 2
# 6%3 =0

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print("\nThe number " + str(number) + " is even.")
else:
 print("\nThe number " + str(number) + " is odd.")



























