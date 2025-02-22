#Tyler Mattson 
#Lab 6 Collection & Logic 
#Section: SE126 - 202502 (Morning Class) 
#Date: Febuary 22th 2025

#VARIABLE DICTIONARY
#======================================================================================================
#section = The section number of the seat 
#firstRow = first row (A)
#secondRow = second row (B)
#thirdRow = third row (C)
#fourthRow = fourth row (D)
#seatDisplay = Function that creates a display of available seats 
#userContinue = Function that prompts the user if they want to contiune after making a seat selection
#seatReserve = Function that asks the user which seat they would like to reserve 
#seatLetter = variable assined to a letter (A, B , C or D)
#row = variable assinged to a number (1, 2, 3, 4, 5, 6, 7,)
#choice = user input ('y', or 'n')
#======================================================================================================

#DESCRIPTION
#=================================================================================================================================================
#This program allows the user to make a selection of which seats they would like to reserve on an airplane
#This program uses functions to handle user input as well as to create and re-create the seat layout before and after the user makes a selection
#This program uses various error checks to ensure the user is inputting the correct data into the program
#This program pulls data from a pre-created CSV file 
#=================================================================================================================================================

import csv 

#Empty lists for storing data 
section = [] 
firstRow = [] 
secondRow = []
thirdRow = [] 
fourthRow = [] 

with open("text files/airplane_seats.csv") as csvfile: #Opening CSV file 

    file = csv.reader(csvfile)
    
    for record in file: 

        section.append (record[0]) #Adds data to empty lists in accordance to CSV file 
        firstRow.append (record[1])
        secondRow.append (record[2])
        thirdRow.append (record[3])
        fourthRow.append (record[4])
        
    print ("=" * 80)
    print()

def seatDisplay(): #This function creates a display for the user to see 
    print()
    print ("\t\t\tWelcome to Tyler Air")
    print()
    print ("=" * 80)
    print()
    print(f"{'Row A':>23}  {'Row B':>15}  {'Row C':>14}  {'Row D':>15}")
    print()
    print ("=" * 80)

    for i in range(0, len(section)): 

        print(f"{section[i]:15} {firstRow[i]:15} {secondRow[i]:15} {thirdRow[i]:15} {fourthRow[i]:15}")

    print ("=" * 80)
    print()

def userContinue(): # This function asks the user if they want to contiune reserving seats 
    print()
    choice = input("\t\t\t\tDo you wish to contiune?").lower()
    print()
    if choice == 'y': #User choice 
        return 'y'
    elif choice == 'n': #User choice 
        return 'n'
    else: 
        print()
        print("\t\t\t\tINVALID INPUT") 
        #Error check to make sure program gets correct data from user 
        #Forces user to enter either 'y' or 'n'

        print()
        return userContinue() #Sends program back to start of function until user inputs correct data ( 'y' or 'n' )

def seatReserve(): #This function asks what seat the users whats to reserve 
    print()
    seat = input("\t\tEnter the seat you want to reserve (Ex. 1A, 2B etc..)").upper()
    print()

    if len(seat) <2: #Checks amount of characters of user input 
        print("\t\t\t\tINVALID INPUT")
        return seatReserve() #Returns user to prompt after incorrect data was input 
    
    row, seatLetter = seat[0], seat[1] #This assigns values from input into two seperate variables: row and seatLetter

    if not row.isdigit(): #isdigit checks if input consits solely of numbers 

        print("\t\t\t\tINVALID INPUT.")
       

    row = int(row) #Converts row into integer for processing 
        
    if row < 1 or row > 7 or seatLetter not in ['A' , 'B' , 'C' , 'D']: 
        print ("INVALID INPUT") #Error check to make sure program gets correct data from user 
        #Makes sure user enters correct number and letter into program 
        return 'invaild' #Prints invalid to notifiy the user that their input was not accepted 
    
 #Conditional statements that check if the seat is already taken 
 #If seat is taken, the list will be updated with an X in place of whatever the user chose 
    if seatLetter == 'A' and firstRow[row - 1] == 'X': 
        print (f"\t\tSeat {seat} is already taken. Please choice another seat. ")
        return 'taken' #Prints taken to notify the user that the seat they entered was taken

    elif seatLetter == 'B' and secondRow[row - 1] == 'X': 
        print (f"\t\tSeat {seat} is already taken. Please choice another seat. ")
        return 'taken'

    elif seatLetter == 'C' and thirdRow[row - 1] == 'X': 
        print (f"\t\tSeat {seat} is already taken. Please choice another seat. ")
        return 'taken'

    elif seatLetter == 'D' and fourthRow[row - 1] == 'X': 
        print (f"\t\tSeat {seat} is already taken. Please choice another seat. ")
        return 'taken'
    
#Conditonal statements that allow the user to reserve a free seat 
#If the seat is taken, the program will prompt the user that seat is already reserved 
    if seatLetter == 'A': #Checks if variable is equal to the letter 
        firstRow[row - 1] = 'X' #Indexing starts at zero, subtract one to set properly
        print()
        print("\t\t\t**Seat was reserved successfully**")
        print()
        #row 1
    elif seatLetter == 'B': 
        secondRow[row - 1] = 'X'
        print()
        print("\t\t\t**Seat was reserved successfully**") #Print statements that show confirmation to the user 
        print()
        #row 2
    elif seatLetter == 'C': 
        thirdRow[row - 1] = 'X'
        print()
        print("\t\t\t**Seat was reserved successfully**")
        print()
        #row 3
    elif seatLetter == 'D': 
        fourthRow[row - 1] = 'X'
        print()
        print("\t\t\t**Seat was reserved successfully**")
        print()
        #row 4
    return 'reserved' 

#Function call that creates display for user 
seatDisplay()

reserveCont = 'y' 

#User loop that allows user to keep entering data 
while reserveCont == 'y': 
    reservedSeat = 'taken' 

    while reservedSeat == 'taken': 
        reservedSeat = seatReserve()

    seatDisplay() #Function call that updates the display with user inputs added

    reserveCont = userContinue() #Function call that allows user to continously loop program