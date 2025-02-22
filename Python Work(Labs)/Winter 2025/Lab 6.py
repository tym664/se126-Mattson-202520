#Tyler Mattson 
#Lab 5 Collection & Logic 
#Section: SE126 - 202502 (Morning Class) 
#Date: Febuary 22th 2025

#VARIABLE DICTIONARY
#===============================================================================

#===============================================================================

#DESCRIPTION
#===============================================================================================================================================

#===============================================================================================================================================

import csv 

section = [] 
firstRow = [] 
secondRow = []
thirdRow = [] 
fourthRow = [] 

with open("text files/airplane_seats.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for record in file: 

        section.append (record[0])
        firstRow.append (record[1])
        secondRow.append (record[2])
        thirdRow.append (record[3])
        fourthRow.append (record[4])
        
    for i in range(0,len(section)): 

        print()
        print(f"{section[i]:8}  {firstRow[i]:15} {secondRow[i]:20}  {thirdRow[i]:20}  {fourthRow[i]:10}")
    print ("=" * 115)
    print()