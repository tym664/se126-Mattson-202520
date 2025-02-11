#Tyler Mattson 
#Lab 4 Parallel List Processing & Creating/Writing to Files
#Section: SE126 - 202502 (Morning Class) 
#Date: Febuary 3rd 2025

#VARIABLE DICTIONARY
#===============================================================================
#firstName = Employees first name
#lastName = Employees last name 
#emails = Employees emails 
#department = Which department each employee works at 
#phoneExt = Employees unique phone extension 
#screenName = Employees screen names for their emails 
#depNum = Variable assigned to each employee to give them their phone extensions 
#totalRecords = How many records were processed in the file 
#totalStark = Total number of employees within House Stark 
#totalTarg = Total number of employees within House Targaryen 
#totalTully = Total number of employees within House Tully
#totalLann = Total number of employees within House Lannister
#totalBara = Total number of employees within House Baratheon
#otalNight = Total number of employees within The Night’s Watch
#===============================================================================

#Importing CSV libary
import csv

#Empty lists
firstName = []
lastName = []
emails = []
department = []
phoneExt = [] 
screenName = [] 
depNum = 0
totalRecords = 0
totalStark = 0 
totalTarg = 0 
totalTully = 0 
totalLann = 0 
totalBara = 0 
totalNight = 0 

#Opening CSV file
with open("text files/got_emails.csv") as csvfile:
    

    file = csv.reader(csvfile)
    
    for record in file: 

        totalRecords += 1 #Keeps track of each record being processed, adds total when new file is created 

        firstName.append (record[0])
        lastName.append (record[1])
        screenName.append (record[3])
        emails.append (str(record[3] + "@westeros.net")) #adds emails extension to employees screen names

#Conditional statements to determine which house is connected to which department 
        if (record[4]) == 'House Stark': 
            department.append ('Research & Development')
            phoneExt.append (int(100+depNum)) #Creates unique phone extension for each employee 
            totalStark += 1 

        elif (record[4]) == 'House Targaryen': 
            department.append ('Marketing') #Determines which department each employee belongs too 
            phoneExt.append (int(200+depNum)) 
            totalTarg += 1  #Each variable keeps track of their respective house, adds total number of employees of each house in new file 
            
        elif (record[4]) == 'House Tully':
            department.append ('Human Resources') 
            phoneExt.append (int(300+depNum))
            totalTully += 1 
            
        elif (record[4]) == 'House Lannister':
            department.append ('Accounting') 
            phoneExt.append (int(400+depNum))
            totalLann += 1 
            
        elif (record[4]) == 'House Baratheon':
            department.append ('Sales') 
            phoneExt.append (int(500+depNum))
            totalBara += 1  
             
        else: 
            (record[4]) == 'The Night’s Watch'
            department.append ('Auditing') 
            phoneExt.append (int(600+depNum))
            totalNight += 1  
             
        depNum += 1  #depNum is to randomly assign each employee with a number for their phone extension 
       
#Headers for data placement
print()
print ("\t\t\t\t\tEmployee data")

print("=" * 130)
print(f"{'FIRST':8} {'LAST':>11} {'EMAIL':>23} {'DEPARTMENT':>37} {'PhoneEXT':>25}") #Header 
print("-" * 130)
    
for i in range(0, len (firstName)):

    print(f"{firstName[i]:15} {lastName[i]:15} {emails[i]:35} {department[i]:25}  {phoneExt[i]:10}")

print("=" * 130)
print()

#CREATING FILE ====================================================================================================================================================

file = open('text files/Westeros.csv', 'w') #Creates new file 

for i in range(0, len (firstName)): 

    file.write(f"{firstName[i]}, {lastName[i]}, {emails[i]},  {department[i]}, {phoneExt[i]}\n") #Writes lists to new file 

#Data formatting within the created csv file 
file.write ("="*80)    
file.write (f"\n\t\t\tTotal Number of employees: {totalRecords}") 
file.write (f"\n\t\t\tTotal Number of employees in House Stark: {totalStark}") 
file.write (f"\n\t\t\tTotal Number of employees in House Targaryen: {totalTarg}") 
file.write (f"\n\t\t\tTotal Number of employees in House Tully: {totalTully}") 
file.write (f"\n\t\t\tTotal Number of employees in House Lannister: {totalLann}") 
file.write (f"\n\t\t\tTotal Number of employees in House Baratheon: {totalBara}") 
file.write (f"\n\t\t\tTotal Number of employees in The Nights Watch: {totalNight}") 
file.write ("\n================================================================================")

file.close()  #Closes file 

print ("\t\t**User has created file. Check for file name 'Westeros.csv' for employee information**") #Alerting the user they created a new file
print()
print ("\t\t\t\t\tProgram is finised.")
print()
print("-" * 130)  
print()