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
#The program consists of functions that handle data. The program imports the CSV file, displays a search menu, 
#allows the user to add a word/defintion, search for a word, exit the program, and displaying the dictionary file to the user. 
#The user can add any word they choose, as well as a definiton tied to that word of choice. Once the word has been added, the user will be able 
#to show the dictionary file again with their added word and definition. The program will not save user added content after the program is exited.
#The program does not display an alphabetized list of the words from the dictionary.  
#=================================================================================================================================================

import csv 

#Recursion Function (W9D1)
def loadDictonary(filename): #filename represents the path of the file being imported 
    dictionary = {} #creates empty dictionary 
    with open(filename) as csvfile: #Opening CSV file 
        file = csv.reader(csvfile)#Defining CSV file 
        for rec in file: 
            word = rec[0] #Defining record 0 
            definition = rec[1] #Definting record 1 
            dictionary[word] = definition #Updates dictionary by assigning definition to the 'word' key 
    return dictionary #Returns the value of the dictionary variable from function, makes this function recursion function

#Function for menu 
def menu(): #Shows menu (1-4) 
    print("My programming Dictionary Menu")
    print("=" * 50)#Formatting
    print("1. Show all words")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. EXIT")
    print("=" * 50)#Formatting

#Function to handle user input for choice 1 
def showWords(dictionary): #Show dict 
    if dictionary: 
        print("\t\tWords in Dictionary")
        print("=" * 50)#Formatting
        print(f"{'Word' :<20} {'Definition' :<30}") #Displays headers 
        print("=" * 180)#Formatting
        for key in dictionary: 
            print(f"\n{key.capitalize() :<15}: {dictionary[key] :<30}") #capitalize() capitalizes the first letter of the word stored in key, prints the words with the first letter capitalized
        print("=" * 180)#Formatting
    else: 
        print("That word cannot be found") #Error check 

#Function for handling input choice 2 
def addWord(dictionary): #Add word to dict 
    print()#Empty space for formatting 
    word = input("Enter the word to add to dictionary:").strip().lower() #.strip().lower() is used so the user can enter a capital or lowercase 
    print()#Empty space for formatting 
    if word in dictionary: #if statnment that checks if word is in dictionary
        print()#Empty space for formatting 
        print(f"The word '{word}' already exists")#Allows user to know if word entered already exists in the dictionary 

    else: #else statement that moves the programn along if the word is not in the dictionary 
        definition = input(f"Enter the definition for '{word}': ")#Allows user to enter the definition of the word the user entered in the dictionary 
        print()#Empty space for formatting 
        dictionary[word] = definition #Updates dictionary by assigning definition to the 'word' key 
        print()#Empty space for formatting 
        print (f" The word '{word}' has been added to the dicionary.")#Confirmation for the user that the word has been entered into the dictionary
        print()#Empty space for formatting 

#Function to handle input for choice 3 
def searchWord(dictionary): #Search for word in dict
    word = input("Enter the word to search:").strip().lower() #.strip().lower() is used so the user can enter a capital or lowercase 
    if word in dictionary: #if statment that checks if the word is in the dictionary 
        print()#Empty space for formatting 
        print(f"{'Word' :<20} {'Definition' :<20}")#Formatting 
        print("=" * 180)#Formatting
        print(f"{word.capitalize():<20}: {dictionary[word]:<30}") #capitalize() capitalizes the first letter of the word stored in key 
        print("=" * 180)#Formatting
        print()#Empty space for formatting 
        
    else: #If the word cannot be found in the dictionary, program will move to this else statment 
        print("The word cannot be found") #Error check 

#Function to handle input for choice 4
def exProgram(): #Exit the program 
    print ("\t\tExiting the program") 
    print()#Empty space for formatting 

#Function calls 
filename = "text files/words.csv" #Call for filename 
menu() #Call for display menu
dictionary = loadDictonary(filename) #Calling function (loadDictonary) , passing data to variable (filename)

#LUser loop 
choice = '' #Definies choice as an empty vairable 

while choice != '4': #Loops user in program until they choose option 4 to exit program. 4 works here because choice was defined as an empty variable 
 
    choice = input("Please select an option (1-4):") #User choice 
    print()#Empty space for formatting 

#Conditional statements to display data requested from user 
    if choice == "1": 
        showWords(dictionary)#Function call to show dict 

    elif choice == "2": 
        searchWord(dictionary)#Function call to search dict

    elif choice == "3": 
        addWord(dictionary)#Function call to add a word and definition to dict 

    elif choice == "4": 
            exProgram()#Funtion call to exit program 
    else: 
     print("Invalid choice") #Error check 