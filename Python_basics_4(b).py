# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:42:55 2024

@author: mcing
Continuation of dictionaries

NESTED DICTIONARY
"""
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username, user_info in users.items():
 full_name = user_info['first'] + " " + user_info['last']
 location = user_info['location']
 print("\nUsername: " + username)
 print("\tFull name: " + full_name.title())
 print("\tLocation: " + location.title())
 
#Exercise
 
people = [{'josy':'bioinformatician'},
        {'amy':'epidemiologist'},
        {'penny':'geneticist'}]

for i in people:
    for name, job in i.items():
        print("\nHi my name is"+ " "+name.title()+ " "+ "and I am a"+" "+ job) 
    
#Print the name of eache city and its information all at once.
city={'east london':
        {'province':'eastern cape','population': 250000},
    'cape town':{
        'province':'western cape',
        'population':1000000},
    'pretoria':{
        'province':'gauteng',
        'population':1500000}}   

for cities,facts in city.items():
    province=facts['province']
    populaton=facts['population']
    print("\nCity:"+ cities.title())
    print("\t" + province.title())
    print("\t" + str(populaton))

 