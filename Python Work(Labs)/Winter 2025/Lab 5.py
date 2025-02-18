#Tyler Mattson 
#Lab 5 Searching & Sorting 
#Section: SE126 - 202502 (Morning Class) 
#Date: Febuary 16th 2025

#VARIABLE DICTIONARY
#===============================================================================
#libraryNum = Library number for book 
#title = Title of the book 
#author = Author of the book 
#genre = Genre of the book 
#pgCount = How many pages each book has 
#status = Status of the book, if it is available, on loan
#foundList = List to store found values 
#bubbleSearch = Variable to call Bubble sort alogorithm
#swap = Used to switch vairables for bubble sort 
#binarySearch = Variable to call binary search algorithm
#sequentialSearch = Vairable to call sequential search algorithm
#searchType = Variable that user inputs to desired search 
#searchInput = Variable that user inputs for binary search 
#searchQuery = Varianle that user inputs for sequental search 
#ans = Users answer to enter or exit loop 
#===============================================================================

#Importing CSV libary to handle
import csv 


#Function

def display(x, foundList, records):
    print("\t\t\t\t\tWelcome to Book Finder")
    print()
    print(f"{'LIB #':8}  {'TITLE':37}  {'AUTHOR':18}  {'GENRE':19} {'Pg AMT':11} {'Loan Status':10}")

    print("=" * 115)
    if x != "x":
        
        print(f"{libraryNum[x]:8}  {title[x]:35}  {author[x]:20}  {genre[x]:20}  {pgCount[x]:10} {status[x]:10}")

    elif foundList:
        
        for i in range(0, records):
            print(f"{libraryNum[foundList[i]]:8}  {title[foundList[i]]:35} {author[foundList[i]]:20} {genre[foundList[i]]:20}  {pgCount[foundList[i]]:10} {status[foundList[i]]:10}") 
    
    else:

        for i in range(0, records):
            print(f"{libraryNum[i]:8}  {title[i]:35} {author[i]:20}  {genre[i]:20}  {pgCount[i]:10} {status[i]:10}")

    print("=" * 115)

#Function for switching variables (For bubble sort)

def swap (a, b):  
    libraryNum[a], libraryNum[b] = libraryNum[b], libraryNum[a]
    title[a], title[b] = title[b] , title[a]
    author[a], author[b] = author[b] , author[a]
    genre[a], genre[b] = genre[b], genre[a]
    pgCount[a], pgCount[b] = pgCount[b] , pgCount[a]
    status[a], status[b] = status[b] , status[a]

# Function for bubble sort algo 
def bubbleSearch():
    for a in range(len(libraryNum)):
        for b in range(0,len(libraryNum) - a - 1):
            if libraryNum[b] > libraryNum[b + 1]:
                swap (b, b + 1)
                

#Function for binary search algo 
def binarySearch(searchInput, foundList): 
    min = 0 
    max = len(libraryNum) - 1 
    foundList.clear()
    while min <= max:
        mid = (min + max) // 2 
        if libraryNum[mid] == searchInput: 
            foundList.append(mid)
            min = max + 1 
        elif libraryNum[mid] < searchInput: 
            min = mid + 1 
        else: 
            max = mid - 1 

#Function for sequential search algo 
def sequentialSearch(listSearch, searchQurey, foundList): 
    for i in range(len(listSearch)): 
        if searchQurey.lower() in listSearch[i].lower():
            foundList.append(i)


#Empty Lists for storing data 
libraryNum = [] 
title = [] 
author = [] 
genre = [] 
pgCount = [] 
status = []  

with open("text files/book_list.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for record in file: 

        libraryNum.append (record[0])
        title.append (record[1])
        author.append (record[2])
        genre.append (record[3])
        pgCount.append (record[4])
        status.append (record[5]) 

print()
print ("=" * 115)
print()

display ("x", [], len(libraryNum))

print()
ans = input("\t\t\t\tWould you like to enter the search program? [y/n]").lower()
print()

while ans != "y" and ans != "n": #This loop makes sure the user inputs the correct information into the program
    print("\t\t\t\t***INVALID ENTRY!***")
    print()
    ans = input("\t\t\t\tWould you like to enter the search program? [y/n]").lower() #loops user untill correct information is given to the program

if ans == "y": #Direct loop based on user input 

    searchType = " " 

    while searchType != "7":
        print()
        print("\t\t\t\t\t****Personal Library Menu****")
        print() 
        print("\t\t\t\t\t1. Search by TITLE")
        print("\t\t\t\t\t2. Search by AUTHOR") 
        print("\t\t\t\t\t3. Search by GENRE") 
        print("\t\t\t\t\t4. Search by LIBRARY NUMBER")
        print("\t\t\t\t\t5. Search by AVAILABLE")
        print("\t\t\t\t\t6. Search by ON LOAN")
        print("\t\t\t\t\t7. EXIT")
        print()
        print ("=" * 115 )

        searchType =  input("\t\t\t\tHow would you like to search? [1-7]: ") 
        print()

        foundList = [] #Empty list to store found data 

        if searchType not in ["1", "2", "3", "4", "5", "6", "7"]:
             print("\t\t\t\t***INVALID ENTRY!***\nPlease try again") #Error check that forces user to input correct information

        if searchType == "1": #Sequential search function to find the title 
            searchQuery = input("\t\t\t\tEnter the TITLE:")
            print()
            sequentialSearch(title, searchQuery, foundList)
            if foundList:
                display("x", foundList, len(foundList))
            else: 
                print("\t\t\t\tNo records found.")
    
        if searchType == "2":  #Sequential search function to find the author 
            searchQuery = input("\t\t\t\tEnter the AUTHOR:")
            print()
            sequentialSearch(author, searchQuery, foundList)
            if foundList:
                display("x", foundList, len(foundList))
            else: 
                print("\t\t\t\tNo records found.")
           
        if searchType == "3": #Sequential search function to find the genre
            searchQuery = input("\t\t\t\tEnter the GENRE:")
            print()
            sequentialSearch(genre, searchQuery, foundList)
            if foundList:
                display("x", foundList, len(foundList))
            else: 
                print("\t\t\t\tNo records found.")
    
        if searchType == "4": #Binary and bubble sort function to find the library number 
            searchInput = input("\t\t\t\tEnter LIBRARY NUMBER:")
            print()
            bubbleSearch()
            binarySearch(searchInput, foundList)
            if foundList: 
                display("x" , foundList, len(foundList))
            else:
                print("\t\t\t\tNo record found.")
        
        if searchType == "5": #Displays all items listed with Available 
            searchQuery = "Available"
            sequentialSearch(status, searchQuery, foundList)
            if foundList:
                display("x", foundList, len(foundList))
            else: 
                print("\t\t\t\tNo records found.")

        if searchType == "6": #Displays all items listed with On loan 
            searchQuery = "On loan"
            sequentialSearch(status, searchQuery, foundList)
            if foundList:
                display("x", foundList, len(foundList))
            else: 
                print("\t\t\t\tNo records found.")

        elif searchType == "7":  #End of loop 
            print("\t\t\t\tExiting Program")
            print()
            print("\t\t\t\tThank you for using Book Finder")