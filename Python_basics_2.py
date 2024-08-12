# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:34:06 2024

@author: mcing
practising how to code in python 2
"""

#In the pervious exercise we learnt how to perform how to loop through 
#an entire list using just few lines of code regardless of how.

magicians = ['alice', 'david', 'carolina'] 
for i in magicians: 
 print(i)
 
#Doing more work within a for loop.
#So in the loop below we want to Give the elements of the loop,
#Capital letters, and after that add the rest of the sentence.
magicians = ['alice', 'david', 'carolina'] 
for i in magicians:
    print(i.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + i.title() + ".\n")
    #The print function below is after 
print("Thank you, everyone. That was a great magic show!")

#Execises
"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these 
pizza names in a list, and then use a for loop to print the name of each pizza.
•	 Modify your for loop to print a sentence using the name of the pizza 
instead of printing just the name of the pizza. For each pizza you should 
have one line of output containing a simple statement like I like pepperoni 
pizza.
•	 Add a line at the end of your program, outside the for loop, that states 
how much you like pizza. The output should consist of three or more lines 
about the kinds of pizza you like and then an additional sentence, such as 
I really love pizza!
4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to 
print out the name of each animal.
•	 Modify your program to print a statement about each animal, such as 
A dog would make a great pet.
•	 Add a line at the end of your program stating what these animals have in 
common. You could print a sentence such as Any of these animals would 
make a great pet!

"""
pizza =["paperroni","chilli chicken","mushroom"]
#Print a sentence for each pizza
for i in pizza:
    print("I like" + " "+ i + " "+"pizza"+".\n")
print("I really love pizza!")

pets =["dog","cat","horse"]
#Print a sentence for each pizza
for i in pets:
    print("A"+ " "+ i+ " "+"would make a great pet"+ ".\n")
print("Any of these animals would make a great pet")

#Making Numerical Lists.
#Python’s range() function makes it easy to generate a series of numbers. 
#For example, you can use the range() function to print a series of numbers 
#like this:
#Range(start,stop,step)

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
inclusive.
4-4. One Million: Make a list of the numbers from one to one million, and then 
use a for loop to print the numbers. (If the output is taking too long, stop it by 
pressing ctrl-C or by closing the output window.)
4-5. Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and 
ends at one million. Also, use the sum() function to see how quickly Python can 
add a million numbers.
4-6. Odd Numbers: Use the third argument of the range() function to make a list 
of the odd numbers from 1 to 20. Use a for loop to print each number.
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to 
print the numbers in your list.
4-8. Cubes: A number raised to the third power is called a cube. For example, 
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
is, the cube of each integer from 1 through 10), and use a for loop to print out 
the value of each cube.
4-9. Cube Comprehension: Use a list comprehension to generate a list of the 
first 10 cubes
"""    
for value in range(1,5):
 print(value)    

#Now let us create a list of numbers.
even_numbers = list(range(2,11,2))  # the list starts with 2, and ends at 11. Each value is multiplied by 2
print(even_numbers)

squares = []
for i in range(1,11):
    square=i**2
    squares.append(square)
print(squares)

#Another example is a List Comprehenson
squares1=[i**2 for i in range(1,11)]
print(squares1)
#but then list comprehensions can be complicated,
#So using the ussual one above.

#EXERCISE
for values in range(1,20):
     print(values)
     
#Odd Numbers: Use the third argument of the range() function to make a list 
#of the odd numbers from 1 to 20. Use a for loop to print each number.
for values in range(1,20,3):
    print(values)

#Make a list of the multiples of 3 to 30
multiples=[]
for i in range(3,30):
    multi=i*3
    multiples.append(multi)
print(multiples)

#make a list of the first 10 cubes.
cubes=[]
for i in range(1,10):
    cube=i**3
    cubes.append(cube)
print(cubes)

#Working with Part of a list.
#This aprt of the exercise is calledslicing a List.
#This is when we want only a port of the list not everything.

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3]) #this will be from first to 3rd
print(players[1:4]) #This will be from 2nd to 4th
print(players[:4]) #This will read from 4th position to 1st from back
print(players[2:])#This will be from 3rd to last postion
print(players[-3:]) #This gives us the last three from the back.

#Now if we want to loop through a Slice:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players:")
for i in players[0:3]:
    print(i.title())

#Exercises:
"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several 
lines to the end of the program that do the following:
•	 Print the message, The first three items in the list are:. Then use a slice to 
print the first three items from that program’s list.
•	 Print the message, Three items from the middle of the list are:. Use a slice 
to print three items from the middle of the list.
•	 Print the message, The last three items in the list are:. Use a slice to print 
the last three items in the list
"""    

cars = ["toyota","vw","mercedes","jeep","suzuki","ranger"]
print("The first three items in the list are:"+".\n")
for i in cars[0:3]:
    print(i.title())
print("Three items from the middle of the list are:"+".\n")
for n in cars[1:5]:
        print(n.title())
print("The last three items in the list are:"+".\n")
for m in cars[-3:]:
            print(m.title())
            


























