# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:04:14 2024

@author: mcing
"""

f = open("test_filr.txt","a")
f.write("\nThis is another line\n")
f.close()
"""
w means we want to write someting into the file.
a means that we want to append something at the end of the file.
"""
#This will work when we want to read the file
f =open("test_filr.txt","r")
file_line=f.readline
print(file_line)
f.close()

#How to open a fasta file for reading
def read_fasta_new_way(filename):
    file_name=open("fasta_file_prac.fasta","r")
    done_sequences=[]
    sequences=""
    file=file_name.readlines()
    file=file_name.strip()   
    for line in file:
        if line.startswith(">"):
            if sequences:
                done_sequences.append(sequences)
                sequences=""
            else:
                sequences+=line
        if sequences:
            done_sequences.append(sequences)
    file_name.close()

#Another alternative is:
file_name=open("fasta_dile.fasta","r")
done_sequences=[]
sequences=""
for line in file_name.readlines():
    if line.startswith(">"):
        if sequences:
            done_sequences.append(sequences)
            sequences=""
        else:
            sequences+=line
    if sequences:
        done_sequences.append(sequences)
file_name.close()

#Using the with statement:
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

            
               
    