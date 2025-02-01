#Tyler Mattson 
#Lab 3, Program that will analyze potential voters
#Section: SE126 - 202502 (Morning Class) 
#Date: January 27 2024 
#=================================================

#VARIABLE DICTIONARY

#===============================================================
#notEligi = Not eligible to vote, under 18 
#age = Age of voter
#Voted = If person voted
#eligi_didnt_vote = Eligible to vote but did not vote
#totalRecords = Total amount of records processed in the program
#registered = # of people who are registered
#votedStatus =  If the person voted or not
#idNum = Numerical ID for person in data file 
#===============================================================

#BASE PROGRAM CODE

#Importing CSV libary 
import csv

notEligi = 0
age = 0
not_reg_old_enough = 0
voted = 0
eligi_didnt_vote = 0
totalRecords = 0
idNum = 0

#Opening CSV file 
with open("voter_info.csv") as csvfile:

#Headers for labeling data
    file = csv.reader(csvfile)
    print()
    print("\t\t\t\tVoter information:")
    print("=" *80)
    print()
    print(f"{'ID Number':<15} {'Age':<10} {'Registered to vote':>10} {'Old enough to vote':>25}")
    print()
    print("=" * 80) 
    
#For loop to process data in file
    
    for record in file:
        
#Defining where the variables are in the file 
        
        totalRecords += 1
        idNum = record [0]
        age = (int(record[1]))
        registered = (record[2]) == 'Y'
        
#Conditional statements to determine if the if the person is registered to vote or not, old enough to vote 
        if registered == 1:
            registered = 'Y'
        else:
            registered = 'N'
    
        votedStatus = record[3] == 'Y'
        if votedStatus == 1:
            votedStatus = 'Y'
        else:
            votedStatus = 'N'
        
#Conditional statements to determine data within file, data that is printed below the list  

        if age < 18:
            
            notEligi += 1 #Not eligible to vote, under 18 years old 
        else:
            if not registered:
                not_reg_old_enough += 1 # Old enough to vote, but not registered to vote 
            else:
                if votedStatus:
                    voted += 1 # Registered to vote, voted 
                else:
                    
                    eligi_didnt_vote += 1 #Registered to vote, but did not vote
                    
                    
        #Printing data from file in list form and formatting the data being displayed 
                    
        print(f"{idNum:15} {age:<10} {registered:>12} {votedStatus:>20}")

                    
#Print statements for data below the list, and formatting the data 
                    
print ("=" * 80)
print()
print(f"\t\tNumber of individuals not eligible to register: {notEligi}")
print()
print(f"\t\tNumber of individuals old enough to vote but not registered: {not_reg_old_enough}")
print()
print(f"\t\tNumber of individuals eligible to vote but did not vote: {eligi_didnt_vote}")
print()
print(f"\t\tNumber of individuals who did vote: {voted}")
print()
print("=" * 80)
print()
print(f"\t\t\tTotal number of records processed: {totalRecords}")
print()
print("=" * 80)
print("=" * 80)
print()
print("\t\t\t\tProgram completed")
print()
