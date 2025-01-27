#Tyler Mattson 
#W4D1 Sequential Search [Lab4]
#SE116 202502 (Morning Class)
#Date: January 27 2025



#VARIABLE DICTIONARY--------------------

#Importing csv file 
import csv 

#Function to determine letter grade 
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
        let = "F" 
    else: 
        let = "ERROR" 

    return let # 'let' value replaces the function call in the main code 

#Create empty lists to hold data 
fName = []
lName = [] 
test1 = [] 
test2 = []
test3 = [] 

# Opening csv file to read data 
with open("text files/class_grades.csv") as csvfile: 
    file = csv.reader(csvfile) 

    for rec in file: 
        #Append the file data into appropiate lists, storing data into lists 
        fName.append (rec[0]) 
        lName.append (rec[1])
        test1.append (int(rec[2]))
        test2.append (int(rec[3]))
        test3.append (int(rec[4]))
#Disconnecting from file   


#process the list data to calc an avg test scores, find a letter grade equivalent 

num_avg = [] # Holds students numerical avg of test scores 
let_avg = [] # Holds students letter grades 

for i in range(0, len(fName)): # 'i' is shorthand for 'index' 
    a = (test1[i] + test2[i] + test3[i]) /3 
    #add avg to num_avg list 

    num_avg.append(a) 

    l = letter(a) #return value of letter() stored to 'l' 
    let_avg.append(i) 

#Print data to user 

print(f"{'FNAME':10} {'LNAME':10} {'T1':3} {'T2':>9} {'T3':>10} {'# AVG':>10} {'L AVG':>10}") 
print("=" * 75)

for i in range(0, len(fName)): 
    print(f"{fName[i]:10} {lName[i]:10} {test1[i]:<10} {test2[i]:<10} {test3[i]:<10} {num_avg[i]:6.2f} {let_avg[i]:<10} ") 

print("=" * 75)

#Write a program that allows a user to repeatdly search for a student by their last name or their letter grade 

print("Welcome to Student Search")

answer = input("Would you like to begin searching? [y/n?]")


while answer == "y": 
    print("\tSEARCH MENU")
    print("1. Search by LAST name")
    print("2. Search by LETTER GRADE")
    print("3. EXIT")
    search_type = input("Enter your search type [1-3]")
    
    if search_type == "1":
        print("1. Search by LAST name") 
        found = -1 

        search_name = input("Enter the LAST NAME of the Student")

        for i in range(0, len(lName)): 
            if search_name.lower() == lName[i].lower(): 
                found = i 

        
        if not found: 
            print(f"Your Search for {search_name} was not found") 
            print(f"Program is case senstive") 

        else: 
            print(f"Your Search for {search_name} was found") 

            for i in range(0, len(found)): 
            print(f"{fName[found[i]]:10} {lName[found[i]]:10} {test1[found[i]]:<10} {test2[found[i]]:<10} {test3[found[i]]:<10} {num_avg[found[i]]:<10} {let_avg[found[i]]:<10} ") 




        elif search_type == "2": 
            
