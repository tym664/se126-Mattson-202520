#Tyler Mattson 
#Lab 7 Dictionaries
#Section: SE126 - 202502 (Morning Class) 
#Date: March 3rd 2025

#VARIABLE DICTIONARY
#======================================================================================================
#loadDictonary() = Function method to load the CSV file 
#filename = The name of the CSV file 
#word = The word in the dictionary CSV file 
#definition = The defintion of the word in the dictionary CSV file 
#dictionary = Variable assigned to the dictionary
#showWords() = Function method to show the words/defintions in the dictionary CSV file 
#addWord() = Function method to add a word to the dictionary 
#searchWord ()= Function method that allows user to search for a word in the ditctionary CSV file 
#choice = User loop. Allows user to either exit or contiune using the program 
#exProgram() = Function method that handles exiting the program 
#menu() = Function method that display the menu choices (1-4) 
#======================================================================================================

#DESCRIPTION
#=================================================================================================================================================
#This program imports a pre-made dictionary from a CSV file 
#The program consists of functions that handle data. Importing the CSV file, displaying search menu, 
#adding a word/defintion, searching for a word, exiting the program, and displaying the file to the user. 
#The user can chose to either Show the dictionary, Search for a key word, Add a word, or exit the program
#=================================================================================================================================================

import csv 

def loadDictonary(filename): #filename represents the path of the file being imported 
    dictionary = {} #creates empty dictionary
    with open(filename) as csvfile: #Opening CSV file 
        file = csv.reader(csvfile)
        for rec in file: 
            word = rec[0] #Defining record 0 
            definition = rec[1] #Definting record 1 
            dictionary[word] = definition #Updates dictionary by assigning definition to the 'word' key 
    return dictionary #Returns the value of the dictionary variable from function 

#Function for menu 
def menu(): 
    print("My programming Dictionary Menu")
    print("=" * 50)
    print("1. Show all words")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. EXIT")
    print("=" * 50)

#Function to handle user input for choice 1 
def showWords(dictionary): #Show dict 
    if dictionary: 
        print("\t\tWords in Dictionary")
        print("=" * 50)
        print(f"{'Word' :<20} {'Definition' :<30}") #Displays headers 
        print("=" * 180)
        for key in dictionary: 
            print(f"\n{key.capitalize() :<15}: {dictionary[key] :<30}") #capitalize() capitalizes the first letter of the word stored in key 
        print("=" * 180)
    else: 
        print("That word cannot be found") #Error check 

#Function for handling input choice 2 
def addWord(dictionary): #Add word to dict 
    print()
    word = input("Enter the word to add to dictionary:").strip().lower() #.strip().lower() is used so the user can enter a capital or lowercase 
    print()
    if word in dictionary: 
        print()
        print(f"The word '{word}' already exists")
    else: 
        definition = input(f"Enter the definition for '{word}': ")
        print()
        dictionary[word] = definition #Updates dictionary by assigning definition to the 'word' key 
        print()
        print (f" The word '{word}' has been added to the dicionary.")
        print()

#Function to handle input for choice 3 
def searchWord(dictionary): #Search for word in dict
    word = input("Enter the word to search:").strip().lower() #.strip().lower() is used so the user can enter a capital or lowercase 
    if word in dictionary: 
        print()
        print(f"{'Word' :<20} {'Definition' :<20}")
        print("=" * 180)
        print(f"{word.capitalize():<20}: {dictionary[word]:<30}") #capitalize() capitalizes the first letter of the word stored in key 
        print("=" * 180)
        print()
        #capitalize capitalizes the word in the print statement 
    else: 
        print("The word cannot be found") #Error check 

#Function to handle input for choice 4
def exProgram(): #Exit the program 
    print ("Exiting the program") 

#Function calls 
filename = "text files/words.csv" #Call for filename 
menu() #Call for display menu 
dictionary = loadDictonary(filename) #Calling function (loadDictonary) , passing data to variable (filename)

#LUser loop 
choice = '' #Definies choice as a vairable 

while choice != '4': #Loops user in program until they choose option 4 to exit program 
 
    choice = input("Please select an option (1-4):") #User choice 
    print()

#Conditional statements to display data requested from user 
    if choice == "1": 
        showWords(dictionary)#Function call to show dict 

    elif choice == "2": 
        searchWord(dictionary)#Funcrion call search dict 

    elif choice == "3": 
        addWord(dictionary)#Function call to add a word and definition to dict 

    elif choice == "4": 
            exProgram()#Funtion call to exit program 
    else: 
     print("Invalid choice") #Error check 