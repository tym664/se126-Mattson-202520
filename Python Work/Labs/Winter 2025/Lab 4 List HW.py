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
emails = []
department = []
phoneExt = [] 
screenName = [] 



#Opening CSV file
with open("text files/got_emails.csv") as csvfile:
    

    file = csv.reader(csvfile)
    
    for record in file: 

        email = (f"{screenName}@westeros.net")
        firstName.append (record[0])
        lastName.append (record[1])
        emails.append (str(record[2])) 
        phoneExt.append (record[4]) 
        department.append (record[3])
        if record [3] == 'HOUSE STARK': 
            department.append ("Research & Development")
            phoneExt.append (int('100,199'))
        elif record [3] == 'House Taragaryen':
            department.append ("Marketing")



       
#Headers for data placement
print()
print(f"{'FIRST':8} {'LAST':>12} {'DEPARTMENT':>18} {'EMAIL':>20} {'EXT':>14}")
print("=" *130)
        

    
for i in range(0, len (firstName)):
    
    
    print(f"{firstName[i]:15} {lastName[i]:20} {department[i]:15} {emails[i]:8}") 

found = "x"
search = input("Who would you like to find?:") 

for i in range(0, len (firstName)): 
    if search.lower() in firstName[i].lower(): 
        found = i 
    
if found != "x":
    print (f"Your search for {search} was found. ")
    print(f"{firstName[found]:15} {lastName[found]:20}{department[found]:>25}")

else: 
    print(f"Your search for {search} was not found.")


found = [] 
search = input("Who would you like to find?:") 

file = open('text files/Westeros.csv', 'w')

for i in range(0, len (firstName)): 

    file.write(f"{firstName[i]}, {department[i]}\n")

file.close() 

    

        



    
    