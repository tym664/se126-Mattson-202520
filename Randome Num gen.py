#Description:
#This program just generates random numbers
#After the random numbers are generated, the program adds the numbers to a CSV file
#=======================================================================================================================================

import random #imports the random library into python 
import csv#Imports CSV library into python 
#=======================================================================================================================================
def randNum():#Function for generating random numbers with CSV file writer included
    lower = int(input("Enter the lower number: "))#User inputs lower number
    upper = int(input("Enter the highest nubmer: "))#User inputs the highest number 
    randNumber = random.randint(lower, upper)
    print(f"The random number between {lower} and {upper} is: {randNumber}") 
    with open('randomNumbers.csv', mode='a', newline='') as file:#Opens a CSV file 
        writer = csv.writer(file)#Writes to CSV file 
        writer.writerow([randNumber])#Writes data to CSV file 
#=======================================================================================================================================
#Loop to allow user to continue inputting numbers into the program 
contiuneProgram = "y"
while contiuneProgram == "y":
    randNum()#Call back to the function to put user in loop 
    contiuneProgram = input("Do you wish to find another number? (y/n)")
print("Thank you for using program")