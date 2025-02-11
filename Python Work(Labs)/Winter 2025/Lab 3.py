#Tyler Mattson 
#Lab 3 In class lab, 1D & Parallel Lists
#Section: SE126 - 202502 (Morning Class) 
#Date: January 22 2024

#Thank you for helping me Katie. You're the best! 

#VARIABLE DICTIONARY
#===============================
#compType = Desktop or Laptop
#manu = Dell or HP
#proc = i5 or i7
#ram = 8 or 16 GB
#hd_1 = Hard drive 1 
#num_hd = Number of hard drives
#hd_2 = Hard Drive 2
#os = Operating System
#yr = Year machine was purchased
#old_desk = Old desktop
#old_lap = Old laptop
#===============================

#BASE PROGRAM CODE


#Importing CSV libary 
import csv

#Empty lists
compType =[]
manu = []
proc = []
ram = []
hd_1 = []
num_hd = []
hd_2 = []
os = []
yr = []

#Opening CSV file 
with open("filehandling.csv") as csvfile:

    file = csv.reader(csvfile)
    
#Headers for data placement     
    print("IT inventory:")
    print()
    print("=" * 130)
    print(f"{'Type':<10} {'Manufacturer':<15} {'Processor':<15} {'RAM(GB)':<10} {'HDD1'} \t{'Num HDD':>10} {'HDD2':>18} {'OS':>11.9} {'Purchase Year':>22}")
    print("=" * 130)

#For loop for handling data in the csv file
    
    for record in file:

#Conditional Statements for determing machine type and manufacturer
        if record[0] == 'D':
            compType.append("Desktop")
        else:
            compType.append("Laptop")
            
        if record[1] == 'DL':
            manu.append ("Dell")
        elif record[1] == 'HP':
            manu.append ("HP")
            
        else:
            manu.append ("Gateway")
            
#Defining other variables 
            
        proc.append (record[2])
        ram.append  (record[3])
        hd_1.append  (record[4])
        num_hd.append  (int(record[5]))

#Conditional statements for machines that have one or two HDD
        if int(record[5]) == 1:
            hd_2.append  ("----")
            os.append  (record[6])
            yr.append  (record[7])

        elif int(record[5]) == 2:
            hd_2.append  (record[6])
            os.append  (record[7])
            yr.append (record[8])

for index in range(0, len(compType)):
    
    print(f"{compType[index]:<10} {manu[index]:<15} {proc[index]:>5} {ram[index]:>15} {hd_1[index]:>10} {num_hd[index]:>12} {hd_2[index]:>21} {os[index]:>12} {yr[index]:>15}")

#Two 'for' loops to determine which desktops and laptops needs to be replaced 
old_desk = 0   
for index in range(0, len(yr)):
    if int(yr[index]) <= 16:
        if compType[index] == "Desktop":
            old_desk += 1


old_lap = 0    
for index in range(0, len(yr)):
    if int(yr[index]) <= 16:
        if compType[index] == "Laptop":
            old_lap += 1


#Number of desktops and laptops that need to be replaced and cost            
print()            
print("=" * 130)
print()
print(f"\t\t\tTotal number of desktops that need to be replaced: {old_desk} Cost: ${old_desk * 2000: 6.2f}")
print()
print(f"\t\t\tTotal number of laptops that need to be replaced: {old_lap} Cost: ${old_lap * 1500: 10.2f}")
print() 
print(f"\t\t\t\t\t\tTOTAL RECORDS IN FILE: {len(compType)}")
print()
print("=" * 130)
print()
            
        

         
        
        
            


        
           
                

         

    
       
    
    
    
    
    
            

