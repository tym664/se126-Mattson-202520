#Tyler Mattson 
#W2D2 Text File Handling review with filters [Lab2]
#SE116 202502 (Morning Class)
#Date: January 14 2025


#Program Prompt-------------------------

#VARIABLE DICTIONARY--------------------
#totalRecs -> Total amount of information in the CSV file 
#roomsOver -> Rooms that are over capacity 
#ppl -> People number of people attending meeting in the room 
# maxCap -> Maximun capacity each room can hold 

#Imports--------------------------------

#Functions------------------------------
    #This fucntion is passed 2 values and returns the difference between them
import csv


def difference (people, maxCap):
    diff = maxCap - people
    return diff

#Main code------------------------------

#intitalize needed counting variables
totalRec = 0 
roomsOver = 0 
print (f"{"NAME":20}  {"MAX":5}   {"PPL":5}   {"OVER"}") 
print("------------------------------------------------------")

#Connecting to CSV file--------
with open("text files/classLab2.csv") as csvfile:  

    
    file = csv.reader(csvfile)


    for rec in file: 
        #Below code occurs for every record (row) in the file (text file) 

        #Assign each field data value to a friendly variable name 
        
        name = rec [0]
        max = int (rec[1]) #All text data read as a string, cast as a number 
        ppl = int (rec[2])
        totalRec +=1 

    #Call the difference() function 

        remaining = difference(ppl, max)  

    #Count and display rooms that are over capacity 


        if remaining < 0: #Can also be if remaning > max 

            roomsOver += 1 
            print (f"{name:20}  {max:5}   {ppl:5}   {abs(remaining):5}") 

#Connecting to CSV file--------

print(f"\nRooms currently OVER CAPACITY: {roomsOver}") 
print(f"Total rooms in file: {totalRec}\n\n")



