# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:51:11 2024

@author: mcinga

The for loops takes a collection of items and executes a block of code,
once for each item in the collection. In contrast, the while loop runs 
as long as, or while a certain condition is true.
"""
#You can use a while loop to count up through a series of numbers.
#For example, the following while  loop counts from 1 to 5.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1
    
"""
In the first line, we start counting from 1 by setting the value of 
current_number to 1. The while loop is then set to keep running as long 
as the value of current_number is less than or equal to 5. The code inside 
the loop prints the value of current_number and then adds 1 to that value 
with current_number += 1. (The += operator is shorthand for current_number = 
current_number + 1.) 
"""

""" 
For example, a game needs a while loop to keep running as long as you want 
to keep playing, and so it can stop running as soon as you ask it to quit
"""
prompt ="\nTell me something, and I will repeat it back to you:"
prompt +="\nenter 'quit' to end the program"

message =""
while message != 'quit':
    message=input(prompt)
    print(message)
    
#The program above works well, but it does not quit after putting in qiut.
# So by having a if statement then it should work.    
    
prompt ="\nTell me something, and I will repeat it back to you:"
prompt +="\nenter 'quit' to end the program"

message =""
while message != 'quit':
    message=input(prompt)
    if message != 'quit':
        print(message)
    #print(message)  
    
'''
Using a Flag

In the previous example, we had the program perform certain tasks while 
a given condition was true. But what about more complicated programs in 
which many different events could cause the program to stop running?
For example, in a game, several different events can end the game. 
When the player runs out of ships, their time runs out, or the cities they 
were supposed to protect are all destroyed, the game should end. It needs 
to end if any one of these events happens. If many possible events might 
occur to stop the program, trying to test all these conditions in one while
statement becomes complicated and difficult
'''
    
    
"""
For a program that should run only as long as many conditions are true, 
you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We 
can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. As a result, 
our overall while statement needs to check only one condition: whether or 
not the flag is currently True. Then, all our other tests (to see if an event has 
occurred that should set the flag to False) can be neatly organized in the rest
"""   

basic = "\nTell me something, and I will repeat it back to you:"
basic += "\nEnter 'quit' to end the program. "
 
active = True #This monitors if the programm should continue running
while active:
 basic = input(basic)
 if basic == 'quit':
     active = False
 else:
     print(basic)
     
"""
Using a break to exit a loop.
This is where we exit the loop, with out running the rest of the,
code. We will be using the break command.
"""
entry = "\nPlease enter the name of a city you have visited:"
entry += "\n(Enter 'quit' when you are finished.) "
while True:
 city = input(entry)
 
 if city == 'quit':
     break
 else:
     print("I'd love to go to " + city.title() + "!")


entry2 = "\nPlease enter the name of a city you have visited:"
entry2 += "\n(Enter 'quit' when you are finished.) "

city = True
while city:
 city = input(entry2)
 
 if city == 'quit':
     break
 else:
     print("I'd love to go to " + city.title() + "!")


"""
Using continue in a Loop
Rather than breaking out of a loop entirely without executing the rest of its 
code, you can use the continue statement to return to the beginning of the 
loop based on the result of a conditional test. For example, consider a loop 
that counts from 1 to 10 but prints only the odd numbers in that range:
"""

current_number = 0
while current_number < 10:
 current_number += 1
 if current_number % 2 == 0:
     continue
 
 print(current_number)

"""
current_number =0
current_number =+ 1
while current_number < 10:
    if current_number % 2 ==0:
        continue
print(current_number)

this one did not work
"""

x = 1
while x <= 5:
 print(x)
 x += 1

#So the code below, is adding going through the numbers below 5,
#and adding 1 before printing them.
y= 1
while y <=5:
    y+=1
    print(y)
#Exercises.
"""
A while loop will continue asking for an input until the end user,
tells it to stop in this case the user inouts "stop"
"""

"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza
"""

pizza = "\nPlease select your pizza toppings.\n"
topping = True
while topping:
    topping=input(pizza)
    if topping == 'quit':
        break
    else:
        print("\nI will add that topping to your pizza!")


"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15. Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket.
"""
"""
The try block contains code that might cause an exception to occur. 
In this case, it’s the conversion of user_input to an integer with int(user_input).
If the user enters something that’s not a number, this will raise a ValueError.
The except ValueError block is executed if the ValueError exception is raised inside the try block. 
It catches the exception and allows you to handle it gracefully.
Here, it informs the user to enter a valid age and resets age to None to prompt the user again.
"""        
  
text5 = "\nPlease enter your age.\n"
age2 = True
# Start the loop with True as the condition
while age2:
    user_input = input(text5)
    try:
        # Convert the input to an integer
        age = int(user_input)
        
        # Check the age and print the corresponding message
        if age < 3:
            print("Ticket is free!")
            break  # Exit the loop
        elif 3 <= age < 12:
            print("The ticket is $10")
            break  # Exit the loop
        elif age >= 12:
            print("The ticket is $15")
            break  # Exit the loop
    except ValueError:
        # If the input is not a valid integer, print an error message
        print("Please enter a valid age.")
       
"""
Moving items from one list to Another
"""
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
 current_user = unconfirmed_users.pop()
 print("Verifying user: " + current_user.title())
 confirmed_users.append(current_user)
 
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
 print(confirmed_user.title())

    
#Filling a dictionary with User input
responses ={}

polling_active =True
while polling_active:
    name =input("\nWhat is your name?")
    response=input("\nWhich mountain would you like to climb someday?")
    #Store the response into a dictionary.
    responses[name]=response
    repeat=input("\nWould you like to let another person respond? (yes/no)")
    if (repeat == 'no'):
        polling_active=False #I could use break here.
print("\n----Poll Results-----")
for name,response in responses.items():
    print(name + " "+ "would like to climb"+ " "+response+".")
    
    
#Exercise
"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop 
through the list of sandwich orders and print a message for each order, such 
as I made your tuna sandwich. As each sandwich is made, move it to the list 
of finished sandwiches. After all the sandwiches have been made, print a 
message listing each sandwich that was made.
"""    
sandwiches=['butter','jam','peanut butter']
finished_sandwiches=[]

while sandwiches:
    made=sandwiches.pop()
    print("\nI have made your" + " "+ made +" "+ "sandwich."+"\n")
    finished_sandwiches.append(made)
print("These are the sandwiches that have been made:")
for i in finished_sandwiches:
    print(i+"\n")
    

"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
the sandwich 'pastrami' appears in the list at least three times. Add code 
near the beginning of your program to print a message saying the deli has 
run out of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
in finished_sandwiches.
"""
sandwich_orders=['pastrami','butter','pastrami','jam','peanut butter','pastrami','tuna']   
complete_orders=[]

print("\nThe deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
        made=sandwich_orders.pop()
        print("\nI have made your" + " "+made+" "+"sandwich."+"\n")
        complete_orders.append(made)
print("These are the sandwiches that have been made:")
for i in complete_orders:
    print(i+"\n")
    

"""
7-10. Dream Vacation: Write a program that polls users about their dream 
vacation. Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll.
"""
wish="If you could visit one place in the world where would you go?"
place=True
results2={}
while place:
    name=input("What is your name?\n")
    age=input("How old are you?\n")
    country=input(wish)
    results2[name]=country
    try:
        age3=int(age)
    except ValueError:
        print("Please enter a valid number.\n")
        #continue
        #results2[name]=country
    repeat=input("\nWould you like to let another person respond? (yes/no)")
    if (repeat == 'no'):
        place=False       
print("\n----Poll Results-----\n")
for name,country in results2.items():
    print("My name is"+ " "+ name+ " I want to visit"+ " "+country.title()+".\n")
    
    
   
    
    
    
    
    
    