# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:57:49 2024

@author: mcinga
Software Engineering course lesson 1
"""

hw = "hello world"
print(hw)
print("This is my world" + " "+hw.title())

ab ="Isn\'t" # we use the back slash which is now an escape, so that it can recognise that  
print(ab)

#Indexing
id = hw[1:6]+hw[-2:0]
print(id)

a ="Well"*3
print(a)
b = "I'm"+" "+"in love with bagels"
print(b)
c = "I'm out"[0:3]+" "+ "in"
print(c)

tooManySpaces ="Spaceman"*2
tooManySpaces=tooManySpaces[0:-1]
print(tooManySpaces)

name="Ben"
age= 24
print(f"His name is {name} and he is {age} old")

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


number_list = []
active = True

with open("numbers.txt", "w") as file:  # Open in write mode
    while active:
        try:
            one = int(input("Enter the first number:\n"))
        except ValueError:
            print("That is not a valid number. Please enter a valid number.")
            continue

        number_list.append(one)

        try:
            two = int(input("Enter the second number:\n"))
        except ValueError:
            print("That is not a valid number. Please enter a valid number.")
            continue

        number_list.append(two)

        print("The sum is :", one + two)
        file.write(str(one) + " + " + str(two) + " = " + str(one + two) + "\n")  # Write to file

        repeat = input("Would you like to add another number? (yes/no)\n")
        if repeat.lower() == "yes":
            continue
        elif repeat.lower() == "no":
            break

def read_fasta_file(filename):
       with open("fasta_file.fas","r") as file:
           done_sequence=[]
           sequence=" "
           for line in file:
               line=line.strip()
               if line.startswith(">"):
                   if sequence:
                       done_sequence.append(sequence)
                       sequence=" "
                   else:
                       sequence+=line
           if sequence:
               done_sequence.append(sequence)
return done_sequence

#==============================================================================
"""
Working with two files    
"""  

#with open("numbers_1.txt","w") as f1, open("numbers_2.txt","w") as f2:

    
number_list = []
active = True

while active:
    try:
        one = int(input("Enter the first number:\n"))
    except ValueError:
        print("That is not a valid number. Please enter a valid number.")
        continue

    number_list.append(one)

    try:
        two = int(input("Enter the second number:\n"))
    except ValueError:
        print("That is not a valid number. Please enter a valid number.")
        continue

    number_list.append(two)

    print("The sum is :", one + two)

    # Write to numbers_1.txt
    with open("numbers_1.txt", "w") as f1:
        f1.write(str(one) + " + " + str(two) + " = " + str(one + two) + "\n")

    # Write to numbers_2.txt
    with open("numbers_2.txt", "w") as f2:
        f2.write(str(one) + " (list) = " + str(number_list) + "\n")  # Write list to numbers_2.txt

    repeat = input("Would you like to add another number? (yes/no)\n")
    if repeat.lower() == "yes":
        continue
    elif repeat.lower() == "no":
        break
    
    
ab=open("dog.txt", "w")
ab.write("ayakha is strong")
ab.close()


count =0
while True:
    
    while True:
        count+=1
        if count %2 ==0:
            continue
        print(count)
        if count>=19:
            break
        print("ended loop")



for i in range(20):
    if i % 2 ==0:
        continue
    print(i)

for i in range(5):
    if i ==3:
        continue
    print(i)
    
x =0
while x<4:
    x+=1
    print(x)
    break


















