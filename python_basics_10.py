# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:53:54 2024

@author: mcinga
Analyze Text
"""
filename ="alice.txt"
try:
    with open(filename) as f_obj:
        contents =f_obj.read()
except FileNotFoundError:
    msg ="Sorry, the file" +" "+ filename +" "+ "does not exist."
    print(msg)
else:
    words =contents.split()
    num_words =len(words)
    print("The file"+" "+filename+" "+"has about"+" "+str(num_words)+" "+"words")
    

#Working with Multiple Files.
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read() 
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        """ Count approximate number of words in the file."""
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + 
 " words.")
filename = 'alice.txt'
count_words(filename) 

filenames =['alice.txt','little_women.txt','peter_pan.txt']
for i in filenames:
    count_words(i)
    

active =True
while active:
    try:
        one=int(input("Enter the first number:\n"))
    except ValueError:
        print("That is not a valid number.PLease enter a valid number.")
        continue
    try:
        two=int(input("Enter the second number:\n"))
    except ValueError:
        print("That is not a valid number.PLease enter a valid number.")
        continue
    print("The sum is :"+ str(one +two))
    repeat=input("Would you like to add another numner. (yes\no)\n")
    if (repeat == "yes"):
        continue
    elif repeat =="no":
        break
    
        
        
        































































                        