#W3D2 List Review- 1D list and parallel Lists
#this file uses: class_grade.csv

#VARIABLE DICTIONARY--------------------


#Imports--------------------------------
import csv


#Functions------------------------------

#Main code------------------------------

totalRecords = 0 

firstName = []  
lastName = []
test1 = []
test2 = []
test3 =[] 
avg = []

with open ("text files/class_grades.csv")as csvfile: 

    file = csv.reader(csvfile)

    for rec in file: 
        #for every record in the file do the following 

        #print(f"{rec[0]:10}\t{rec[1]:10}")
        #add the reccord data to its corresponding list (1 list per field) 
        #append --> to add to the end 

        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect from file 

#basic processing - use 1D parallel lists to print all the data to the console 
for index in range(0, len(firstName)):  #len() --> length of collection, returns # of items 
    print(f"\nINDEX {'#':3} : {'First' :10} {'Last':10}  {'T1':3}  {'T2':3}  {'T3':3} {'AVG':3}")
                           
    #index --> key of the list, allows access to one specific value 
    print(f"INDEX {index:3} {firstName[index]:10} {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3} {avg[index]:3.2f}")
    print("-" *55)


#create a new list to hold each students avg test scores 

totalAvg = []

#process the current student data to find and store each students tests score avg to the avg list 

for i in range(0, len(avg)):
    totalAvg += avg[i] 

classAvg = totalAvg /len(avg)
print(f"\n The Class Average of these {len(avg)} students is: {classAvg:.2f}")
    #a = (test1[i] + test2[i] + test3[i]) / 3
    #avg.append(a) 
   


    

    