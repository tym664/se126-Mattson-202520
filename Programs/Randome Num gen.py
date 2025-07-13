#Description:
#This program generates random numbers
#The user inputs lowest number and hightest number of their choice, then the program generates a random number betwee the two given numbers
#After the random numbers are generated, the program adds the numbers to a CSV file
#The program will keep adding numbers to CSV file, if CSV file is deleted a new one will be created, but numbers will not be saved
#=======================================================================================================================================
import random #imports the random library into python, allowing the program to generate random numbers 
import csv#Imports CSV library into python 
import os #Imports the users Operating System for screen clearing function to work properly 
#=======================================================================================================================================
print("Welcome to NumGen, the random number generator")#Title, welcoming the user to NumGen program 
print("-" *40)#Formatting 
def randNum():#Function for generating random numbers with CSV file writer included
    lower = int(input("Enter the lower number: "))#User inputs lower number
    print("-" *40)#Formatting 
    print()#Formatting 
    upper = int(input("Enter the highest nubmer: "))#User inputs the highest number 
    print("=" *40)#Formatting
    print()#Formatting 
    randNumber = random.randint(lower, upper)
    print(f"The random number between {lower} and {upper} is: {randNumber}") 
    print("=-=" *16)#Formatting 
    print()#Formatting 
#=======================================================================================================================================
    with open('NumGen_data.csv', mode='a', newline='') as file:#Opens a CSV file 
        writer = csv.writer(file)#Writes to CSV file 
        writer.writerow([randNumber])#Writes data to CSV file 
#=======================================================================================================================================
def screenClear(): #This function clears the screen for the user if the user wants to contiune, used to make display cleaner
    os.system('cls' if os.name == 'nt' else 'clear') #This is to handle different operating systems terminals (Windows/Mac) program checks operating system to apply proper clear function to terminal 
#=======================================================================================================================================
#Loop to allow user to continue inputting numbers into the program 
contiuneProgram = "y"
while contiuneProgram == "y":
    randNum()#Call back to the function to put user in loop 
    contiuneProgram = input("Do you wish to find another number? (y/n)")#Asking the user if they wish to contiune using the program 
    screenClear()#Calls the screen clearing function to clear the screen for the user 
#=======================================================================================================================================
print("-"*40)#Formatting     
print("Thank you for using NumGen")#End statement, indicating the program has ended 
print("Please check created file for numbers.")#End statement, indicating the program has ended 
print("-"*40)#Formatting 
print()#Formatting

