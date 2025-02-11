#Tyler Mattson 
#Mid-Term
#Section: SE126 - 202502 (Morning Class) 
#Date: Febuary 4th 2025


import csv 

firstName = []
lastName = [] 
email = [] 
department = [] 
phoneExt = [] 
officeNum = []
totalRecords = 0 
depNum = 0
depNum1 = 0

#Opening CSV file
with open("text files/westeros.csv") as csvfile:
    

    file = csv.reader(csvfile)
    
    for record in file: 

        totalRecords += 1 #Keeps track of each record being processed, adds total when new file is created 

        firstName.append (record[0])
        lastName.append (record[1])
        email.append (str(record[2]))
        department.append (record[3])
        officeNum.append (int(100+depNum))
        phoneExt.append (int(100 + depNum1)) 
    
             
        depNum += 5  #Assigns numbers to phone extension 
        depNum1 += 1  #Creates office number 
       
print()
print (f"\t\t\t\t\t\t\tEmployee data on file")
print("=" * 150)
print(f"{'FIRST':8} {'LAST':>11} {'EMAIL':>23} {'DEPARTMENT':>35} {'PhoneEXT':>27} {'Office Num':>22}")
print("-" * 150)
    
for i in range(0, len (firstName)):
    

    print(f"{firstName[i]:15} {lastName[i]:15} {email[i]:35} {department[i]:25}  {phoneExt[i]:10}  {officeNum[i]:20} ")

print("-" * 150)
print (f"\t\t\t\t\t\t\tTotal Records: {totalRecords}")
print("-" * 150)
print() 


#SEARCH FUNCTION--------------------------------------------------------------------------------------------------------------------------

print ("Welcome to the Westeros Services Directory Search.")
print("-" * 50)
print()
answer = input ("Would you like to start your search? {Y/N}").lower()

while answer == 'y': 
    print ("**Search Menu**")
    print ("1. Search by EMAIL")
    print ("2. Search by Department")
    print ("3. EXIT")

    search_type = input("Enter your search type [1-3]: ")

    
    if search_type == "1": 
        
        print("\tSearch by EMAIL")
        
        found = -1  
        searchEmail = input("Enter the email you would like to find") 

        for i in range(0, len(email)):
            

            if searchEmail.lower() == email[i].lower(): 
               
                found = i
       
        if found != -1:
            
            print(f"Your search for {searchEmail} was FOUND! Here is their data: ")
            print(f"{found[i]} {firstName[found[i]]:15} {lastName[found[i]]:15} {email[found[i]]:35} {department[found[i]]:25} {phoneExt[found[i]]:10}  {officeNum[found[i]]:20} ")
        else: 
            
            print(f"Your search for {searchEmail} was NOT FOUND!")
            print("Program is case senstive.")
    
    elif search_type == "2": 
        print("\tDepartment Search")

        found = []  
        searchDepart= input("Enter the DEPARTMENT you are looking for ") 

        
        for i in range(0, len(department)):
            

            if searchDepart.upper() == department[i]: 
                
                found.append(i)  
                print(f"Found {searchDepart} in INDEX {i}")

        
        if not found: 
            
            print(f"Your search for {searchDepart} was not found")
            print("Program is case senstive!")
        else: 
           
            print(f"Your search for {searchDepart} was found. Here is their data: ")

           
            for i in range(0, len(found)):
                print(f"{found[i]} {firstName[found[i]]:15} {lastName[found[i]]:15} {email[found[i]]:35} {department[found[i]]:25}  {phoneExt[found[i]]:10}  {officeNum[found[i]]:20} ")

    elif search_type == "3": 
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    if search_type == "1" or search_type == "2":
       
        answer = input("Would you like to search again? [y/n]: ").lower()


#CREATING FILE--------------------------------------------------------------------------------------------------------------------


file = open ("text files/midterm_choice1.csv" , 'w')

for i in range(0, len(firstName)):

    file.write(f"{firstName[i]}, {lastName[i]}, {email[i]},  {department[i]}, {phoneExt[i]}, {officeNum[i]}\n")

file.write(f"Total Records: {totalRecords}") 

file.close()

print ("Program has finished running. Thank you") 




