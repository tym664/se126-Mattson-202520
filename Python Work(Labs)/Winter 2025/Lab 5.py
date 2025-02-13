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
#totalRecords = How many times the program ran through the records 
#===============================================================================

#Importing CSV libary to handle
import csv 


#Function

def display(x, foundList, records): 

    print(f"{libraryNum[i]:5} {title[i]:25} {author[i]:15} {genre[i]:20} {pgCount[i]:5} {status[i]:5}")
    print("=" * 80)
    if x != "x": 
      print(f"{libraryNum[x]:5} {title[x]:25} {author[x]:15} {genre[x]:20} {pgCount[x]:5} {status[x]:5}")
    




    


#Empty Lists for storing data 
libraryNum = [] 
title = [] 
author = [] 
genre = [] 
pgCount = [] 
status = [] 
totalRecords = 0 

with open("text files/book_list.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for record in file: 

        totalRecords += 1 #Keeps track of each record being processed 

        libraryNum.append (record[0])
        title.append (record[1])
        author.append (record[2])
        genre.append (record[3])
        pgCount.append (record[4])
        status.append (record[5]) 

print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20}  {'PAGE COUNT':5} {'STATUS':5}")
print ("=" * 110)

for i in range (0, len(libraryNum)):

    print(f"{libraryNum[i]:5} {title[i]:25} {author[i]:15} {genre[i]:20} {pgCount[i]:5} {status[i]:5}")


display("x",0,len(libraryNum)) 
print()
ans = input("Would you like to enter the search program? [y/n]").lower()


while ans != "y" and ans != "n": #This loop makes sure the user inputs the correct information 
    print("***INVALID ENTRY!***")
    print()
    ans = input("Would you like to enter the search program? [y/n]").lower()
    
while ans == "y":

    print("\t**Persoal Library Menu**")
    print() 
    print("1. Search by TITLE")
    print("2. Search by AUTHOR") 
    print("3. Search by GENRE") 
    print("4. Search by LIBRARY NUMBER")
    print("5. Search by AVAILABLE")
    print("6. Search by ON LOAN")
    print("7. EXIT")
    print()
    print ("=" * 80 )

    searchType =  input("\nHow would you like to search today? [1-8]: ") 

    if searchType not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
         print("***INVALID ENTRY!***\nPlease try again") #Error check that forces user to input correct information
