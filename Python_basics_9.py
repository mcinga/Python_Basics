# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:15:47 2024

@author: mcinga
FILES AND EXCEPTIONS.
"""

"""
The first line of this program has a lot going on. Let’s start by looking 
at the open() function. To do any work with a file, even just printing its contents,
you first need to open the file to access.

The keyword with closes the file once access to it is no longer needed. 
Notice how we call open() in this program but not close(). You could open 
Files and Exceptions 191
and close the file by calling open() and close(), but if a bug in your program 
prevents the close() statement from being executed, the file may never 
close. This may seem trivial, but improperly closed files can cause data 
to be lost or corrupted. And if you call close() too early in your program, 
you’ll find yourself trying to work with a closed file (a file you can’t access), 
which leads to more errors.
"""
with open ('pi_digits.txt') as file:
    contents=file.read()
    print(contents.rstrip()) #removing white spaces on the right side of the string.

"""
Reading Line by Line
"""
filename ="pi_digits.txt"

with open(filename) as file_object:
    """Making a List of Lines from a File"""
    lines=file_object.readlines() #readlines takes each line from file and stores it in a list
    """Working with a File's Contents"""
    pi_string="" #this will hold the digits of pi
    for line in lines:#this adds each line of digits to the pi string and removes the new line character.
      pi_string+=line.strip()  
    print(pi_string) # prints the string
    print(len(pi_string)) #tells us the length of the string.
    

filename2="pi_million_digits.txt"
with open(filename2) as fn:
    lines=fn.readlines()
    pi2_string=""
    for i in lines:
        pi2_string+=i.strip()
    print(pi2_string[:16]+"...")
    print(len(pi2_string))
        
with open(filename2) as fl:
    lines=fl.readlines()
    pi3_string=""
    for i in lines:
        pi3_string+=i.strip()
    try:
        birthday=input("Enter your birth,in the form mmddyy:")
        int_birthday=int(birthday) #Converting it into integer to trigger ValueError.
        if (birthday in pi3_string):
            print("Your birthday appears in the first million didgits of pi!")
        else:
            print("Your birthday does not appear in the first million digits of pi!")
    except ValueError:
        print("Please enter a valid number consisting of digits only!")
    

#Exercises:
with open("learning_python.txt") as lp:
    lines=lp.readlines()
    text=" "
    for line in lines:
        text+=line.strip()
                
#Reading a fasta file:
#Will import it as a module on another script.
#def read_fasta(filename):   
with open(filename.fas) as file:
    sequences=[] #for every sequence that is read and done it is stored here.
    sequence= " " #Store the sequence here, and when it it done move it to the sequences list.
    for line in file:
        line=line.strip() # removing white spaces in both sides
        if line.startswith(">"):
            if sequence:
                sequences.append(sequence)
                sequence=" " # Starting a new sequence, meaning that the first one has been read and appended to sequences list. So reading a new one now.
            else:
                sequence+=line
    if sequence: #looking for the last sequence.
        sequences.append(sequence)
#return sequences

"""
Writing to a file
"""
filename3="programming.txt"
with open(filename3,'w') as file_object:
    file_object.write("I love programming")

filename4="Programming2.txt"
with open(filename4,'w') as file:
    file.write("I love programming!\n")
    file.write("I love creating new games.\n")

#Exercise
responses=[]
active=True
while active:
    prompt=input("Please enter your name.")
    responses.append(prompt)
    print("Hello!"+ " "+ responses[-1]+ "\n")
    with open("guest_book.txt","a") as file:
        file.write(responses[-1]+ "\n")
    if (prompt == "Quit"):
        break
    else:
        continue
   
    
#I need to create a program that will be fore people who want to,
# book  a reservation at a restaurant.    
responses={}
active=True
while active:
    print(" Welcome to the Ballito!"+"\n")
    date=input("Please choose your reservation date!\n")
    d=str(int(date))+" " +"April 2024"
    guests=input("How many guests are you expecting?\n")
    g="Number of guests:" + str(int(guests))
    responses[d]=g
    continuation=input("Do you have any special requests? (yes/no)\n")
    if (continuation == "yes"):
        extra=input(" Please enter your special requests:\n")
        #Stores special requests with the date as the key
        responses[d]=(g,extra)
    elif continuation == "no":
        pass #this when we do not want any action to take place here.
    with open("Reservation.txt","a") as file:
     for date,details in responses.items():
         file.write(f"{date} :{details}\n")   
    repeat=input("Would you like to make another reservation? (yes/no)\n")
    if (repeat == "no"):
        print("Thank you for booking with us, see you on the"+ " "+ d +"\n")
        break
    elif  repeat == "yes":
       pass
 



print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
 first_number = input("\nFirst number: ")
 if first_number == 'q':
     break
 second_number = input("Second number: ")
 if second_number == 'q':
     break
answer = int(first_number) / int(second_number)
print(answer)






























































































































































































