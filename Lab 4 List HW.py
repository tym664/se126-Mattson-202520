#Tyler Mattson 
#Lab 4 Parallel List Processing & Creating/Writing to Files
#Section: SE126 - 202502 (Morning Class) 
#Date: Febuary 3rd 2025


#VARIABLE DICTIONARY
#===============================

#===============================


#Importing CSV libary
import csv

#Empty lists
firstName = []
lastName = []
age = []
screenName = []
houseAlligence = [] 

#Opening CSV file
with open("text files/got_emails.csv") as csvfile:

    file = csv.reader(csvfile)
    for record in file: 
        firstName.append (record[0])
        lastName.append (record[1])
        age.append (record[2])
        screenName.append (record[3])
        houseAlligence.append (record[4])
        

#Headers for data placement
print()
print(f"{'FIRST':8} {'LAST':>12} {'AGE':>18} {'SCREEN-NAME':>20} {'HOUSE':>14} {'EMAIL':>14} {'DEPO':>14} {'EXT':>14}")
print("=" *130)
        

    
for i in range(0, len (firstName)):
    
    
    print(f"{firstName[i]:15} {lastName[i]:20} {age[i]:15} {screenName[i]:8} {houseAlligence[i]:>25}")

found = "x"
search = input("Who would you like to find?:") 

for i in range(0, len (firstName)): 
    if search.lower() in firstName[i].lower(): 
        found = i 
    
if found != "x":
    print (f"Your search for {search} was found. ")
    print(f"{firstName[found]:15} {lastName[found]:20} {age[found]:15} {screenName[found]:8} {houseAlligence[found]:>25}")

else: 
    print(f"Your search for {search} was not found.")


found = [] 
search = input("Who would you like to find?:") 

    

        



    
    