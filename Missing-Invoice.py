#!/usr/bin/env python


import random
import os
from os import sys


#List all files from directory
#test directory: /Users/fabiogos/Desktop/projects/Missing-Invoice/Invoices-test

direc =  raw_input('Type directory where invoices are located: ')
files = os.listdir(direc)

#Sometimes a hidden file is created and messes up the script, remove this stupid hidden file
if '.DS_Store' in files:
    files.remove('.DS_Store')

#list that will contain only the invoice numbers
numbers=[]

#Picks each relevant character of each invoice and append to list number
for invoice in files:
    first_number=str(invoice[8])
    second_number=str(invoice[9])
    third_number=str(invoice[10])
    fourth_number=str(invoice[11])
    fifth_number=str(invoice[12])
    sixth_number=str(invoice[13])
    seventh_number=str(invoice[14])
    invoice_number=(first_number+second_number+third_number+fourth_number+fifth_number+sixth_number+seventh_number)
    numbers.append(invoice_number)

#transforms numbers into a dictionary to remove duplicates and then makes it a list again (disctionaries cannot have duplicates and are dropped automatically)
numbers = list(dict.fromkeys(numbers))

#sorting list that contain all invoice numbers
numbers.sort()


i=0
missing_numbers=[]

#Loop to find missing numbers inside list numbers
for number in numbers:
    #breaks if last element of loop
    if number==numbers[-1]:
        break
    #find if there's a missing invoice and qty of sequential missing invoices
    gap=int(numbers[i+1])-int(numbers[i])
    if gap>1:
        #j is used to calculate the qty of sequential missing invoices
        j=1-gap
        for x in range(0,gap-1):
            missing_number=int(numbers[i])-j
            missing_numbers.append(missing_number)
            j+=1
    i+=1


missing_numbers.sort()
print (missing_numbers)

