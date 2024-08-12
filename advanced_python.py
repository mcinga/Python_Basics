# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:06:36 2024

@author: mcing
#Advanced python scripts
"""

#Doing list comprehensions
numbers =[12,13,14]
doubled= [x *2 for x in numbers]
print(doubled)

n =[2,4,6]
d=[]
for i in n:
    d.append(i*2)
print(d)

"""
The syntax of:
    newlist=[ expression(element) for element in oldList if condition ]
    expression: Represents the operation you want to execute on every item within the iterable.
(1) Element: The term “variable” refers to each value taken from the iterable.
(2) Iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
(3) Condition: (Optional) A filter helps decide whether or not an element should be added to the new list. 
"""
no =[1,2,3,4,5]
sq = [x ** 2 for x in no]
print(sq)

"""
Iteratoin with list comprehension
"""
List =[character for character in [1,2,3]]
print(List)

list =[i for i in range(11) if i % 2 == 0]
print(list)


matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)


lb =[]
for i in 'Geek 4 geeks!':
    lb.append(i)
print(lb)

#======================================================



























