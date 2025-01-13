#W2D1 - Text File Handling - Introduction

#Step 1: Import the csv (comma seperated value) libary 
import csv 

total_records = 0 #the total number of records (rows) in the file 

#conntecting to the files path - swith \to/
with open ("textFiles/simple.csv") as csvfile: 
    #indent 1 level! (new block) 
    # 
    # 
    # allow processor to read the file data 
    file = csv.reader(csvfile) 
    
    #loop through every record (row) in the file 
    for record in file: 
        
        
        total_records += 1 
        
    print (f"\nTOTAL RECORDS: {total_records}\n")