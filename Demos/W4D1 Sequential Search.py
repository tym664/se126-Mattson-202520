#Tyler Mattson 
#W2D2 Text File Handling review with filters [Lab2]
#SE116 202502 (Morning Class)
#Date: January 28 2025 
#PROGRAM PROMPT: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

#--IMPORTS---------------------------------------------------------
import csv
#--FUNCTIONS-------------------------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let ="F"
    else:
        let = "ERROR"

    return let
#--MAIN EXECUTING CODE---------------------------------------------
#Empty lists 
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

#connecting to the file --------
with open("text files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #store data from current record to corresponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)

        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#process the lists to create and store each student's numeric average as well as letter grade average, then display all data back to the user
num_avg = []        #holds student's numeric avg: (test1 + test2 + test3) / 3
let_avg = []        #holds student's letter avg: letter(num_avg) return

for i in range(0, len(firstName)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    let_avg.append(letter(a))

#print field headers for display below
print(f"{'FIRST':10}  {'LAST':10}  {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6}  {'L AVG'}")
print("-----------------------------------------------------------------------------")
#processing through lists for display
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.1f}  {let_avg[i]}")
print("-----------------------------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE: {len(firstName)}")


print("\tWelcome to the Student Search Program")

answer = input("Would you like to start your search? [y/n]: ").lower()

while answer == "y":
    #show user search menu 
    print("\t~Search Menu~")
    print("1. Search by LAST name")         #one search value found
    print("2. Search by LETTER grade")      #multiple search values found
    print("3. EXIT")
    #gain search type 
    search_type = input("Enter your search type [1-3]: ")

    #filter search options based on type
    if search_type == "1": 
        
        print("\tLAST NAME SEARCH~")
        #step 1: set-up and gain search query
        found = -1  
        search_last = input("Enter the last name you wish to find: ") #name we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(lastName)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_last.lower() == lastName[i].lower(): 
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #last name FOUND!
            print(f"Your search for {search_last} was FOUND! Here is their data: ")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {let_avg[found]}")
        else: 
            #NOT found
            print(f"Your search for {search_last} was NOT FOUND!")
            print("Program is case senstive.")
    
    elif search_type == "2": #LETTER GRADE
        print("\tLETTER GRADE SEARCH")

        #sequential search - search for a collection of students based on their Letter Grade Average
        #this version of sequential search is looking for MULTIPLE items, based on a specific letter grade

        #step 1: set-up and gain search query
        found = []  #empty list, found locations (index) will be stored if/when found
        search_let= input("Enter the LETTER GRADE you wish to find: ") #grade we are looking through all students for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(let_avg)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_let.upper() == let_avg[i]: 
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
                print(f"Found a {search_let} grade in INDEX {i}")

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {search_let} was not found")
            print("Program is case senstive!")
        else: 
            #last name FOUND!
            print(f"Your search for {search_let} was found. Here is their data: ")

            #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found)):
                print(f"{found[i]}:  {firstName[found[i]]:10}  {lastName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.1f}  {let_avg[found[i]]}")
    elif search_type == "3": #exit
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop - answer should be able to change value! 
    if search_type == "1" or search_type == "2":
        #when search_type == "3" the user has chosen to exit, and if they did not provide a 1, 2, or 3 to search_type then they will automatically be brought back through the loop to see the menu again
        answer = input("Would you like to search again? [y/n]: ").lower()


print("\nThanks for using the search program.\n")